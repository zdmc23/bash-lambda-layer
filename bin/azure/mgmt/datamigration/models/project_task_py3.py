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

from .resource import Resource


class ProjectTask(Resource):
    """A task resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param etag: HTTP strong entity tag value. This is ignored if submitted.
    :type etag: str
    :param properties: Custom task properties
    :type properties: ~azure.mgmt.datamigration.models.ProjectTaskProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ProjectTaskProperties'},
    }

    def __init__(self, *, etag: str=None, properties=None, **kwargs) -> None:
        super(ProjectTask, self).__init__(**kwargs)
        self.etag = etag
        self.properties = properties
