""" Clustered Learning of Approximate Manifolds.
"""
import concurrent.futures
import logging
import pickle
from collections import deque
from operator import itemgetter
from typing import Set, Dict, Iterable, BinaryIO, List, Union, Tuple, IO, Any

import numpy as np
from scipy.spatial.distance import cdist

from pyclam.types import Data, Radius, Vector, Metric

SUBSAMPLE_LIMIT = 100
BATCH_SIZE = 10_000
LOG_LEVEL = logging.INFO

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s:%(levelname)s:%(name)s:%(module)s.%(funcName)s:%(message)s"
)


class Cluster:
    """ A cluster of points.

    Clusters maintain:
        references to their their children,
        the manifold to which they belong,
        and the indices of the points they are responsible for.

    You can compare clusters, hash them, partition them, perform tree search, prune them, and more.
    Cluster implements methods that create and utilize the underlying tree structure used by Manifold.
    """

    def __init__(self, manifold: 'Manifold', argpoints: Vector, name: str, **kwargs):
        """
        A Cluster needs to know the manifold it belongs to and the indexes of the points it contains.
        The name of a Cluster indicates its position in the tree.

        :param manifold: The manifold to which the cluster belongs.
        :param argpoints: A list of indexes of the points that belong to the cluster.
        :param name: The name of the cluster indicating its position in the tree.
        """
        logging.debug(f"Cluster(name={name}, argpoints={argpoints})")
        self.manifold: 'Manifold' = manifold
        self.argpoints: Vector = argpoints
        self.name: str = name
        self.children: Union[None, List['Cluster']] = None

        # Reference to the distance function for easier usage
        self.distance = self.manifold.distance

        # list of candidate neighbors.
        # This helps with a highly efficient neighbor search for clusters in the tree.
        # Candidates have the following properties:
        #     candidate.depth <= self.depth
        #     self.distance_from([candidate.argmedoid]) <= candidate.radius + self.radius * 4
        self.candidates: Union[Dict['Cluster', float], None] = None

        self.cache: Dict[str, Any] = dict()
        self.cache.update(**kwargs)

        # This is used while reading clusters from file during Cluster.from_json().
        if not argpoints:
            if 'children' in self.cache:
                self.children: Set[Cluster] = {child for child in self.cache['children']}
                self.argpoints: List[int] = [p for child in self.children for p in child.argpoints]
            else:
                raise ValueError(f'Cluster {name} needs argpoints of children when reading from file')
        return

    def __eq__(self, other: 'Cluster') -> bool:
        """ Two clusters are identical if they have the same name and the same set of points. """
        return all((
            self.name == other.name,
            set(self.argpoints) == set(other.argpoints),
        ))

    def __lt__(self, other: 'Cluster') -> bool:
        """ For sorting clusters in Graphs. Sorts by depth, breaking ties by name. """
        return (self.name < other.name) if self.depth == other.depth else (self.depth < other.depth)

    def __bool__(self) -> bool:
        return self.cardinality > 0

    def __hash__(self):
        """ Be careful to use this only with other clusters in the same tree. """
        return hash(self.name)

    def __str__(self) -> str:
        return self.name or 'root'

    def __repr__(self) -> str:
        if 'repr' not in self.cache:
            self.cache['repr'] = ': '.join([self.name, ', '.join(map(str, sorted(self.argpoints)))])
        return self.cache['repr']

    def __iter__(self) -> Vector:
        # Iterates in batches, instead of by element.
        for i in range(0, self.cardinality, BATCH_SIZE):
            yield self.argpoints[i:i + BATCH_SIZE]

    def __contains__(self, point: Data) -> bool:
        """ Check weather the given point could be inside this cluster. """
        return self.overlaps(point=point, radius=0.)

    @property
    def parent(self) -> 'Cluster':
        if 'parent' not in self.cache:
            if self.depth > 0:
                self.cache['parent'] = self.manifold.ancestry(self)[-2]
            else:
                raise ValueError(f"root cluster has no parent")
        return self.cache['parent']

    @property
    def cardinality(self) -> int:
        return len(self.argpoints)

    @property
    def metric(self) -> str:
        """ The metric used in the manifold. """
        return self.manifold.metric

    @property
    def depth(self) -> int:
        """ The depth in the tree at which the cluster exists. """
        if 'depth' not in self.cache:
            self.cache['depth'] = self.name.count('0')
        return self.cache['depth']

    def distance_from(self, x1: Union[List[int], Data]) -> np.ndarray:
        """ Helper to ease calculation of distance from the cluster center. """
        return self.distance([self.argmedoid], x1)[0]

    @property
    def points(self) -> Data:
        """ An iterator, in batches, over the points in the Clusters. """
        for i in range(0, self.cardinality, BATCH_SIZE):
            yield self.manifold.data[self.argpoints[i:i + BATCH_SIZE]]

    @property
    def argsamples(self) -> Vector:
        """ Indices of samples chosen for finding poles.

        Ensures that there are at least 2 different points in samples,
        otherwise returns a single sample that represents the entire cluster.
        i.e., if len(argsamples) == 1, the cluster contains only duplicates.
        """
        if 'argsamples' not in self.cache:
            logging.debug(f"building cache for {self}")
            if self.cardinality <= SUBSAMPLE_LIMIT:
                n = len(self.argpoints)
                indices = self.argpoints
            else:
                n = int(np.sqrt(self.cardinality))
                indices = [int(i) for i in np.random.choice(self.argpoints, n, replace=False)]

            # Handle Duplicates.
            if self.distance(indices, indices).max(initial=0.) == 0.:
                indices = np.unique(self.manifold.data[self.argpoints], return_index=True, axis=0)[1]
                indices = [self.argpoints[i] for i in indices][:n]

            # Cache it.
            self.cache['argsamples'] = indices
        return self.cache['argsamples']

    @property
    def samples(self) -> Data:
        """ Returns the samples from the cluster. Samples are used in computing approximate centers and poles.
        """
        return self.manifold.data[self.argsamples]

    @property
    def nsamples(self) -> int:
        """ The number of samples for the cluster. """
        return len(self.argsamples)

    @property
    def argcenter(self) -> int:
        return self.argmedoid

    @property
    def center(self) -> Data:
        return self.medoid

    @property
    def argmedoid(self) -> int:
        """ The index used to retrieve the medoid. """
        if 'argmedoid' not in self.cache:
            logging.debug(f"building cache for {self}")
            argmedoid = np.argmin(self.distance(self.argsamples, self.argsamples).sum(axis=1))
            self.cache['argmedoid'] = self.argsamples[int(argmedoid)]
        return self.cache['argmedoid']

    @property
    def centroid(self) -> Data:
        """ The Geometric Mean of the cluster. """
        return np.average(self.samples, axis=0)

    @property
    def medoid(self) -> Data:
        """ The Geometric Median of the cluster. """
        return self.manifold.data[self.argmedoid]

    @property
    def argradius(self) -> int:
        """ The index of the point which is farthest from the medoid. """
        if ('argradius' not in self.cache) or ('radius' not in self.cache):
            logging.debug(f'building cache for {self}')

            def argmax_max(b):
                distances = self.distance_from(b)
                argmax = int(np.argmax(distances))
                return b[argmax], distances[argmax]

            argradii_radii = [argmax_max(batch) for batch in iter(self)]
            argradius, radius = max(argradii_radii, key=itemgetter(1))
            if radius < 0:
                raise ValueError(f'got cluster {self.name} with negative radius. '
                                 f'Make sure that the distance function used always returns non-negative values.')

            self.cache['argradius'], self.cache['radius'] = int(argradius), float(radius)
        return self.cache['argradius']

    @property
    def radius(self) -> Radius:
        """ The radius of the cluster.

        Computed as distance from medoid to the farthest point in the cluster.
        """
        if 'radius' not in self.cache:
            logging.debug(f'building cache for {self}')
            _ = self.argradius
        return self.cache['radius']

    @property
    def local_fractal_dimension(self) -> float:
        """ The local fractal dimension of the cluster. """
        if 'local_fractal_dimension' not in self.cache:
            logging.debug(f'building cache for {self}')
            if self.nsamples == 1:
                self.cache['local_fractal_dimension'] = 1.
            else:
                count = sum([
                    1 if distance <= (self.radius / 2) else 0
                    for batch in iter(self)
                    for distance in self.distance_from(batch)
                ])
                self.cache['local_fractal_dimension'] = 1. if count == 0 else np.log2(self.cardinality / count)
        return self.cache['local_fractal_dimension']

    @property
    def ancestors(self) -> List['Cluster']:
        """ Ancestry of self, excluding self.
        """
        return self.manifold.ancestry(self)[:-1]

    @property
    def descendents(self) -> List['Cluster']:
        """ All clusters in the subtree starting at self, excluding self.
        """
        return [cluster for layer in self.manifold.layers[self.depth + 1:]
                for cluster in layer.clusters
                if self.name == cluster.name[:len(self.name)]]

    @property
    def ratios(self) -> List[float]:
        if 'ratios' not in self.cache:
            if self.depth > 0:
                lfd_ratio = self.local_fractal_dimension / self.parent.local_fractal_dimension
                self.cache['ratios'] = [  # Child/Parent Ratios
                    1 / (1 + np.exp(-lfd_ratio)),  # local fractal dimension
                    self.cardinality / self.parent.cardinality,  # cardinality
                    max(self.radius, 1e-16) / max(self.parent.radius, 1e-16)  # radius
                ]
            else:
                self.cache['ratios'] = [1., 1., 1.]
        return self.cache['ratios']

    @property
    def ema_ratios(self) -> List[float]:
        if 'ema_ratios' not in self.cache:
            if self.depth > 0:
                smoothing, period = 2, 10
                alpha = smoothing / (1 + period)
                current, previous = np.asarray(self.ratios), np.asarray(self.parent.ratios)
                self.cache['ema_ratios'] = alpha * current + (1 - alpha) * previous
                self.cache['ema_ratios'][0] = 1 / (1 + np.exp(-self.cache['ema_ratios'][0]))
            else:
                self.cache['ema_ratios'] = [1., 1., 1.]
        return self.cache['ema_ratios']

    def clear_cache(self) -> None:
        """ Clears the cache for the cluster. """
        logging.debug(f'clearing cache for {self}')
        self.cache.clear()
        return

    def overlaps(self, point: Data, radius: Radius) -> bool:
        """ Checks if point is within radius + self.radius of cluster. """
        return self.distance_from(np.asarray([point]))[0] <= (self.radius + radius)

    def _find_poles(self) -> List[int]:
        """ Poles are approximately the two farthest points in the cluster.

        :return: list of indexes of the poles.
        """
        assert len(self.argsamples) > 1, f'must have more than one unique point before poles can be chosen'

        if len(self.argsamples) > 2:
            farthest = self.argsamples[int(np.argmax(self.distance([self.argradius], self.argsamples)[0]))]
            poles = [self.argradius, farthest]
        else:
            poles = [p for p in self.argsamples]

        assert len(set(poles)) == len(poles), f'poles cannot contain duplicate points.'
        return poles

    def partition(self, *criterion) -> Set['Cluster']:
        """ Partition cluster into children.

        If the cluster can be partitioned, partition it and return list of children.
        Otherwise, return empty list.

        :param criterion: criteria to use to determine if a Cluster can be partitioned.
        :return: List of children.
        """
        if not all((
            len(self.argsamples) > 1,
            *(c(self) for c in criterion),
        )):  # cluster cannot be partitioned
            logging.debug(f'{self} cannot be partitioned.')
            self.children = list()
        else:
            poles: List[int] = self._find_poles()
            child_argpoints: List[List[int]] = [[p] for p in poles]

            for batch in iter(self):
                argpoints = [p for p in batch if p not in poles]
                if len(argpoints) > 0:
                    distances = self.distance(argpoints, poles)
                    [child_argpoints[int(np.argmin(row))].append(p) for p, row in zip(argpoints, distances)]

            child_argpoints.sort(key=len)
            self.children: Set['Cluster'] = {
                Cluster(self.manifold, argpoints, self.name + '0' + '1' * i)
                for i, argpoints in enumerate(child_argpoints)
            }
            [child.cache.update({'parent': self}) for child in self.children]

            logging.debug(f'{self} was partitioned into {len(self.children)} child clusters.')

        return self.children

    def _tree_search(self, point: Data, radius: Radius, depth: int) -> Dict['Cluster', Radius]:
        distance = self.distance_from(np.asarray([point]))[0]
        assert distance <= radius + self.radius, f'_tree_search was started with no overlap.'
        assert self.depth < depth, f'_tree_search needs to have depth ({depth}) > self.depth ({self.depth}). '

        # results and candidates ONLY contain clusters that have overlap with point
        results: Dict['Cluster', Radius] = dict()
        candidates: Dict['Cluster', Radius] = {self: distance}
        for _ in range(self.depth, depth):
            # if cluster was not partitioned any further, add it to results.
            results.update({cluster: distance for cluster, distance in candidates.items() if not cluster.children})

            # filter out only those candidates that were partitioned.
            candidates = {cluster: distance for cluster, distance in candidates.items() if cluster.children}

            # proceed down the tree
            children: List[Cluster] = [child for candidate in candidates.keys() for child in candidate.children]
            if len(children) == 0:
                break

            # filter out clusters that are too far away to possibly contain any hits.
            argcenters = [child.argmedoid for child in children]
            distances = self.distance(np.asarray([point]), argcenters)[0]
            radii = [radius + child.radius for child in children]
            candidates = {
                cluster: distance
                for cluster, distance, radius in zip(children, distances, radii)
                if distance <= radius
            }

            if len(candidates) == 0:
                break

        # put all potential clusters in one dictionary.
        results.update(candidates)
        assert all((depth >= cluster.depth for cluster in results.keys()))
        return results

    def tree_search(self, point: Data, radius: Radius, depth: int) -> Dict['Cluster', Radius]:
        """ Searches down the tree for clusters that overlap point with radius at depth. """
        logging.debug(f'tree_search(point={point}, radius={radius}, depth={depth}')
        if depth == -1:
            depth = len(self.manifold.layers)
        if depth < self.depth:
            raise ValueError('depth must not be less than cluster.depth')

        results: Dict['Cluster', Radius] = dict()
        if self.depth == depth:
            results = {self: self.distance_from(np.asarray([point]))[0]}
        elif self.overlaps(point, radius):
            results = self._tree_search(point, radius, depth)

        return results

    def json(self):
        """ This is used for writing the manifold to disk. """
        data = {
            'name': self.name,
            'argpoints': None,  # Do not save argpoints until at leaves.
            'children': [],
            'radius': self.radius,
            'argradius': self.argradius,
            'argsamples': self.argsamples,
            'argmedoid': self.argmedoid,
            'local_fractal_dimension': self.local_fractal_dimension,
            'candidates': None if self.candidates is None else {c.name: d for c, d in self.candidates.items()},
        }
        if self.children:
            data['children'] = [c.json() for c in self.children]
        else:
            data['argpoints'] = self.argpoints
        return data

    @staticmethod
    def from_json(manifold, data):
        children = set([Cluster.from_json(manifold, c) for c in data.pop('children', [])])
        return Cluster(manifold, children=children, **data)


class Edge:
    """ An Edge is a connection between two clusters.
    """
    def __init__(self, clusters: Tuple[Cluster, Cluster], distance: float):
        left, right = clusters
        if right < left:
            left, right = right, left
        else:
            pass

        self._left: Cluster = left
        self._right: Cluster = right
        self._distance: float = distance

    def __eq__(self, other: 'Edge') -> bool:
        return self.clusters == other.clusters

    def __str__(self) -> str:
        return f'{str(self.left)} -- {str(self.right)}'

    def __hash__(self) -> int:
        return hash(str(self))

    def __contains__(self, cluster: Cluster) -> bool:
        return cluster in self.clusters

    @property
    def clusters(self) -> Tuple[Cluster, Cluster]:
        return self._left, self._right

    @property
    def left(self) -> Cluster:
        return self._left

    @property
    def right(self) -> Cluster:
        return self._right

    @property
    def distance(self) -> float:
        return self._distance

    @property
    def to_self(self) -> bool:
        return self.left.name == self.right.name

    def neighbor(self, cluster: Cluster) -> Cluster:
        if cluster in self:
            return self.left if cluster.name == self.right.name else self.right
        else:
            raise ValueError(f'Cluster {cluster.name} is not in this edge.')


class Graph:
    """ An induced graph from clusters in the tree.

    Clusters form the nodes, and two clusters with overlapping volumes have an edge connecting them.

    The Graph Invariant:
        * Every data point used to build the Manifold is also present in a Graph.
        * Each point is present in exactly one Cluster.

    This invariant only holds for full graphs, and not for subgraphs or components.

    """
    # TODO: Implement dump/load

    def __init__(self, *clusters):
        logging.debug(f'Graph(clusters={list(map(str, clusters))})')
        assert all(isinstance(c, Cluster) for c in clusters), 'all inputs to the Graph must be clusters.'

        self.clusters: Set[Cluster] = {cluster for cluster in clusters}
        self.edges: Set[Edge] = set()
        self.is_built: bool = False  # this flag is set to True at the end of build_edges.
        self.cache: Dict[str, Any] = dict()

    def __eq__(self, other: 'Graph') -> bool:
        """ Two Graphs are identical if they have the same sets of clusters and edges. """
        return (self.clusters == other.clusters) and (self.edges == other.edges)

    def __bool__(self) -> bool:
        return self.cardinality > 0

    def __iter__(self) -> Iterable[Cluster]:
        yield from self.clusters

    def __str__(self) -> str:
        if 'str' not in self.cache:
            self.cache['str'] = ', '.join(sorted(list(map(str, self.clusters))))
        return self.cache['str']

    def __repr__(self) -> str:
        if 'repr' not in self.cache:
            self.cache['repr'] = '\n'.join(sorted(list(map(repr, self.clusters))))
        return self.cache['repr']

    def __hash__(self) -> int:
        return hash(str(self))

    def __contains__(self, cluster: Cluster) -> bool:
        return cluster in self.clusters

    @property
    def edges_dict(self) -> Dict[Cluster, Set[Edge]]:
        if 'edges_dict' not in self.cache:
            self.cache['edges_dict'] = {
                cluster: {edge for edge in self.edges if cluster in edge}
                for cluster in self.clusters
            }
        return self.cache['edges_dict']

    @property
    def cardinality(self) -> int:
        return len(self.clusters)

    @property
    def population(self) -> int:
        return sum((cluster.cardinality for cluster in self.clusters))

    @property
    def manifold(self) -> 'Manifold':
        return next(iter(self.clusters)).manifold

    @property
    def metric(self) -> Metric:
        return next(iter(self.clusters)).metric

    @property
    def depth(self) -> int:
        if 'depth' not in self.cache:
            self.cache['depth'] = max((cluster.depth for cluster in self.clusters))
        return self.cache['depth']

    @property
    def min_depth(self) -> int:
        if 'min_depth' not in self.cache:
            self.cache['min_depth'] = min((cluster.depth for cluster in self.clusters))
        return self.cache['min_depth']

    @property
    def depth_range(self) -> Tuple[int, int]:
        return self.min_depth, self.depth

    @property
    def components(self) -> Set['Graph']:
        """ Returns the set of all connected components in the Graph. """
        if not self.is_built:
            self.build_edges()

        if 'components' not in self.cache:
            components: Set['Graph'] = set()
            unvisited: Set[Cluster] = {cluster for cluster in self.clusters}
            while unvisited:
                component: Set[Cluster] = self.traverse(unvisited.pop())
                unvisited -= component
                components.add(self.subgraph(component))

            self.cache['components'] = components

        return self.cache['components']

    def component_containing(self, cluster: Cluster) -> 'Graph':
        """ returns the connected component to which cluster belongs. """
        for component in self.components:
            if cluster in component:
                return component
        else:
            raise ValueError(f'cluster {str(cluster)} not found in any component.')

    def subgraph(self, clusters: Set[Cluster]) -> 'Graph':
        """ returns the subgraph containing only the given clusters. """
        if not clusters.issubset(self.clusters):
            raise ValueError(f'Some clusters were not found in the graph.')

        graph: Graph = Graph(*clusters)
        graph.edges = {edge for edge in self.edges if set(edge.clusters).issubset(clusters)}
        graph.is_built = True
        return graph

    def clear_cache(self) -> None:
        self.cache.clear()
        return

    @staticmethod
    def _find_candidates(cluster: Cluster) -> None:
        """ Update the cluster.candidates dictionary. """
        radius: float = cluster.manifold.root.radius
        ancestry: List[Cluster] = cluster.manifold.ancestry(cluster)

        # iterate over non-root clusters in ancestry
        for depth in range(1, cluster.depth + 1):
            if ancestry[depth].radius > 0:
                radius = ancestry[depth].radius

            # This ensures that candidates are calculated once per cluster
            if ancestry[depth].candidates is None:
                # Keep candidates from parent
                candidates: Dict[Cluster, float] = {c: 0. for c in ancestry[depth - 1].candidates}

                # Get all children of candidates at the same depth.
                candidates.update({
                    child: 0.
                    for c in ancestry[depth - 1].candidates
                    for child in c.children
                    if c.depth == (depth - 1)
                })

                if len(candidates) > 0:
                    distances = ancestry[depth].distance_from([c.argmedoid for c in candidates])
                    ancestry[depth].candidates = {
                        c: float(d)
                        for c, d in zip(candidates, distances)
                        # The factor of 4 is a safe bet for now.
                        # The factor might change after an in-depth analysis of radii trends.
                        if d <= c.radius + radius * 4
                    }
                else:
                    ancestry[depth].candidates = dict()
        return

    def _find_neighbors(self, cluster: Cluster) -> None:
        """ Find all neighbors of cluster and update the set of edges. """
        if cluster.candidates is None:
            self._find_candidates(cluster)

        self.edges.update({
            Edge((cluster, candidate), distance)
            for candidate, distance in cluster.candidates.items()
            if all((
                cluster != candidate,  # prevent self-edges
                candidate in self.clusters,  # only make edges to other clusters in the graph
                distance <= cluster.radius + candidate.radius,  # make sure of volume overlap
            ))
        })
        return

    def build_edges(self) -> 'Graph':
        """ Calculates all edges for the Graph.

        We define two clusters to share an edge when those two clusters have overlapping volumes.
        """
        logging.info(f'building edges for graph with {self.cardinality} clusters in {list(self.depth_range)} depth range.')

        # build edges
        [self._find_neighbors(cluster) for cluster in self.clusters]
        self.is_built = True
        return self

    def edges_from(self, cluster: Cluster) -> List[Edge]:
        """ returns all edges that connect to cluster. """
        return list(self.edges_dict[cluster])

    def neighbors(self, cluster: Cluster) -> List[Cluster]:
        """ returns all neighbors of cluster. """
        return [edge.neighbor(cluster) for edge in self.edges_from(cluster)]

    def distances(self, cluster: Cluster) -> List[float]:
        """ returns distances to each neighbor of cluster. """
        return [edge.distance for edge in self.edges_from(cluster)]

    def traverse(self, start: Cluster) -> Set[Cluster]:
        """ Graph traversal starting at start. """
        if not self.is_built:
            self.build_edges()

        logging.debug(f'starting traversal from {start}')
        visited: Set[Cluster] = set()
        frontier: Set[Cluster] = {start}

        while frontier:
            visited.update(frontier)
            frontier = {
                neighbor for cluster in frontier
                for neighbor in self.neighbors(cluster)
                if neighbor not in visited
            }

        return visited

    def bft(self, start: Cluster) -> Set[Cluster]:
        """ Breadth-First traversal starting at start. """
        if not self.is_built:
            self.build_edges()

        logging.debug(f'starting traversal from {start}')
        visited: Set[Cluster] = set()
        queue = deque([start])

        while queue:
            cluster = queue.popleft()
            if cluster not in visited:
                visited.add(cluster)
                queue.extend([neighbor for neighbor in self.neighbors(cluster) if neighbor not in visited])
            else:
                continue

        return visited

    def dft(self, start: Cluster) -> Set[Cluster]:
        """ Depth-First traversal starting at start. """
        if not self.is_built:
            self.build_edges()
        else:
            pass

        logging.debug(f'starting traversal from {start}')
        visited: Set[Cluster] = set()
        stack: List[Cluster] = [start]

        while stack:
            cluster = stack.pop()
            if cluster not in visited:
                visited.add(cluster)
                stack.extend([neighbor for neighbor in self.neighbors(cluster) if neighbor not in visited])

        return visited

    def _add(self, cluster: Cluster) -> None:
        """ Adds the cluster and all associated edges to the graph.

        Assumes that the cluster is not already in the graph.
        Caller need to invalidate cache.
        """
        self.clusters.add(cluster)
        self._find_neighbors(cluster)
        return

    def _remove(self, cluster: Cluster) -> None:
        """ Removes the cluster and all associated edges from the graph.

        Assumes that the cluster is in the graph.
        Caller need to invalidate cache.
        """
        self.edges -= set(self.edges_from(cluster))
        self.clusters.remove(cluster)
        return

    def replace_clusters(self, removals: Set[Cluster], additions: Set[Cluster]) -> 'Graph':
        """ Replace the Clusters in removals by the clusters in additions.

        The set of points in the to-be-removed clusters must be the same as the set of points in the to-be-added clusters.

        :param removals: a set of Clusters to be removed from the graph.
        :param additions: a set of Clusters to be added to the graph.
        :return: the updated graph.
        """
        if not removals.issubset(self.clusters):
            raise ValueError(f'cannot remove clusters that are not in the graph.')
        elif len(additions.intersection(self.clusters)) > 0:
            raise ValueError(f'Cannot add clusters that are already in the graph.')
        else:
            added_points: Set[int] = {point for cluster in additions for point in cluster.argpoints}
            removed_points: Set[int] = {point for cluster in removals for point in cluster.argpoints}
            if added_points != removed_points:
                raise ValueError(f'Mismatch between points being replaced. '
                                 f'Clusters being added must have the same set of points as those being removed')

        [self._remove(cluster) for cluster in removals]
        [self._add(cluster) for cluster in additions]
        self.clear_cache()
        return self


class Manifold:
    """
    The Manifold's main job is to organize the underlying Clusters and Graphs.
    It does this by providing the ability to reset the build the Cluster-tree, the Graph-stack, and the optimal Graph.
    With the tree and the graphs, Manifold provides utilities for:
        rho-nearest neighbors search,
        k-nearest neighbors search,
    """

    def __init__(
            self,
            data: Data,
            metric: Metric,
            argpoints: Union[Vector, float] = None,
            **kwargs
    ):
        """ A Manifold needs the data from which to learn the manifold, and a distance function to use while doing so.

        :param data: The data to learn. This should be a numpy.ndarray or a numpy.memmap.
        :param metric: The distance function to use for the data.
                       Any distance function allowed by scipy.spatial.distance is allowed here.
        :param argpoints: Optional. List of indexes or portion of data to which to restrict Manifold.
        """
        logging.debug(f'Manifold(data={data.shape}, metric={metric}, argpoints={argpoints})')
        self.data: Data = data
        self.metric: Metric = metric

        if argpoints is None:
            self.argpoints = list(range(self.data.shape[0]))
        elif type(argpoints) is list:
            self.argpoints = list(map(int, argpoints))
        elif type(argpoints) is float:
            self.argpoints = np.random.choice(
                self.data.shape[0],
                int(self.data.shape[0] * argpoints),
                replace=False
            )
            self.argpoints = list(map(int, self.argpoints))
        else:
            raise ValueError(f"Invalid argument to argpoints. {argpoints}")

        self.root: Cluster = Cluster(self, self.argpoints, '')
        self.layers: List[Graph] = [Graph(self.root)]  # layer-graphs by depth in the tree
        self.graphs: List[Graph] = list()  # optimal-graphs build from selection criteria

        self.cache: Dict[str, Any] = dict()
        self.cache.update(**kwargs)
        return

    def __eq__(self, other: 'Manifold') -> bool:
        """ Two manifolds are identical if they have the same metric and the same leaf-clusters. """
        return self.metric == other.metric and set(self.layers[-1]) == set(other.layers[-1])

    def __iter__(self) -> Iterable[Graph]:
        yield from self.layers

    def __getitem__(self, depth: int) -> Graph:
        return self.layers[depth]

    def __str__(self) -> str:
        if 'str' not in self.cache:
            self.cache['str'] = f'{self.metric}-{", ".join((str(p) for p in self.argpoints))}'
        return self.cache['str']

    def __repr__(self) -> str:
        if 'repr' not in self.cache:
            self.cache['repr'] = f'{str(self)}\n\n' + '\n\n'.join((repr(graph) for graph in self.layers))
        return self.cache['repr']

    def clear_cache(self):
        self.cache = dict()
        return

    @property
    def depth(self) -> int:
        return len(self.layers) - 1

    def distance(self, x1: Union[List[int], Data], x2: Union[List[int], Data]) -> np.ndarray:
        """ Calculates the pairwise distances between all points in x1 and x2.

        This DOES NOT do any batching.

        The metric given to Manifold should have the following properties:
            * dist(p1, p2) = 0 if and only if p1 = p2.
            * dist(p1, p2) = dist(p2, p1)

        :param x1: a list of indices, or a 2D matrix of data points
        :param x2: a list of indices, or a 2D matrix of data points
        :return: matrix of pairwise distances.
        """
        x1, x2 = np.asarray(x1), np.asarray(x2)
        # Fetch data if given indices.
        if len(x1.shape) < 2:
            x1 = self.data[x1 if x1.ndim == 1 else np.expand_dims(x1, 0)]
        if len(x2.shape) < 2:
            x2 = self.data[x2 if x2.ndim == 1 else np.expand_dims(x2, 0)]

        return cdist(x1, x2, metric=self.metric)

    def build(self, *criteria) -> 'Manifold':
        """ Rebuilds the Cluster-tree and the Graph-stack. """
        from pyclam.criterion import ClusterCriterion, SelectionCriterion

        cluster_criteria: List[ClusterCriterion] = [
            criterion for criterion in criteria
            if isinstance(criterion, ClusterCriterion)
        ]

        selection_criteria: List[SelectionCriterion] = [
            criterion for criterion in criteria
            if isinstance(criterion, SelectionCriterion)
        ]

        self.layers = [Graph(self.root)]
        self.build_tree(*cluster_criteria)
        self.root.candidates = {self.root: 0.}

        if len(selection_criteria) > 0:
            logging.info(f'building graphs with {len(selection_criteria)} Selection Criteria.')
            self.graphs = [Graph(*select(self.root)).build_edges() for select in selection_criteria]
        else:
            logging.warning('No Selection Criterion was provided. Using leaves for building graph.')
            self.graphs = [Graph(*[cluster for cluster in self.layers[-1].clusters]).build_edges()]

        return self

    def build_tree(self, *criterion) -> 'Manifold':
        """ Builds the Cluster-tree. """
        while True:
            logging.info(f'depth: {self.depth}, {self.layers[-1].cardinality} clusters')
            clusters = self._partition_threaded(criterion)
            if self.layers[-1].cardinality < len(clusters):
                self.layers.append(Graph(*clusters))
            else:
                break
        return self

    def _partition_single(self, criterion) -> List[Cluster]:
        # TODO: Consider removing and only keeping multi-threaded version
        # filter out clusters not previously partitioned
        new_layer: List[Cluster] = [cluster for cluster in self.layers[-1] if cluster.depth < len(self.layers) - 1]

        # get the deepest clusters. These can potentially be partitioned
        partitionable: List[Cluster] = [cluster for cluster in self.layers[-1] if cluster.depth == len(self.layers) - 1]
        [cluster.partition(*criterion) for cluster in partitionable]

        # extend new_layer to contain all the new clusters
        [new_layer.extend(cluster.children) if cluster.children else new_layer.append(cluster) for cluster in partitionable]
        return new_layer

    def _partition_threaded(self, criterion) -> List[Cluster]:
        new_layer: List[Cluster] = [cluster for cluster in self.layers[-1] if cluster.depth < len(self.layers) - 1]
        partitionable: List[Cluster] = [cluster for cluster in self.layers[-1] if cluster.depth == len(self.layers) - 1]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_cluster = [executor.submit(c.partition, *criterion) for c in partitionable]
            [v.result() for v in concurrent.futures.as_completed(future_to_cluster)]

        [new_layer.extend(cluster.children) if cluster.children else new_layer.append(cluster) for cluster in partitionable]
        return new_layer

    def ancestry(self, cluster: Union[str, Cluster]) -> List[Cluster]:
        """ Returns the sequence of clusters that needs to be traversed to reach the requested cluster.

        :param cluster: A cluster or the name of a cluster.
        :return: The lineage of the cluster starting at the root.
        """
        if type(cluster) is Cluster:
            cluster = cluster.name

        if cluster.count('0') > self.depth:
            raise ValueError(f'depth of requested cluster must not be greater than depth of cluster-tree. '
                             f'Got {cluster}, max-depth: {self.depth}')

        lineage: List[Cluster] = [self.root]
        if len(cluster) > 0:
            ancestry_pieces: List[str] = list(cluster.split('0'))
            ancestry = ['']
            for piece in ancestry_pieces[1:]:
                ancestry.append(ancestry[-1] + '0' + piece)

            for ancestor in ancestry[1:]:
                if lineage[-1].children:
                    for child in lineage[-1].children:
                        if child.name == ancestor:
                            lineage.append(child)
                            break
                else:
                    break

        if cluster != lineage[-1].name:
            raise ValueError(f'wanted {cluster} but got {lineage[-1].name}')
        return lineage

    def select(self, name: str) -> Cluster:
        """ Returns the cluster with the given name. """
        return self.ancestry(name)[-1]

    def find_points(self, point: Data, radius: Radius) -> List[Tuple[int, Radius]]:
        """ Returns all indices of points that are within radius of point. """
        candidates: List[int] = [p for c in self.find_clusters(point, radius, len(self.layers))
                                 for p in c.argpoints]
        results: Dict[int, Radius] = dict()
        point = np.expand_dims(point, axis=0)
        for i in range(0, len(candidates), BATCH_SIZE):
            batch = candidates[i:i + BATCH_SIZE]
            distances = self.distance(point, batch)[0]
            results.update({p: d for p, d in zip(batch, distances) if d <= radius})
        return sorted([(p, d) for p, d in results.items()], key=itemgetter(1))

    def find_clusters(self, point: Data, radius: Radius, depth: int) -> Dict['Cluster', Radius]:
        """ Returns all clusters that contain points within radius of point at depth. """
        return {r: d for c in self.layers[0] for r, d in c.tree_search(point, radius, depth).items()}

    def find_knn(self, point: Data, k: int) -> List[Tuple[int, Radius]]:
        """ Finds and returns the k-nearest neighbors of point. """
        radius: Radius = np.float64(np.mean([c.radius for c in self.layers[-1]]))
        radius = np.float64(max(radius, 1e-16))
        results = self.find_points(point, radius)
        while len(results) < k:
            radius *= 2
            results = self.find_points(point, radius)

        return sorted(results, key=itemgetter(1))[:k]

    def dump(self, fp: Union[BinaryIO, IO[bytes]]) -> None:
        pickle.dump({
            'metric': self.metric,
            'root': self.root.json(),
            'graphs': [{cluster.name for cluster in graph.clusters} for graph in self.graphs]
        }, fp, protocol=pickle.HIGHEST_PROTOCOL)
        return

    @staticmethod
    def load(fp: Union[BinaryIO, IO[bytes]], data: Data) -> 'Manifold':
        d = pickle.load(fp)
        manifold = Manifold(data, metric=d['metric'])

        manifold.root = Cluster.from_json(manifold, d['root'])
        manifold.layers = [Graph(manifold.root)]
        while True:
            for cluster in manifold.layers[-1]:
                if cluster.cache['candidates'] is None:
                    cluster.candidates = None
                else:
                    cluster.candidates = {manifold.select(c): d for c, d in cluster.cache['candidates'].items()}

            childless = [cluster for cluster in manifold.layers[-1] if not cluster.children]
            with_child = [cluster for cluster in manifold.layers[-1] if cluster.children]
            if with_child:
                graph = childless + [child for cluster in with_child for child in cluster.children]
                manifold.layers.append(Graph(*graph))
            else:
                break

        manifold.graphs = [Graph(*[manifold.select(cluster) for cluster in graph]).build_edges() for graph in d['graphs']]
        return manifold
