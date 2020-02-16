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

from .event_subscription_destination_py3 import EventSubscriptionDestination


class ServiceBusQueueEventSubscriptionDestination(EventSubscriptionDestination):
    """Information about the service bus destination for an event subscription.

    All required parameters must be populated in order to send to Azure.

    :param endpoint_type: Required. Constant filled by server.
    :type endpoint_type: str
    :param resource_id: The Azure Resource Id that represents the endpoint of
     the Service Bus destination of an event subscription.
    :type resource_id: str
    """

    _validation = {
        'endpoint_type': {'required': True},
    }

    _attribute_map = {
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
    }

    def __init__(self, *, resource_id: str=None, **kwargs) -> None:
        super(ServiceBusQueueEventSubscriptionDestination, self).__init__(**kwargs)
        self.resource_id = resource_id
        self.endpoint_type = 'ServiceBusQueue'
