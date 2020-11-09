"""Projects are specific repository or sources to download from a remote location.

In its most basic form a project only has a 'name:'. This would make `Dfetch`
retrieve the mymodule project from the only remote listed (`mycompany-git-modules`)
and place it in a folder ``mymodule`` in the same folder as the manifest.

.. note:: A project name *must* be unique.

.. code-block:: yaml

    manifest:
        version: 0.0

        remotes:
        - name: mycompany-git-modules
          url-base: http://git.mycompany.local/mycompany/

        projects:
         - name: mymodule

Destination and revision
########################
Since we want more control on what project is retrieved and where it is placed
the ``revision:``, ``branch:`` and ``dst:`` attributes can help. Below manifest
will download tag ``v1.13`` of the mymodule and place it in the path listed by ``dst:``.

.. code-block:: yaml

    manifest:
        version: 0.0

        remotes:
        - name: mycompany-git-modules
          url-base: http://git.mycompany.local/mycompany/

        projects:
         - name: mymodule
           branch: v1.13
           dst: external/mymodule

We can also list multiple projects.

.. code-block:: yaml

    manifest:
        version: 0.0

        remotes:
        - name: mycompany-git-modules
          url-base: http://git.mycompany.local/mycompany/

        projects:
         - name: mymodule
           branch: v1.13
           dst: external/mymodule

         - name: myothermodule
           revision: bea84ba8f
           dst: external/myothermodule

"""
import copy
from typing import Dict, Optional, Union

from typing_extensions import TypedDict

from dfetch.manifest.remote import Remote

ProjectEntryDict = TypedDict(
    "ProjectEntryDict",
    {
        "name": str,
        "revision": str,
        "remote": str,
        "src": str,
        "dst": str,
        "url": str,
        "patch": str,
        "repo": str,
        "branch": str,
        "repo-path": str,
        "default_remote": Optional[Remote],
    },
    total=False,
)


class ProjectEntry:  # pylint: disable=too-many-instance-attributes
    """A single Project entry in the manifest file."""

    def __init__(self, kwargs: ProjectEntryDict) -> None:
        """Create the project entry."""
        self._name: str = kwargs["name"]
        self._revision: str = kwargs.get("revision", "")

        self._remote: str = kwargs.get("remote", "")
        self._remote_obj: Optional[Remote] = kwargs.get("default_remote", None)
        self._src: str = kwargs.get("src", "")  # noqa
        self._dst: str = kwargs.get("dst", ".")
        self._url: str = kwargs.get("url", "")
        self._patch: str = kwargs.get("patch", "")  # noqa
        self._repo_path: str = kwargs.get("repo-path", "")
        self._branch: str = kwargs.get("branch", "")

    @classmethod
    def from_yaml(
        cls,
        yamldata: Union[Dict[str, str], ProjectEntryDict],
        default_remote: Optional[Remote] = None,
    ) -> "ProjectEntry":
        """Create a Project Entry from yaml data.

        Returns:
            ProjectEntry:  An immutable ProjectEntry
        """
        kwargs: ProjectEntryDict = {}
        for key in ProjectEntryDict.__annotations__.keys():
            try:
                kwargs[str(key)] = yamldata[key]  # type: ignore
            except KeyError:
                pass
        kwargs["default_remote"] = default_remote
        return cls(kwargs)

    @classmethod
    def copy(
        cls, other: "ProjectEntry", default_remote: Optional[Remote] = None
    ) -> "ProjectEntry":
        """Create a Project Entry copy from a Project Entry."""
        # pylint: disable=protected-access
        the_copy = copy.copy(other)
        if not the_copy._remote_obj:
            the_copy._remote_obj = default_remote
        return the_copy

    def set_remote(self, remote: Remote) -> None:
        """Set the remote."""
        self._remote_obj = remote
        self._remote = remote.name
        if self._url.startswith(remote.url):
            self._url = self._url.replace(remote.url, "").strip("/")

    @property
    def remote_url(self) -> str:
        """Get the remote url of the project."""
        if self._url:
            return self._url
        if self._remote_obj:
            return "/".join(
                self._remote_obj.url.strip("/").split("/") + self._repo_path.split("/")
            )
        return ""

    @property
    def remote(self) -> str:
        """Get the url."""
        return self._remote

    @property
    def name(self) -> str:
        """Get the name of the project."""
        return self._name

    @property
    def destination(self) -> str:
        """Get the local path the project should be copied to."""
        return self._dst

    @property
    def branch(self) -> str:
        """Get the branch that should be fetched."""
        return self._branch

    @property
    def revision(self) -> str:
        """Get the revision that should be fetched."""
        return self._revision

    def __repr__(self) -> str:
        """Get a string representation of this project entry."""
        version = (
            f"{self.branch} {self.revision}".strip()
            if (self.branch or self.revision)
            else "latest"
        )
        return f"{self.name:20s} {version} {self.remote_url} {self.destination}"

    def as_yaml(self) -> Dict[str, str]:
        """Get this project as yaml dictionary."""
        yamldata = {
            "name": self._name,
            "revision": self._revision,
            "remote": self._remote,
            "src": self._src,
            "dst": self._dst,
            "url": self._url,
            "patch": self._patch,
            "branch": self._branch,
        }

        return {k: v for k, v in yamldata.items() if v}
