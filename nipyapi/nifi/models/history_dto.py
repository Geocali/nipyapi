# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.8.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HistoryDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'total': 'int',
        'last_refreshed': 'str',
        'actions': 'list[ActionEntity]'
    }

    attribute_map = {
        'total': 'total',
        'last_refreshed': 'lastRefreshed',
        'actions': 'actions'
    }

    def __init__(self, total=None, last_refreshed=None, actions=None):
        """
        HistoryDTO - a model defined in Swagger
        """

        self._total = None
        self._last_refreshed = None
        self._actions = None

        if total is not None:
          self.total = total
        if last_refreshed is not None:
          self.last_refreshed = last_refreshed
        if actions is not None:
          self.actions = actions

    @property
    def total(self):
        """
        Gets the total of this HistoryDTO.
        The number of number of actions that matched the search criteria..

        :return: The total of this HistoryDTO.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this HistoryDTO.
        The number of number of actions that matched the search criteria..

        :param total: The total of this HistoryDTO.
        :type: int
        """

        self._total = total

    @property
    def last_refreshed(self):
        """
        Gets the last_refreshed of this HistoryDTO.
        The timestamp when the report was generated.

        :return: The last_refreshed of this HistoryDTO.
        :rtype: str
        """
        return self._last_refreshed

    @last_refreshed.setter
    def last_refreshed(self, last_refreshed):
        """
        Sets the last_refreshed of this HistoryDTO.
        The timestamp when the report was generated.

        :param last_refreshed: The last_refreshed of this HistoryDTO.
        :type: str
        """

        self._last_refreshed = last_refreshed

    @property
    def actions(self):
        """
        Gets the actions of this HistoryDTO.
        The actions.

        :return: The actions of this HistoryDTO.
        :rtype: list[ActionEntity]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this HistoryDTO.
        The actions.

        :param actions: The actions of this HistoryDTO.
        :type: list[ActionEntity]
        """

        self._actions = actions

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, HistoryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
