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
module: avi_l4policyset
author: Chaitanya Deshpande (@chaitanyaavi) <chaitanya.deshpande@avinetworks.com>
short_description: Module for setup of L4PolicySet Avi RESTful Object
description:
    - This module is used to configure L4PolicySet object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.6"
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
    created_by:
        description:
            - Creator name.
            - Field introduced in 17.2.7.
        type: str
    description:
        description:
            - Field introduced in 17.2.7.
        type: str
    is_internal_policy:
        description:
            - Field introduced in 17.2.7.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    l4_connection_policy:
        description:
            - Policy to apply when a new transport connection is setup.
            - Field introduced in 17.2.7.
        type: dict
    labels:
        description:
            - Key value pairs for granular object access control.
            - Also allows for classification and tagging of similar objects.
            - Field introduced in 20.1.2.
            - Maximum of 4 items allowed.
        type: list
    name:
        description:
            - Name of the l4 policy set.
            - Field introduced in 17.2.7.
        required: true
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Field introduced in 17.2.7.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Id of the l4 policy set.
            - Field introduced in 17.2.7.
        type: str
extends_documentation_fragment:
    - vmware.nsx_alb
'''

EXAMPLES = """
- name: Example to create L4PolicySet object
  avi_l4policyset:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_l4policyset
"""

RETURN = '''
obj:
    description: L4PolicySet (api/l4policyset) object
    returned: success, changed
    type: dict
'''


