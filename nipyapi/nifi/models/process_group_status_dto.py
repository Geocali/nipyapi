# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.10.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProcessGroupStatusDTO(object):
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
        'id': 'str',
        'name': 'str',
        'stats_last_refreshed': 'str',
        'aggregate_snapshot': 'ProcessGroupStatusSnapshotDTO',
        'node_snapshots': 'list[NodeProcessGroupStatusSnapshotDTO]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'stats_last_refreshed': 'statsLastRefreshed',
        'aggregate_snapshot': 'aggregateSnapshot',
        'node_snapshots': 'nodeSnapshots'
    }

    def __init__(self, id=None, name=None, stats_last_refreshed=None, aggregate_snapshot=None, node_snapshots=None):
        """
        ProcessGroupStatusDTO - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._stats_last_refreshed = None
        self._aggregate_snapshot = None
        self._node_snapshots = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if stats_last_refreshed is not None:
          self.stats_last_refreshed = stats_last_refreshed
        if aggregate_snapshot is not None:
          self.aggregate_snapshot = aggregate_snapshot
        if node_snapshots is not None:
          self.node_snapshots = node_snapshots

    @property
    def id(self):
        """
        Gets the id of this ProcessGroupStatusDTO.
        The ID of the Process Group

        :return: The id of this ProcessGroupStatusDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProcessGroupStatusDTO.
        The ID of the Process Group

        :param id: The id of this ProcessGroupStatusDTO.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ProcessGroupStatusDTO.
        The name of the Process Group

        :return: The name of this ProcessGroupStatusDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProcessGroupStatusDTO.
        The name of the Process Group

        :param name: The name of this ProcessGroupStatusDTO.
        :type: str
        """

        self._name = name

    @property
    def stats_last_refreshed(self):
        """
        Gets the stats_last_refreshed of this ProcessGroupStatusDTO.
        The time the status for the process group was last refreshed.

        :return: The stats_last_refreshed of this ProcessGroupStatusDTO.
        :rtype: str
        """
        return self._stats_last_refreshed

    @stats_last_refreshed.setter
    def stats_last_refreshed(self, stats_last_refreshed):
        """
        Sets the stats_last_refreshed of this ProcessGroupStatusDTO.
        The time the status for the process group was last refreshed.

        :param stats_last_refreshed: The stats_last_refreshed of this ProcessGroupStatusDTO.
        :type: str
        """

        self._stats_last_refreshed = stats_last_refreshed

    @property
    def aggregate_snapshot(self):
        """
        Gets the aggregate_snapshot of this ProcessGroupStatusDTO.
        The aggregate status of all nodes in the cluster

        :return: The aggregate_snapshot of this ProcessGroupStatusDTO.
        :rtype: ProcessGroupStatusSnapshotDTO
        """
        return self._aggregate_snapshot

    @aggregate_snapshot.setter
    def aggregate_snapshot(self, aggregate_snapshot):
        """
        Sets the aggregate_snapshot of this ProcessGroupStatusDTO.
        The aggregate status of all nodes in the cluster

        :param aggregate_snapshot: The aggregate_snapshot of this ProcessGroupStatusDTO.
        :type: ProcessGroupStatusSnapshotDTO
        """

        self._aggregate_snapshot = aggregate_snapshot

    @property
    def node_snapshots(self):
        """
        Gets the node_snapshots of this ProcessGroupStatusDTO.
        The status reported by each node in the cluster. If the NiFi instance is a standalone instance, rather than a clustered instance, this value may be null.

        :return: The node_snapshots of this ProcessGroupStatusDTO.
        :rtype: list[NodeProcessGroupStatusSnapshotDTO]
        """
        return self._node_snapshots

    @node_snapshots.setter
    def node_snapshots(self, node_snapshots):
        """
        Sets the node_snapshots of this ProcessGroupStatusDTO.
        The status reported by each node in the cluster. If the NiFi instance is a standalone instance, rather than a clustered instance, this value may be null.

        :param node_snapshots: The node_snapshots of this ProcessGroupStatusDTO.
        :type: list[NodeProcessGroupStatusSnapshotDTO]
        """

        self._node_snapshots = node_snapshots

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
        if not isinstance(other, ProcessGroupStatusDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
