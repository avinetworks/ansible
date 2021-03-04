#!/usr/bin/python3
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
# Avi Version: 17.1.1
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
from __future__ import (absolute_import, division, print_function)


DOCUMENTATION = '''
---
module: avi_tenant
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of Tenant Avi RESTful Object
description:
    - This module is used to configure Tenant object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
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
    config_settings:
        description:
            - Tenantconfiguration settings for tenant.
        type: dict
    created_by:
        description:
            - Creator of this tenant.
        type: str
    description:
        description:
            - User defined description for the object.
        type: str
    local:
        description:
            - Boolean flag to set local.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    name:
        description:
            - Name of the object.
        required: true
        type: str
    suggested_object_labels:
        description:
            - Suggestive pool of key value pairs for recommending assignment of labels to objects in the user interface.
            - Every entry is unique in both key and value.
            - Field introduced in 20.1.2.
            - Maximum of 256 items allowed.
        type: list
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Unique object identifier of the object.
        type: str
extends_documentation_fragment:
    - vmware.nsx_alb
'''

EXAMPLES = """
  - name: Create Tenant using Service Engines in provider mode
    avi_tenant:
      controller: '{{ controller }}'
      password: '{{ password }}'
      username: '{{ username }}'
      config_settings:
        se_in_provider_context: false
        tenant_access_to_provider_se: true
        tenant_vrf: false
      description: VCenter, Open Stack, AWS Virtual services
      local: true
      name: Demo
"""

RETURN = '''
obj:
    description: Tenant (api/tenant) object
    returned: success, changed
    type: dict
'''


