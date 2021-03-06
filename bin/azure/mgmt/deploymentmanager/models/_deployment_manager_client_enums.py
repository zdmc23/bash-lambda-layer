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

from enum import Enum


class DeploymentMode(str, Enum):

    incremental = "Incremental"
    complete = "Complete"


class RestRequestMethod(str, Enum):

    get = "GET"
    post = "POST"


class RestMatchQuantifier(str, Enum):

    all = "All"
    any = "Any"


class RestAuthLocation(str, Enum):

    query = "Query"
    header = "Header"
