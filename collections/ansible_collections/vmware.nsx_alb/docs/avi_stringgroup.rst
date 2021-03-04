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
module: avi_stringgroup
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of StringGroup Avi RESTful Object
description:
    - This module is used to configure StringGroup object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
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
            - User defined description for the object.
        type: str
    kv:
        description:
            - Configure key value in the string group.
        type: list
    labels:
        description:
            - Key value pairs for granular object access control.
            - Also allows for classification and tagging of similar objects.
            - Field introduced in 20.1.2.
            - Maximum of 4 items allowed.
        type: list
    longest_match:
        description:
            - Enable the longest match, default is the shortest match.
            - Field introduced in 18.2.8.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    name:
        description:
            - Name of the string group.
        required: true
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    type:
        description:
            - Type of stringgroup.
            - Enum options - SG_TYPE_STRING, SG_TYPE_KEYVAL.
            - Default value when not specified in API or module is interpreted by Avi Controller as SG_TYPE_STRING.
        required: true
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the string group.
        type: str
extends_documentation_fragment:
    - vmware.nsx_alb
'''

EXAMPLES = """
  - name: Create a string group configuration
    avi_stringgroup:
      controller: '{{ controller }}'
      password: '{{ password }}'
      username: '{{ username }}'
      kv:
      - key: text/html
      - key: text/xml
      - key: text/plain
      - key: text/css
      - key: text/javascript
      - key: application/javascript
      - key: application/x-javascript
      - key: application/xml
      - key: application/pdf
      name: System-Compressible-Content-Types
      tenant_ref: /api/tenant?name=admin
      type: SG_TYPE_STRING
"""

RETURN = '''
obj:
    description: StringGroup (api/stringgroup) object
    returned: success, changed
    type: dict
'''


