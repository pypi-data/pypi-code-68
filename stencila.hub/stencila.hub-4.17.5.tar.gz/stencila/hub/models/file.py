# coding: utf-8

"""
    Stencila Hub API

    ## Authentication  Many endpoints in the Stencila Hub API require an authentication token. These tokens carry many privileges, so be sure to keep them secure. Do not place your tokens in publicly accessible areas such as client-side code. The API is only served over HTTPS to avoid exposing tokens and other data on the network.  To obtain a token, [`POST /api/tokens`](#operations-tokens-tokens_create) with either a `username` and `password` pair, or an [OpenID Connect](https://openid.net/connect/) token. Then use the token in the `Authorization` header of subsequent requests with the prefix `Token` e.g.      curl -H \"Authorization: Token 48866b1e38a2e9db0baada2140b2327937f4a3636dd5f2dfd8c212341c88d34\" https://hub.stenci.la/api/projects/  Alternatively, you can use `Basic` authentication with the token used as the username and no password. This can be more convenient when using command line tools such as [cURL](https://curl.haxx.se/) e.g.      curl -u 48866b1e38a2e9db0baada2140b2327937f4a3636dd5f2dfd8c212341c88d34: https://hub.stenci.la/api/projects/  Or, the less ubiquitous, but more accessible [httpie](https://httpie.org/):      http --auth 48866b1e38a2e9db0baada2140b2327937f4a3636dd5f2dfd8c212341c88d34: https://hub.stenci.la/api/projects/  In both examples above, the trailing colon is not required but avoids being asked for a password.  ## Versioning  The Stencila Hub is released using semantic versioning. The current version is available from the [`GET /api/status`](/api/status) endpoint. Please see the [Github release page](https://github.com/stencila/hub/releases) and the [changelog](https://github.com/stencila/hub/blob/master/CHANGELOG.md) for details on each release. We currently do not provide versioning of the API but plan to do so soon (probably by using a `Accept: application/vnd.stencila.hub+json;version=1.0` request header). If you are using, or interested in using, the API please contact us and we may be able to expedite this.   # noqa: E501

    The version of the OpenAPI document: v1
    Contact: hello@stenci.la
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from stencila.hub.configuration import Configuration


class File(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'path': 'str',
        'current': 'bool',
        'created': 'datetime',
        'updated': 'datetime',
        'modified': 'datetime',
        'size': 'int',
        'mimetype': 'str',
        'encoding': 'str',
        'fingerprint': 'str',
        'job': 'int',
        'source': 'int',
        'snapshot': 'str',
        'upstreams': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'path': 'path',
        'current': 'current',
        'created': 'created',
        'updated': 'updated',
        'modified': 'modified',
        'size': 'size',
        'mimetype': 'mimetype',
        'encoding': 'encoding',
        'fingerprint': 'fingerprint',
        'job': 'job',
        'source': 'source',
        'snapshot': 'snapshot',
        'upstreams': 'upstreams'
    }

    def __init__(self, id=None, path=None, current=None, created=None, updated=None, modified=None, size=None, mimetype=None, encoding=None, fingerprint=None, job=None, source=None, snapshot=None, upstreams=None, local_vars_configuration=None):  # noqa: E501
        """File - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._path = None
        self._current = None
        self._created = None
        self._updated = None
        self._modified = None
        self._size = None
        self._mimetype = None
        self._encoding = None
        self._fingerprint = None
        self._job = None
        self._source = None
        self._snapshot = None
        self._upstreams = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.path = path
        if current is not None:
            self.current = current
        if created is not None:
            self.created = created
        self.updated = updated
        self.modified = modified
        self.size = size
        self.mimetype = mimetype
        self.encoding = encoding
        self.fingerprint = fingerprint
        self.job = job
        self.source = source
        self.snapshot = snapshot
        self.upstreams = upstreams

    @property
    def id(self):
        """Gets the id of this File.  # noqa: E501


        :return: The id of this File.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this File.


        :param id: The id of this File.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def path(self):
        """Gets the path of this File.  # noqa: E501

        The path of the file within the project.  # noqa: E501

        :return: The path of this File.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this File.

        The path of the file within the project.  # noqa: E501

        :param path: The path of this File.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) < 1):
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `1`")  # noqa: E501

        self._path = path

    @property
    def current(self):
        """Gets the current of this File.  # noqa: E501

        Is the file currently in the project? Used to retain a history for file paths within a project.  # noqa: E501

        :return: The current of this File.  # noqa: E501
        :rtype: bool
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this File.

        Is the file currently in the project? Used to retain a history for file paths within a project.  # noqa: E501

        :param current: The current of this File.  # noqa: E501
        :type current: bool
        """

        self._current = current

    @property
    def created(self):
        """Gets the created of this File.  # noqa: E501

        The time the file info was created.  # noqa: E501

        :return: The created of this File.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this File.

        The time the file info was created.  # noqa: E501

        :param created: The created of this File.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this File.  # noqa: E501

        The time the file info was updated. This field will have the last time this row was altered (i.e. changed from current, to not).  # noqa: E501

        :return: The updated of this File.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this File.

        The time the file info was updated. This field will have the last time this row was altered (i.e. changed from current, to not).  # noqa: E501

        :param updated: The updated of this File.  # noqa: E501
        :type updated: datetime
        """

        self._updated = updated

    @property
    def modified(self):
        """Gets the modified of this File.  # noqa: E501

        The file modification time.  # noqa: E501

        :return: The modified of this File.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this File.

        The file modification time.  # noqa: E501

        :param modified: The modified of this File.  # noqa: E501
        :type modified: datetime
        """

        self._modified = modified

    @property
    def size(self):
        """Gets the size of this File.  # noqa: E501

        The size of the file in bytes  # noqa: E501

        :return: The size of this File.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this File.

        The size of the file in bytes  # noqa: E501

        :param size: The size of this File.  # noqa: E501
        :type size: int
        """

        self._size = size

    @property
    def mimetype(self):
        """Gets the mimetype of this File.  # noqa: E501

        The mimetype of the file.  # noqa: E501

        :return: The mimetype of this File.  # noqa: E501
        :rtype: str
        """
        return self._mimetype

    @mimetype.setter
    def mimetype(self, mimetype):
        """Sets the mimetype of this File.

        The mimetype of the file.  # noqa: E501

        :param mimetype: The mimetype of this File.  # noqa: E501
        :type mimetype: str
        """
        if (self.local_vars_configuration.client_side_validation and
                mimetype is not None and len(mimetype) > 512):
            raise ValueError("Invalid value for `mimetype`, length must be less than or equal to `512`")  # noqa: E501

        self._mimetype = mimetype

    @property
    def encoding(self):
        """Gets the encoding of this File.  # noqa: E501

        The encoding of the file e.g. gzip  # noqa: E501

        :return: The encoding of this File.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this File.

        The encoding of the file e.g. gzip  # noqa: E501

        :param encoding: The encoding of this File.  # noqa: E501
        :type encoding: str
        """
        if (self.local_vars_configuration.client_side_validation and
                encoding is not None and len(encoding) > 512):
            raise ValueError("Invalid value for `encoding`, length must be less than or equal to `512`")  # noqa: E501

        self._encoding = encoding

    @property
    def fingerprint(self):
        """Gets the fingerprint of this File.  # noqa: E501

        The fingerprint of the file  # noqa: E501

        :return: The fingerprint of this File.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this File.

        The fingerprint of the file  # noqa: E501

        :param fingerprint: The fingerprint of this File.  # noqa: E501
        :type fingerprint: str
        """
        if (self.local_vars_configuration.client_side_validation and
                fingerprint is not None and len(fingerprint) > 128):
            raise ValueError("Invalid value for `fingerprint`, length must be less than or equal to `128`")  # noqa: E501

        self._fingerprint = fingerprint

    @property
    def job(self):
        """Gets the job of this File.  # noqa: E501

        The job that created the file e.g. a source pull or file conversion.  # noqa: E501

        :return: The job of this File.  # noqa: E501
        :rtype: int
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this File.

        The job that created the file e.g. a source pull or file conversion.  # noqa: E501

        :param job: The job of this File.  # noqa: E501
        :type job: int
        """

        self._job = job

    @property
    def source(self):
        """Gets the source of this File.  # noqa: E501

        The source from which the file came (if any). If the source is removed from the project, so will this file.  # noqa: E501

        :return: The source of this File.  # noqa: E501
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this File.

        The source from which the file came (if any). If the source is removed from the project, so will this file.  # noqa: E501

        :param source: The source of this File.  # noqa: E501
        :type source: int
        """

        self._source = source

    @property
    def snapshot(self):
        """Gets the snapshot of this File.  # noqa: E501

        The snapshot that the file belongs. If the snapshot is deleted so will the files.  # noqa: E501

        :return: The snapshot of this File.  # noqa: E501
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this File.

        The snapshot that the file belongs. If the snapshot is deleted so will the files.  # noqa: E501

        :param snapshot: The snapshot of this File.  # noqa: E501
        :type snapshot: str
        """

        self._snapshot = snapshot

    @property
    def upstreams(self):
        """Gets the upstreams of this File.  # noqa: E501

        The files that this file was derived from (if any).  # noqa: E501

        :return: The upstreams of this File.  # noqa: E501
        :rtype: list[int]
        """
        return self._upstreams

    @upstreams.setter
    def upstreams(self, upstreams):
        """Sets the upstreams of this File.

        The files that this file was derived from (if any).  # noqa: E501

        :param upstreams: The upstreams of this File.  # noqa: E501
        :type upstreams: list[int]
        """
        if self.local_vars_configuration.client_side_validation and upstreams is None:  # noqa: E501
            raise ValueError("Invalid value for `upstreams`, must not be `None`")  # noqa: E501

        self._upstreams = upstreams

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, File):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, File):
            return True

        return self.to_dict() != other.to_dict()
