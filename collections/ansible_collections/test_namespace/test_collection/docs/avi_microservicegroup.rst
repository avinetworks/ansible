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
module: avi_microservicegroup
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of MicroServiceGroup Avi RESTful Object
description:
    - This module is used to configure MicroServiceGroup object
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
    created_by:
        description:
            - Creator name.
        type: str
    description:
        description:
            - User defined description for the object.
        type: str
    name:
        description:
            - Name of the microservice group.
        required: true
        type: str
    service_refs:
        description:
            - Configure microservice(es).
            - It is a reference to an object of type microservice.
        type: list
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the microservice group.
        type: str
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
  - name: Create a Microservice Group that can be used for setting up Network security policy
    avi_microservicegroup:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      description: Group created by my Secure My App UI.
      name: vs-msg-marketing
      tenant_ref: /api/tenant?name=admin
"""

RETURN = '''
obj:
    description: MicroServiceGroup (api/microservicegroup) object
    returned: success, changed
    type: dict
'''


