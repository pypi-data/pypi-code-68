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


class ProjectCreate(object):
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
        'account': 'int',
        'created': 'datetime',
        'name': 'str',
        'title': 'str',
        'description': 'str',
        'temporary': 'bool',
        'public': 'bool',
        'key': 'str',
        'main': 'str',
        'container_image': 'str',
        'liveness': 'str',
        'pinned': 'str',
        'theme': 'str',
        'extra_head': 'str',
        'extra_top': 'str',
        'extra_bottom': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account': 'account',
        'created': 'created',
        'name': 'name',
        'title': 'title',
        'description': 'description',
        'temporary': 'temporary',
        'public': 'public',
        'key': 'key',
        'main': 'main',
        'container_image': 'containerImage',
        'liveness': 'liveness',
        'pinned': 'pinned',
        'theme': 'theme',
        'extra_head': 'extraHead',
        'extra_top': 'extraTop',
        'extra_bottom': 'extraBottom'
    }

    def __init__(self, id=None, account=None, created=None, name=None, title=None, description=None, temporary=None, public=None, key=None, main=None, container_image=None, liveness=None, pinned=None, theme=None, extra_head=None, extra_top=None, extra_bottom=None, local_vars_configuration=None):  # noqa: E501
        """ProjectCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._account = None
        self._created = None
        self._name = None
        self._title = None
        self._description = None
        self._temporary = None
        self._public = None
        self._key = None
        self._main = None
        self._container_image = None
        self._liveness = None
        self._pinned = None
        self._theme = None
        self._extra_head = None
        self._extra_top = None
        self._extra_bottom = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account is not None:
            self.account = account
        if created is not None:
            self.created = created
        if name is not None:
            self.name = name
        self.title = title
        self.description = description
        if temporary is not None:
            self.temporary = temporary
        if public is not None:
            self.public = public
        if key is not None:
            self.key = key
        self.main = main
        self.container_image = container_image
        if liveness is not None:
            self.liveness = liveness
        if pinned is not None:
            self.pinned = pinned
        if theme is not None:
            self.theme = theme
        self.extra_head = extra_head
        self.extra_top = extra_top
        self.extra_bottom = extra_bottom

    @property
    def id(self):
        """Gets the id of this ProjectCreate.  # noqa: E501


        :return: The id of this ProjectCreate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectCreate.


        :param id: The id of this ProjectCreate.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def account(self):
        """Gets the account of this ProjectCreate.  # noqa: E501

        Account that the project belongs to.  # noqa: E501

        :return: The account of this ProjectCreate.  # noqa: E501
        :rtype: int
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ProjectCreate.

        Account that the project belongs to.  # noqa: E501

        :param account: The account of this ProjectCreate.  # noqa: E501
        :type account: int
        """

        self._account = account

    @property
    def created(self):
        """Gets the created of this ProjectCreate.  # noqa: E501

        The time the project was created.  # noqa: E501

        :return: The created of this ProjectCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ProjectCreate.

        The time the project was created.  # noqa: E501

        :param created: The created of this ProjectCreate.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def name(self):
        """Gets the name of this ProjectCreate.  # noqa: E501

        Name of the project. Lowercase only and unique for the account. Will be used in URLS e.g. https://hub.stenci.la/awesome-org/great-project.  # noqa: E501

        :return: The name of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectCreate.

        Name of the project. Lowercase only and unique for the account. Will be used in URLS e.g. https://hub.stenci.la/awesome-org/great-project.  # noqa: E501

        :param name: The name of this ProjectCreate.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def title(self):
        """Gets the title of this ProjectCreate.  # noqa: E501

        Title of the project to display in its profile.  # noqa: E501

        :return: The title of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProjectCreate.

        Title of the project to display in its profile.  # noqa: E501

        :param title: The title of this ProjectCreate.  # noqa: E501
        :type title: str
        """
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) > 256):
            raise ValueError("Invalid value for `title`, length must be less than or equal to `256`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this ProjectCreate.  # noqa: E501

        Brief description of the project.  # noqa: E501

        :return: The description of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectCreate.

        Brief description of the project.  # noqa: E501

        :param description: The description of this ProjectCreate.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def temporary(self):
        """Gets the temporary of this ProjectCreate.  # noqa: E501

        Is the project temporary?  # noqa: E501

        :return: The temporary of this ProjectCreate.  # noqa: E501
        :rtype: bool
        """
        return self._temporary

    @temporary.setter
    def temporary(self, temporary):
        """Sets the temporary of this ProjectCreate.

        Is the project temporary?  # noqa: E501

        :param temporary: The temporary of this ProjectCreate.  # noqa: E501
        :type temporary: bool
        """

        self._temporary = temporary

    @property
    def public(self):
        """Gets the public of this ProjectCreate.  # noqa: E501

        Is the project publicly visible?  # noqa: E501

        :return: The public of this ProjectCreate.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ProjectCreate.

        Is the project publicly visible?  # noqa: E501

        :param public: The public of this ProjectCreate.  # noqa: E501
        :type public: bool
        """

        self._public = public

    @property
    def key(self):
        """Gets the key of this ProjectCreate.  # noqa: E501

        A unique, and very difficult to guess, key to access this project if it is not public.  # noqa: E501

        :return: The key of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ProjectCreate.

        A unique, and very difficult to guess, key to access this project if it is not public.  # noqa: E501

        :param key: The key of this ProjectCreate.  # noqa: E501
        :type key: str
        """
        if (self.local_vars_configuration.client_side_validation and
                key is not None and len(key) > 64):
            raise ValueError("Invalid value for `key`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and len(key) < 1):
            raise ValueError("Invalid value for `key`, length must be greater than or equal to `1`")  # noqa: E501

        self._key = key

    @property
    def main(self):
        """Gets the main of this ProjectCreate.  # noqa: E501

        Path of the main file of the project  # noqa: E501

        :return: The main of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this ProjectCreate.

        Path of the main file of the project  # noqa: E501

        :param main: The main of this ProjectCreate.  # noqa: E501
        :type main: str
        """

        self._main = main

    @property
    def container_image(self):
        """Gets the container_image of this ProjectCreate.  # noqa: E501

        The container image to use as the execution environment for this project.  # noqa: E501

        :return: The container_image of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._container_image

    @container_image.setter
    def container_image(self, container_image):
        """Sets the container_image of this ProjectCreate.

        The container image to use as the execution environment for this project.  # noqa: E501

        :param container_image: The container_image of this ProjectCreate.  # noqa: E501
        :type container_image: str
        """

        self._container_image = container_image

    @property
    def liveness(self):
        """Gets the liveness of this ProjectCreate.  # noqa: E501

        Where to serve the content for this project from.  # noqa: E501

        :return: The liveness of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._liveness

    @liveness.setter
    def liveness(self, liveness):
        """Sets the liveness of this ProjectCreate.

        Where to serve the content for this project from.  # noqa: E501

        :param liveness: The liveness of this ProjectCreate.  # noqa: E501
        :type liveness: str
        """
        allowed_values = ["live", "latest", "pinned"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and liveness not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `liveness` ({0}), must be one of {1}"  # noqa: E501
                .format(liveness, allowed_values)
            )

        self._liveness = liveness

    @property
    def pinned(self):
        """Gets the pinned of this ProjectCreate.  # noqa: E501

        If pinned, the snapshot to pin to, when serving content.  # noqa: E501

        :return: The pinned of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this ProjectCreate.

        If pinned, the snapshot to pin to, when serving content.  # noqa: E501

        :param pinned: The pinned of this ProjectCreate.  # noqa: E501
        :type pinned: str
        """

        self._pinned = pinned

    @property
    def theme(self):
        """Gets the theme of this ProjectCreate.  # noqa: E501

        The name of the theme to use as the default when generating content for this project.  # noqa: E501

        :return: The theme of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this ProjectCreate.

        The name of the theme to use as the default when generating content for this project.  # noqa: E501

        :param theme: The theme of this ProjectCreate.  # noqa: E501
        :type theme: str
        """
        allowed_values = ["bootstrap", "elife", "f1000", "galleria", "giga", "latex", "nature", "plos", "rpng", "skeleton", "stencila", "tufte", "wilmore"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and theme not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `theme` ({0}), must be one of {1}"  # noqa: E501
                .format(theme, allowed_values)
            )

        self._theme = theme

    @property
    def extra_head(self):
        """Gets the extra_head of this ProjectCreate.  # noqa: E501

        Content to inject into the <head> element of HTML served for this project.  # noqa: E501

        :return: The extra_head of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._extra_head

    @extra_head.setter
    def extra_head(self, extra_head):
        """Sets the extra_head of this ProjectCreate.

        Content to inject into the <head> element of HTML served for this project.  # noqa: E501

        :param extra_head: The extra_head of this ProjectCreate.  # noqa: E501
        :type extra_head: str
        """

        self._extra_head = extra_head

    @property
    def extra_top(self):
        """Gets the extra_top of this ProjectCreate.  # noqa: E501

        Content to inject at the top of the <body> element of HTML served for this project.  # noqa: E501

        :return: The extra_top of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._extra_top

    @extra_top.setter
    def extra_top(self, extra_top):
        """Sets the extra_top of this ProjectCreate.

        Content to inject at the top of the <body> element of HTML served for this project.  # noqa: E501

        :param extra_top: The extra_top of this ProjectCreate.  # noqa: E501
        :type extra_top: str
        """

        self._extra_top = extra_top

    @property
    def extra_bottom(self):
        """Gets the extra_bottom of this ProjectCreate.  # noqa: E501

        Content to inject at the bottom of the <body> element of HTML served for this project.  # noqa: E501

        :return: The extra_bottom of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._extra_bottom

    @extra_bottom.setter
    def extra_bottom(self, extra_bottom):
        """Sets the extra_bottom of this ProjectCreate.

        Content to inject at the bottom of the <body> element of HTML served for this project.  # noqa: E501

        :param extra_bottom: The extra_bottom of this ProjectCreate.  # noqa: E501
        :type extra_bottom: str
        """

        self._extra_bottom = extra_bottom

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
        if not isinstance(other, ProjectCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectCreate):
            return True

        return self.to_dict() != other.to_dict()
