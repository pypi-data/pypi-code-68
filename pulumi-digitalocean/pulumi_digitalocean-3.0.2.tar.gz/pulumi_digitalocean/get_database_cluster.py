# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs

__all__ = [
    'GetDatabaseClusterResult',
    'AwaitableGetDatabaseClusterResult',
    'get_database_cluster',
]

@pulumi.output_type
class GetDatabaseClusterResult:
    """
    A collection of values returned by getDatabaseCluster.
    """
    def __init__(__self__, database=None, engine=None, host=None, id=None, maintenance_windows=None, name=None, node_count=None, password=None, port=None, private_host=None, private_network_uuid=None, private_uri=None, region=None, size=None, tags=None, uri=None, urn=None, user=None, version=None):
        if database and not isinstance(database, str):
            raise TypeError("Expected argument 'database' to be a str")
        pulumi.set(__self__, "database", database)
        if engine and not isinstance(engine, str):
            raise TypeError("Expected argument 'engine' to be a str")
        pulumi.set(__self__, "engine", engine)
        if host and not isinstance(host, str):
            raise TypeError("Expected argument 'host' to be a str")
        pulumi.set(__self__, "host", host)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if maintenance_windows and not isinstance(maintenance_windows, list):
            raise TypeError("Expected argument 'maintenance_windows' to be a list")
        pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_count and not isinstance(node_count, int):
            raise TypeError("Expected argument 'node_count' to be a int")
        pulumi.set(__self__, "node_count", node_count)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if private_host and not isinstance(private_host, str):
            raise TypeError("Expected argument 'private_host' to be a str")
        pulumi.set(__self__, "private_host", private_host)
        if private_network_uuid and not isinstance(private_network_uuid, str):
            raise TypeError("Expected argument 'private_network_uuid' to be a str")
        pulumi.set(__self__, "private_network_uuid", private_network_uuid)
        if private_uri and not isinstance(private_uri, str):
            raise TypeError("Expected argument 'private_uri' to be a str")
        pulumi.set(__self__, "private_uri", private_uri)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if size and not isinstance(size, str):
            raise TypeError("Expected argument 'size' to be a str")
        pulumi.set(__self__, "size", size)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if uri and not isinstance(uri, str):
            raise TypeError("Expected argument 'uri' to be a str")
        pulumi.set(__self__, "uri", uri)
        if urn and not isinstance(urn, str):
            raise TypeError("Expected argument 'urn' to be a str")
        pulumi.set(__self__, "urn", urn)
        if user and not isinstance(user, str):
            raise TypeError("Expected argument 'user' to be a str")
        pulumi.set(__self__, "user", user)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def database(self) -> str:
        """
        Name of the cluster's default database.
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter
    def engine(self) -> str:
        """
        Database engine used by the cluster (ex. `pg` for PostreSQL).
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        Database cluster's hostname.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetDatabaseClusterMaintenanceWindowResult']:
        """
        Defines when the automatic maintenance should be performed for the database cluster.
        """
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> int:
        """
        Number of nodes that will be included in the cluster.
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        Password for the cluster's default user.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        Network port that the database cluster is listening on.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="privateHost")
    def private_host(self) -> str:
        """
        Same as `host`, but only accessible from resources within the account and in the same region.
        """
        return pulumi.get(self, "private_host")

    @property
    @pulumi.getter(name="privateNetworkUuid")
    def private_network_uuid(self) -> str:
        """
        The ID of the VPC where the database cluster is located.
        """
        return pulumi.get(self, "private_network_uuid")

    @property
    @pulumi.getter(name="privateUri")
    def private_uri(self) -> str:
        """
        Same as `uri`, but only accessible from resources within the account and in the same region.
        """
        return pulumi.get(self, "private_uri")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        DigitalOcean region where the cluster will reside.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> str:
        """
        Database droplet size associated with the cluster (ex. `db-s-1vcpu-1gb`).
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def uri(self) -> str:
        """
        The full URI for connecting to the database cluster.
        """
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter
    def urn(self) -> str:
        """
        The uniform resource name of the database cluster.
        """
        return pulumi.get(self, "urn")

    @property
    @pulumi.getter
    def user(self) -> str:
        """
        Username for the cluster's default user.
        """
        return pulumi.get(self, "user")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Engine version used by the cluster (ex. `11` for PostgreSQL 11).
        """
        return pulumi.get(self, "version")


class AwaitableGetDatabaseClusterResult(GetDatabaseClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseClusterResult(
            database=self.database,
            engine=self.engine,
            host=self.host,
            id=self.id,
            maintenance_windows=self.maintenance_windows,
            name=self.name,
            node_count=self.node_count,
            password=self.password,
            port=self.port,
            private_host=self.private_host,
            private_network_uuid=self.private_network_uuid,
            private_uri=self.private_uri,
            region=self.region,
            size=self.size,
            tags=self.tags,
            uri=self.uri,
            urn=self.urn,
            user=self.user,
            version=self.version)


def get_database_cluster(name: Optional[str] = None,
                         tags: Optional[Sequence[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseClusterResult:
    """
    Provides information on a DigitalOcean database cluster resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_database_cluster(name="example-cluster")
    pulumi.export("databaseOutput", example.uri)
    ```


    :param str name: The name of the database cluster.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getDatabaseCluster:getDatabaseCluster', __args__, opts=opts, typ=GetDatabaseClusterResult).value

    return AwaitableGetDatabaseClusterResult(
        database=__ret__.database,
        engine=__ret__.engine,
        host=__ret__.host,
        id=__ret__.id,
        maintenance_windows=__ret__.maintenance_windows,
        name=__ret__.name,
        node_count=__ret__.node_count,
        password=__ret__.password,
        port=__ret__.port,
        private_host=__ret__.private_host,
        private_network_uuid=__ret__.private_network_uuid,
        private_uri=__ret__.private_uri,
        region=__ret__.region,
        size=__ret__.size,
        tags=__ret__.tags,
        uri=__ret__.uri,
        urn=__ret__.urn,
        user=__ret__.user,
        version=__ret__.version)
