# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class USqlIndex(Model):
    """A Data Lake Analytics catalog U-SQL table index item.

    :param name: the name of the index in the table.
    :type name: str
    :param index_keys: the list of directed columns in the index
    :type index_keys: list of :class:`USqlDirectedColumn
     <azure.mgmt.datalake.analytics.catalog.models.USqlDirectedColumn>`
    :param columns: the list of columns in the index
    :type columns: list of str
    :param distribution_info: the distributions info of the index
    :type distribution_info: :class:`USqlDistributionInfo
     <azure.mgmt.datalake.analytics.catalog.models.USqlDistributionInfo>`
    :param partition_function: partition function ID for the index.
    :type partition_function: str
    :param partition_key_list: the list of partion keys in the index
    :type partition_key_list: list of str
    :param stream_names: the list of full paths to the streams that contain
     this index in the DataLake account.
    :type stream_names: list of str
    :param is_columnstore: the switch indicating if this index is a
     columnstore index.
    :type is_columnstore: bool
    :param index_id: the ID of this index within the table.
    :type index_id: int
    :param is_unique: the switch indicating if this index is a unique index.
    :type is_unique: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'index_keys': {'key': 'indexKeys', 'type': '[USqlDirectedColumn]'},
        'columns': {'key': 'columns', 'type': '[str]'},
        'distribution_info': {'key': 'distributionInfo', 'type': 'USqlDistributionInfo'},
        'partition_function': {'key': 'partitionFunction', 'type': 'str'},
        'partition_key_list': {'key': 'partitionKeyList', 'type': '[str]'},
        'stream_names': {'key': 'streamNames', 'type': '[str]'},
        'is_columnstore': {'key': 'isColumnstore', 'type': 'bool'},
        'index_id': {'key': 'indexId', 'type': 'int'},
        'is_unique': {'key': 'isUnique', 'type': 'bool'},
    }

    def __init__(self, name=None, index_keys=None, columns=None, distribution_info=None, partition_function=None, partition_key_list=None, stream_names=None, is_columnstore=None, index_id=None, is_unique=None):
        self.name = name
        self.index_keys = index_keys
        self.columns = columns
        self.distribution_info = distribution_info
        self.partition_function = partition_function
        self.partition_key_list = partition_key_list
        self.stream_names = stream_names
        self.is_columnstore = is_columnstore
        self.index_id = index_id
        self.is_unique = is_unique
