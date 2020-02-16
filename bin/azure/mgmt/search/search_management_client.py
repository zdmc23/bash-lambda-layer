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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.admin_keys_operations import AdminKeysOperations
from .operations.query_keys_operations import QueryKeysOperations
from .operations.services_operations import ServicesOperations
from . import models


class SearchManagementClientConfiguration(AzureConfiguration):
    """Configuration for SearchManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The unique identifier for a Microsoft Azure
     subscription. You can obtain this value from the Azure Resource Manager
     API or the portal.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(SearchManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-search/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class SearchManagementClient(SDKClient):
    """Client that can be used to manage Azure Search services and API keys.

    :ivar config: Configuration for client.
    :vartype config: SearchManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.search.operations.Operations
    :ivar admin_keys: AdminKeys operations
    :vartype admin_keys: azure.mgmt.search.operations.AdminKeysOperations
    :ivar query_keys: QueryKeys operations
    :vartype query_keys: azure.mgmt.search.operations.QueryKeysOperations
    :ivar services: Services operations
    :vartype services: azure.mgmt.search.operations.ServicesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The unique identifier for a Microsoft Azure
     subscription. You can obtain this value from the Azure Resource Manager
     API or the portal.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = SearchManagementClientConfiguration(credentials, subscription_id, base_url)
        super(SearchManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2015-08-19'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.admin_keys = AdminKeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.query_keys = QueryKeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.services = ServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
