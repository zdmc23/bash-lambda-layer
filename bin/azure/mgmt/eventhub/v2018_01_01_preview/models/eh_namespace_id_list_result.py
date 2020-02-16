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


class EHNamespaceIdListResult(Model):
    """The response of the List Namespace IDs operation.

    :param value: Result of the List Namespace IDs operation
    :type value:
     list[~azure.mgmt.eventhub.v2018_01_01_preview.models.EHNamespaceIdContainer]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[EHNamespaceIdContainer]'},
    }

    def __init__(self, **kwargs):
        super(EHNamespaceIdListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
