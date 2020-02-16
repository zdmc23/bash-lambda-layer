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


class DeadLetterDestination(Model):
    """Information about the dead letter destination for an event subscription. To
    configure a deadletter destination, do not directly instantiate an object
    of this class. Instead, instantiate an object of a derived class.
    Currently, StorageBlobDeadLetterDestination is the only class that derives
    from this class.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: StorageBlobDeadLetterDestination

    All required parameters must be populated in order to send to Azure.

    :param endpoint_type: Required. Constant filled by server.
    :type endpoint_type: str
    """

    _validation = {
        'endpoint_type': {'required': True},
    }

    _attribute_map = {
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
    }

    _subtype_map = {
        'endpoint_type': {'StorageBlob': 'StorageBlobDeadLetterDestination'}
    }

    def __init__(self, **kwargs):
        super(DeadLetterDestination, self).__init__(**kwargs)
        self.endpoint_type = None
