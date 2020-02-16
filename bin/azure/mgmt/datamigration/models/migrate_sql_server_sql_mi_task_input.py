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

from .sql_migration_task_input import SqlMigrationTaskInput


class MigrateSqlServerSqlMITaskInput(SqlMigrationTaskInput):
    """Input for task that migrates SQL Server databases to Azure SQL Database
    Managed Instance.

    All required parameters must be populated in order to send to Azure.

    :param source_connection_info: Required. Information for connecting to
     source
    :type source_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param target_connection_info: Required. Information for connecting to
     target
    :type target_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param selected_databases: Required. Databases to migrate
    :type selected_databases:
     list[~azure.mgmt.datamigration.models.MigrateSqlServerSqlMIDatabaseInput]
    :param selected_logins: Logins to migrate.
    :type selected_logins: list[str]
    :param selected_agent_jobs: Agent Jobs to migrate.
    :type selected_agent_jobs: list[str]
    :param backup_file_share: Backup file share information for all selected
     databases.
    :type backup_file_share: ~azure.mgmt.datamigration.models.FileShare
    :param backup_blob_share: Required. SAS URI of Azure Storage Account
     Container to be used for storing backup files.
    :type backup_blob_share: ~azure.mgmt.datamigration.models.BlobShare
    """

    _validation = {
        'source_connection_info': {'required': True},
        'target_connection_info': {'required': True},
        'selected_databases': {'required': True},
        'backup_blob_share': {'required': True},
    }

    _attribute_map = {
        'source_connection_info': {'key': 'sourceConnectionInfo', 'type': 'SqlConnectionInfo'},
        'target_connection_info': {'key': 'targetConnectionInfo', 'type': 'SqlConnectionInfo'},
        'selected_databases': {'key': 'selectedDatabases', 'type': '[MigrateSqlServerSqlMIDatabaseInput]'},
        'selected_logins': {'key': 'selectedLogins', 'type': '[str]'},
        'selected_agent_jobs': {'key': 'selectedAgentJobs', 'type': '[str]'},
        'backup_file_share': {'key': 'backupFileShare', 'type': 'FileShare'},
        'backup_blob_share': {'key': 'backupBlobShare', 'type': 'BlobShare'},
    }

    def __init__(self, **kwargs):
        super(MigrateSqlServerSqlMITaskInput, self).__init__(**kwargs)
        self.selected_databases = kwargs.get('selected_databases', None)
        self.selected_logins = kwargs.get('selected_logins', None)
        self.selected_agent_jobs = kwargs.get('selected_agent_jobs', None)
        self.backup_file_share = kwargs.get('backup_file_share', None)
        self.backup_blob_share = kwargs.get('backup_blob_share', None)
