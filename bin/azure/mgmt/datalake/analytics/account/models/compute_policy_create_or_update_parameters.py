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


class ComputePolicyCreateOrUpdateParameters(Model):
    """The parameters used to create a new compute policy.

    :param object_id: The AAD object identifier for the entity to create a
     policy for.
    :type object_id: str
    :param object_type: The type of AAD object the object identifier refers
     to. Possible values include: 'User', 'Group', 'ServicePrincipal'
    :type object_type: str or :class:`AADObjectType
     <azure.mgmt.datalake.analytics.account.models.AADObjectType>`
    :param max_degree_of_parallelism_per_job: The maximum degree of
     parallelism per job this user can use to submit jobs. This property, the
     min priority per job property, or both must be passed.
    :type max_degree_of_parallelism_per_job: int
    :param min_priority_per_job: The minimum priority per job this user can
     use to submit jobs. This property, the max degree of parallelism per job
     property, or both must be passed.
    :type min_priority_per_job: int
    """

    _validation = {
        'object_id': {'required': True},
        'object_type': {'required': True},
        'max_degree_of_parallelism_per_job': {'minimum': 1},
        'min_priority_per_job': {'minimum': 1},
    }

    _attribute_map = {
        'object_id': {'key': 'properties.objectId', 'type': 'str'},
        'object_type': {'key': 'properties.objectType', 'type': 'str'},
        'max_degree_of_parallelism_per_job': {'key': 'properties.maxDegreeOfParallelismPerJob', 'type': 'int'},
        'min_priority_per_job': {'key': 'properties.minPriorityPerJob', 'type': 'int'},
    }

    def __init__(self, object_id, object_type, max_degree_of_parallelism_per_job=None, min_priority_per_job=None):
        self.object_id = object_id
        self.object_type = object_type
        self.max_degree_of_parallelism_per_job = max_degree_of_parallelism_per_job
        self.min_priority_per_job = min_priority_per_job
