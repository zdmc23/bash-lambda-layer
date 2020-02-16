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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class ApplicationsOperations(object):
    """ApplicationsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API version. Constant value: "1.6".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "1.6"

        self.config = config

    def create(
            self, parameters, custom_headers=None, raw=False, **operation_config):
        """Create a new application.

        :param parameters: The parameters for creating an application.
        :type parameters: ~azure.graphrbac.models.ApplicationCreateParameters
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Application or ClientRawResponse if raw=true
        :rtype: ~azure.graphrbac.models.Application or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ApplicationCreateParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.GraphErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('Application', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create.metadata = {'url': '/{tenantID}/applications'}

    def list(
            self, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists applications by filter parameters.

        :param filter: The filters to apply to the operation.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Application
        :rtype:
         ~azure.graphrbac.models.ApplicationPaged[~azure.graphrbac.models.Application]
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = '/{tenantID}/{nextLink}'
                path_format_arguments = {
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.ApplicationPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ApplicationPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/{tenantID}/applications'}

    def delete(
            self, application_object_id, custom_headers=None, raw=False, **operation_config):
        """Delete an application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}'}

    def get(
            self, application_object_id, custom_headers=None, raw=False, **operation_config):
        """Get an application by object ID.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Application or ClientRawResponse if raw=true
        :rtype: ~azure.graphrbac.models.Application or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.GraphErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Application', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}'}

    def patch(
            self, application_object_id, parameters, custom_headers=None, raw=False, **operation_config):
        """Update an existing application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param parameters: Parameters to update an existing application.
        :type parameters: ~azure.graphrbac.models.ApplicationUpdateParameters
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = self.patch.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ApplicationUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    patch.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}'}

    def list_owners(
            self, application_object_id, custom_headers=None, raw=False, **operation_config):
        """Directory objects that are owners of the application.

        The owners are a set of non-admin users who are allowed to modify this
        object.

        :param application_object_id: The object ID of the application for
         which to get owners.
        :type application_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DirectoryObject
        :rtype:
         ~azure.graphrbac.models.DirectoryObjectPaged[~azure.graphrbac.models.DirectoryObject]
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_owners.metadata['url']
                path_format_arguments = {
                    'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.DirectoryObjectPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.DirectoryObjectPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_owners.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/owners'}

    def add_owner(
            self, application_object_id, url, additional_properties=None, custom_headers=None, raw=False, **operation_config):
        """Add an owner to an application.

        :param application_object_id: The object ID of the application to
         which to add the owner.
        :type application_object_id: str
        :param url: A owner object URL, such as
         "https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd",
         where "0b1f9851-1bf0-433f-aec3-cb9272f093dc" is the tenantId and
         "f260bbc4-c254-447b-94cf-293b5ec434dd" is the objectId of the owner
         (user, application, servicePrincipal, group) to be added.
        :type url: str
        :param additional_properties: Unmatched properties from the message
         are deserialized this collection
        :type additional_properties: dict[str, object]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        parameters = models.AddOwnerParameters(additional_properties=additional_properties, url=url)

        # Construct URL
        url = self.add_owner.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'AddOwnerParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    add_owner.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/$links/owners'}

    def remove_owner(
            self, application_object_id, owner_object_id, custom_headers=None, raw=False, **operation_config):
        """Remove a member from owners.

        :param application_object_id: The object ID of the application from
         which to remove the owner.
        :type application_object_id: str
        :param owner_object_id: Owner object id
        :type owner_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        # Construct URL
        url = self.remove_owner.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'ownerObjectId': self._serialize.url("owner_object_id", owner_object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    remove_owner.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/$links/owners/{ownerObjectId}'}

    def list_key_credentials(
            self, application_object_id, custom_headers=None, raw=False, **operation_config):
        """Get the keyCredentials associated with an application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of KeyCredential
        :rtype:
         ~azure.graphrbac.models.KeyCredentialPaged[~azure.graphrbac.models.KeyCredential]
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_key_credentials.metadata['url']
                path_format_arguments = {
                    'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.KeyCredentialPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.KeyCredentialPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_key_credentials.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/keyCredentials'}

    def update_key_credentials(
            self, application_object_id, value, custom_headers=None, raw=False, **operation_config):
        """Update the keyCredentials associated with an application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param value: A collection of KeyCredentials.
        :type value: list[~azure.graphrbac.models.KeyCredential]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        parameters = models.KeyCredentialsUpdateParameters(value=value)

        # Construct URL
        url = self.update_key_credentials.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'KeyCredentialsUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    update_key_credentials.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/keyCredentials'}

    def list_password_credentials(
            self, application_object_id, custom_headers=None, raw=False, **operation_config):
        """Get the passwordCredentials associated with an application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PasswordCredential
        :rtype:
         ~azure.graphrbac.models.PasswordCredentialPaged[~azure.graphrbac.models.PasswordCredential]
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_password_credentials.metadata['url']
                path_format_arguments = {
                    'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
                    'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.GraphErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.PasswordCredentialPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.PasswordCredentialPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_password_credentials.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/passwordCredentials'}

    def update_password_credentials(
            self, application_object_id, value, custom_headers=None, raw=False, **operation_config):
        """Update passwordCredentials associated with an application.

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param value: A collection of PasswordCredentials.
        :type value: list[~azure.graphrbac.models.PasswordCredential]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`GraphErrorException<azure.graphrbac.models.GraphErrorException>`
        """
        parameters = models.PasswordCredentialsUpdateParameters(value=value)

        # Construct URL
        url = self.update_password_credentials.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'tenantID': self._serialize.url("self.config.tenant_id", self.config.tenant_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'PasswordCredentialsUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.GraphErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    update_password_credentials.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/passwordCredentials'}