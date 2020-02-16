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

from .catalog_item import CatalogItem


class USqlView(CatalogItem):
    """A Data Lake Analytics catalog U-SQL view item.

    :param compute_account_name: the name of the Data Lake Analytics account.
    :type compute_account_name: str
    :param version: the version of the catalog item.
    :type version: str
    :param database_name: the name of the database.
    :type database_name: str
    :param schema_name: the name of the schema associated with this view and
     database.
    :type schema_name: str
    :param name: the name of the view.
    :type name: str
    :param definition: the defined query of the view.
    :type definition: str
    """

    _attribute_map = {
        'compute_account_name': {'key': 'computeAccountName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'schema_name': {'key': 'schemaName', 'type': 'str'},
        'name': {'key': 'viewName', 'type': 'str'},
        'definition': {'key': 'definition', 'type': 'str'},
    }

    def __init__(self, compute_account_name=None, version=None, database_name=None, schema_name=None, name=None, definition=None):
        super(USqlView, self).__init__(compute_account_name=compute_account_name, version=version)
        self.database_name = database_name
        self.schema_name = schema_name
        self.name = name
        self.definition = definition
