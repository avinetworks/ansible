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
module: avi_geodb
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of GeoDB Avi RESTful Object
description:
    - This module is used to configure GeoDB object
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
    description:
        description:
            - Description.
            - Field introduced in 21.1.1.
        type: str
    files:
        description:
            - Geo database files.
            - Field introduced in 21.1.1.
        required: true
        type: list
    is_federated:
        description:
            - This field indicates that this object is replicated across gslb federation.
            - Field introduced in 21.1.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    mappings:
        description:
            - Custom mappings of geo values.
            - All mappings which start with the prefix 'system-' (any case) are reserved for system default objects and may be overwritten.
            - Field introduced in 21.1.1.
        type: list
    name:
        description:
            - Geo database name.
            - Field introduced in 21.1.1.
        required: true
        type: str
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 21.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of this object.
            - Field introduced in 21.1.1.
        type: str
extends_documentation_fragment:
    - vmware.nsx_alb
'''

EXAMPLES = """
- name: Example to create GeoDB object
  avi_geodb:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_geodb
"""

RETURN = '''
obj:
    description: GeoDB (api/geodb) object
    returned: success, changed
    type: dict
'''


