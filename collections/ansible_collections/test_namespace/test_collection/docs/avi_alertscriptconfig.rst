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
module: avi_alertscriptconfig
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of AlertScriptConfig Avi RESTful Object
description:
    - This module is used to configure AlertScriptConfig object
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
    action_script:
        description:
            - User defined alert action script.
            - Please refer to kb.avinetworks.com for more information.
        type: str
    name:
        description:
            - A user-friendly name of the script.
        required: true
        type: str
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
            - Unique object identifier of the object.
        type: str
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
  - name: Create Alert Script to perform AWS server autoscaling
    avi_alertscriptconfig:
      username: '{{ username }}'
      controller: '{{ controller }}'
      password: '{{ password }}'
      action_script: "echo Hello"
      name: AWS-Launch-Script
      tenant_ref: /api/tenant?name=Demo
"""

RETURN = '''
obj:
    description: AlertScriptConfig (api/alertscriptconfig) object
    returned: success, changed
    type: dict
'''


