# coding: utf-8

"""
    Ketra Lighting API

    Control your Ketra lights  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aioketraapi.configuration import Configuration


class LampState(object):
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
        'brightness': 'float',
        'master_brightness': 'float',
        'net_brightness': 'float',
        'dim_curve_active': 'bool',
        'dim_curve': 'str',
        'power_on': 'bool',
        'vibrancy': 'float',
        'cct': 'int',
        'x_chromaticity': 'float',
        'y_chromaticity': 'float',
        'transition_time': 'int',
        'updated_at': 'str',
        'transition_complete': 'bool',
        'active_shows': 'list[int]',
        'start_state': 'LampStateParameters'
    }

    attribute_map = {
        'brightness': 'Brightness',
        'master_brightness': 'MasterBrightness',
        'net_brightness': 'NetBrightness',
        'dim_curve_active': 'DimCurveActive',
        'dim_curve': 'DimCurve',
        'power_on': 'PowerOn',
        'vibrancy': 'Vibrancy',
        'cct': 'CCT',
        'x_chromaticity': 'xChromaticity',
        'y_chromaticity': 'yChromaticity',
        'transition_time': 'TransitionTime',
        'updated_at': 'UpdatedAt',
        'transition_complete': 'TransitionComplete',
        'active_shows': 'ActiveShows',
        'start_state': 'StartState'
    }

    def __init__(self, brightness=None, master_brightness=None, net_brightness=None, dim_curve_active=None, dim_curve=None, power_on=None, vibrancy=None, cct=None, x_chromaticity=None, y_chromaticity=None, transition_time=None, updated_at=None, transition_complete=None, active_shows=None, start_state=None, local_vars_configuration=None):  # noqa: E501
        """LampState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._brightness = None
        self._master_brightness = None
        self._net_brightness = None
        self._dim_curve_active = None
        self._dim_curve = None
        self._power_on = None
        self._vibrancy = None
        self._cct = None
        self._x_chromaticity = None
        self._y_chromaticity = None
        self._transition_time = None
        self._updated_at = None
        self._transition_complete = None
        self._active_shows = None
        self._start_state = None
        self.discriminator = None

        if brightness is not None:
            self.brightness = brightness
        if master_brightness is not None:
            self.master_brightness = master_brightness
        if net_brightness is not None:
            self.net_brightness = net_brightness
        if dim_curve_active is not None:
            self.dim_curve_active = dim_curve_active
        if dim_curve is not None:
            self.dim_curve = dim_curve
        if power_on is not None:
            self.power_on = power_on
        if vibrancy is not None:
            self.vibrancy = vibrancy
        if cct is not None:
            self.cct = cct
        if x_chromaticity is not None:
            self.x_chromaticity = x_chromaticity
        if y_chromaticity is not None:
            self.y_chromaticity = y_chromaticity
        if transition_time is not None:
            self.transition_time = transition_time
        if updated_at is not None:
            self.updated_at = updated_at
        if transition_complete is not None:
            self.transition_complete = transition_complete
        if active_shows is not None:
            self.active_shows = active_shows
        if start_state is not None:
            self.start_state = start_state

    @property
    def brightness(self):
        """Gets the brightness of this LampState.  # noqa: E501

        the brightness of the light  # noqa: E501

        :return: The brightness of this LampState.  # noqa: E501
        :rtype: float
        """
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        """Sets the brightness of this LampState.

        the brightness of the light  # noqa: E501

        :param brightness: The brightness of this LampState.  # noqa: E501
        :type brightness: float
        """
        if (self.local_vars_configuration.client_side_validation and
                brightness is not None and brightness > 1):  # noqa: E501
            raise ValueError("Invalid value for `brightness`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                brightness is not None and brightness < 0):  # noqa: E501
            raise ValueError("Invalid value for `brightness`, must be a value greater than or equal to `0`")  # noqa: E501

        self._brightness = brightness

    @property
    def master_brightness(self):
        """Gets the master_brightness of this LampState.  # noqa: E501

        the master brightness value of the light.  This parameter is new for API schema 4 and provides an independent brightness channel that can be varied while 'Brightness' remains constant.  # noqa: E501

        :return: The master_brightness of this LampState.  # noqa: E501
        :rtype: float
        """
        return self._master_brightness

    @master_brightness.setter
    def master_brightness(self, master_brightness):
        """Sets the master_brightness of this LampState.

        the master brightness value of the light.  This parameter is new for API schema 4 and provides an independent brightness channel that can be varied while 'Brightness' remains constant.  # noqa: E501

        :param master_brightness: The master_brightness of this LampState.  # noqa: E501
        :type master_brightness: float
        """
        if (self.local_vars_configuration.client_side_validation and
                master_brightness is not None and master_brightness > 1):  # noqa: E501
            raise ValueError("Invalid value for `master_brightness`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                master_brightness is not None and master_brightness < 0):  # noqa: E501
            raise ValueError("Invalid value for `master_brightness`, must be a value greater than or equal to `0`")  # noqa: E501

        self._master_brightness = master_brightness

    @property
    def net_brightness(self):
        """Gets the net_brightness of this LampState.  # noqa: E501

        The overall brightness of the light (Brightness * MasterBrightness). This parameter is new for API schema 4 and is ignored for a PUT or POST operation.  # noqa: E501

        :return: The net_brightness of this LampState.  # noqa: E501
        :rtype: float
        """
        return self._net_brightness

    @net_brightness.setter
    def net_brightness(self, net_brightness):
        """Sets the net_brightness of this LampState.

        The overall brightness of the light (Brightness * MasterBrightness). This parameter is new for API schema 4 and is ignored for a PUT or POST operation.  # noqa: E501

        :param net_brightness: The net_brightness of this LampState.  # noqa: E501
        :type net_brightness: float
        """
        if (self.local_vars_configuration.client_side_validation and
                net_brightness is not None and net_brightness > 1):  # noqa: E501
            raise ValueError("Invalid value for `net_brightness`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                net_brightness is not None and net_brightness < 0):  # noqa: E501
            raise ValueError("Invalid value for `net_brightness`, must be a value greater than or equal to `0`")  # noqa: E501

        self._net_brightness = net_brightness

    @property
    def dim_curve_active(self):
        """Gets the dim_curve_active of this LampState.  # noqa: E501

        returns true if a dimming curve is currently active on the lamp group.  New for API schema 4.  # noqa: E501

        :return: The dim_curve_active of this LampState.  # noqa: E501
        :rtype: bool
        """
        return self._dim_curve_active

    @dim_curve_active.setter
    def dim_curve_active(self, dim_curve_active):
        """Sets the dim_curve_active of this LampState.

        returns true if a dimming curve is currently active on the lamp group.  New for API schema 4.  # noqa: E501

        :param dim_curve_active: The dim_curve_active of this LampState.  # noqa: E501
        :type dim_curve_active: bool
        """

        self._dim_curve_active = dim_curve_active

    @property
    def dim_curve(self):
        """Gets the dim_curve of this LampState.  # noqa: E501

        if DimCurveActive is true, indicates which dimming curve is active.  New for API schema 4.  # noqa: E501

        :return: The dim_curve of this LampState.  # noqa: E501
        :rtype: str
        """
        return self._dim_curve

    @dim_curve.setter
    def dim_curve(self, dim_curve):
        """Sets the dim_curve of this LampState.

        if DimCurveActive is true, indicates which dimming curve is active.  New for API schema 4.  # noqa: E501

        :param dim_curve: The dim_curve of this LampState.  # noqa: E501
        :type dim_curve: str
        """
        allowed_values = ["Xenon", "GE Ultra Soft White", "Philips EcoVantage A19", "Philips Halogen PAR38", "none"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dim_curve not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dim_curve` ({0}), must be one of {1}"  # noqa: E501
                .format(dim_curve, allowed_values)
            )

        self._dim_curve = dim_curve

    @property
    def power_on(self):
        """Gets the power_on of this LampState.  # noqa: E501

        true if the light is on, false if the light is off  # noqa: E501

        :return: The power_on of this LampState.  # noqa: E501
        :rtype: bool
        """
        return self._power_on

    @power_on.setter
    def power_on(self, power_on):
        """Sets the power_on of this LampState.

        true if the light is on, false if the light is off  # noqa: E501

        :param power_on: The power_on of this LampState.  # noqa: E501
        :type power_on: bool
        """

        self._power_on = power_on

    @property
    def vibrancy(self):
        """Gets the vibrancy of this LampState.  # noqa: E501

        the ratio of RGB to phosphor-converted white LED content.  A value of 0 indicates to use as little RGB as possible.  A value of 1 indicates to use as much RGB as possible  # noqa: E501

        :return: The vibrancy of this LampState.  # noqa: E501
        :rtype: float
        """
        return self._vibrancy

    @vibrancy.setter
    def vibrancy(self, vibrancy):
        """Sets the vibrancy of this LampState.

        the ratio of RGB to phosphor-converted white LED content.  A value of 0 indicates to use as little RGB as possible.  A value of 1 indicates to use as much RGB as possible  # noqa: E501

        :param vibrancy: The vibrancy of this LampState.  # noqa: E501
        :type vibrancy: float
        """
        if (self.local_vars_configuration.client_side_validation and
                vibrancy is not None and vibrancy > 1):  # noqa: E501
            raise ValueError("Invalid value for `vibrancy`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                vibrancy is not None and vibrancy < 0):  # noqa: E501
            raise ValueError("Invalid value for `vibrancy`, must be a value greater than or equal to `0`")  # noqa: E501

        self._vibrancy = vibrancy

    @property
    def cct(self):
        """Gets the cct of this LampState.  # noqa: E501

        the correlated color temperature of the light.  If cct is provided and within the valid range, it will be used instead of x and y chromaticity  # noqa: E501

        :return: The cct of this LampState.  # noqa: E501
        :rtype: int
        """
        return self._cct

    @cct.setter
    def cct(self, cct):
        """Sets the cct of this LampState.

        the correlated color temperature of the light.  If cct is provided and within the valid range, it will be used instead of x and y chromaticity  # noqa: E501

        :param cct: The cct of this LampState.  # noqa: E501
        :type cct: int
        """
        if (self.local_vars_configuration.client_side_validation and
                cct is not None and cct > 25000):  # noqa: E501
            raise ValueError("Invalid value for `cct`, must be a value less than or equal to `25000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cct is not None and cct < 0):  # noqa: E501
            raise ValueError("Invalid value for `cct`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cct = cct

    @property
    def x_chromaticity(self):
        """Gets the x_chromaticity of this LampState.  # noqa: E501

        the x chromaticity of the light.  This parameter will be ignored if a valid cct value is provided on a put/post operation.  A get operation will return a valid value always  # noqa: E501

        :return: The x_chromaticity of this LampState.  # noqa: E501
        :rtype: float
        """
        return self._x_chromaticity

    @x_chromaticity.setter
    def x_chromaticity(self, x_chromaticity):
        """Sets the x_chromaticity of this LampState.

        the x chromaticity of the light.  This parameter will be ignored if a valid cct value is provided on a put/post operation.  A get operation will return a valid value always  # noqa: E501

        :param x_chromaticity: The x_chromaticity of this LampState.  # noqa: E501
        :type x_chromaticity: float
        """
        if (self.local_vars_configuration.client_side_validation and
                x_chromaticity is not None and x_chromaticity > 1):  # noqa: E501
            raise ValueError("Invalid value for `x_chromaticity`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                x_chromaticity is not None and x_chromaticity < 0):  # noqa: E501
            raise ValueError("Invalid value for `x_chromaticity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._x_chromaticity = x_chromaticity

    @property
    def y_chromaticity(self):
        """Gets the y_chromaticity of this LampState.  # noqa: E501

        the y chromaticity of the light.  This parameter will be ignored if a valid cct value is provided on a put/post operation.  A get operation will return a valid value always  # noqa: E501

        :return: The y_chromaticity of this LampState.  # noqa: E501
        :rtype: float
        """
        return self._y_chromaticity

    @y_chromaticity.setter
    def y_chromaticity(self, y_chromaticity):
        """Sets the y_chromaticity of this LampState.

        the y chromaticity of the light.  This parameter will be ignored if a valid cct value is provided on a put/post operation.  A get operation will return a valid value always  # noqa: E501

        :param y_chromaticity: The y_chromaticity of this LampState.  # noqa: E501
        :type y_chromaticity: float
        """
        if (self.local_vars_configuration.client_side_validation and
                y_chromaticity is not None and y_chromaticity > 1):  # noqa: E501
            raise ValueError("Invalid value for `y_chromaticity`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                y_chromaticity is not None and y_chromaticity < 0):  # noqa: E501
            raise ValueError("Invalid value for `y_chromaticity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._y_chromaticity = y_chromaticity

    @property
    def transition_time(self):
        """Gets the transition_time of this LampState.  # noqa: E501

        transition time, in ms.  (Required)  # noqa: E501

        :return: The transition_time of this LampState.  # noqa: E501
        :rtype: int
        """
        return self._transition_time

    @transition_time.setter
    def transition_time(self, transition_time):
        """Sets the transition_time of this LampState.

        transition time, in ms.  (Required)  # noqa: E501

        :param transition_time: The transition_time of this LampState.  # noqa: E501
        :type transition_time: int
        """
        if (self.local_vars_configuration.client_side_validation and
                transition_time is not None and transition_time > 6553500):  # noqa: E501
            raise ValueError("Invalid value for `transition_time`, must be a value less than or equal to `6553500`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transition_time is not None and transition_time < 0):  # noqa: E501
            raise ValueError("Invalid value for `transition_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._transition_time = transition_time

    @property
    def updated_at(self):
        """Gets the updated_at of this LampState.  # noqa: E501

        the time at which the group was last updated.  New for API schema 4.  # noqa: E501

        :return: The updated_at of this LampState.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LampState.

        the time at which the group was last updated.  New for API schema 4.  # noqa: E501

        :param updated_at: The updated_at of this LampState.  # noqa: E501
        :type updated_at: str
        """

        self._updated_at = updated_at

    @property
    def transition_complete(self):
        """Gets the transition_complete of this LampState.  # noqa: E501

        returns true if the lamp is finished transitioning to the last updated color.  New for API schema 4.  # noqa: E501

        :return: The transition_complete of this LampState.  # noqa: E501
        :rtype: bool
        """
        return self._transition_complete

    @transition_complete.setter
    def transition_complete(self, transition_complete):
        """Sets the transition_complete of this LampState.

        returns true if the lamp is finished transitioning to the last updated color.  New for API schema 4.  # noqa: E501

        :param transition_complete: The transition_complete of this LampState.  # noqa: E501
        :type transition_complete: bool
        """

        self._transition_complete = transition_complete

    @property
    def active_shows(self):
        """Gets the active_shows of this LampState.  # noqa: E501

        indicates the show groups that are currently active for the group.  New for API schema 4.  # noqa: E501

        :return: The active_shows of this LampState.  # noqa: E501
        :rtype: list[int]
        """
        return self._active_shows

    @active_shows.setter
    def active_shows(self, active_shows):
        """Sets the active_shows of this LampState.

        indicates the show groups that are currently active for the group.  New for API schema 4.  # noqa: E501

        :param active_shows: The active_shows of this LampState.  # noqa: E501
        :type active_shows: list[int]
        """

        self._active_shows = active_shows

    @property
    def start_state(self):
        """Gets the start_state of this LampState.  # noqa: E501


        :return: The start_state of this LampState.  # noqa: E501
        :rtype: LampStateParameters
        """
        return self._start_state

    @start_state.setter
    def start_state(self, start_state):
        """Sets the start_state of this LampState.


        :param start_state: The start_state of this LampState.  # noqa: E501
        :type start_state: LampStateParameters
        """

        self._start_state = start_state

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LampState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LampState):
            return True

        return self.to_dict() != other.to_dict()
