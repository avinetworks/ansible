#!/usr/bin/python3
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
from __future__ import (absolute_import, division, print_function)


DOCUMENTATION = '''
---
module: avi_federationcheckpoint
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of FederationCheckpoint Avi RESTful Object
description:
    - This module is used to configure FederationCheckpoint object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.7"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        version_added: "2.5"
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        version_added: "2.5"
        choices: ["add", "replace", "delete"]
        type: str
    date:
        description:
            - Date when the checkpoint was created.
            - Field introduced in 20.1.1.
        type: str
    description:
        description:
            - Description for this checkpoint.
            - Field introduced in 20.1.1.
        type: str
    is_federated:
        description:
            - This field describes the object's replication scope.
            - If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines.
            - If the field is set to true, then the object is replicated across the federation.
            - Field introduced in 20.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    name:
        description:
            - Name of the checkpoint.
            - Field introduced in 20.1.1.
        required: true
        type: str
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the checkpoint.
            - Field introduced in 20.1.1.
        type: str
extends_documentation_fragment:
    - vmware.nsx_alb
'''

EXAMPLES = """
- name: Example to create FederationCheckpoint object
  avi_federationcheckpoint:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_federationcheckpoint
"""

RETURN = '''
obj:
    description: FederationCheckpoint (api/federationcheckpoint) object
    returned: success, changed
    type: dict
'''


