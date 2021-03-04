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
module: avi_systemlimits
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of SystemLimits Avi RESTful Object
description:
    - This module is used to configure SystemLimits object
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
    controller_limits:
        description:
            - System limits for the entire controller cluster.
            - Field introduced in 20.1.1.
        type: dict
    controller_sizes:
        description:
            - Possible controller sizes.
            - Field introduced in 20.1.1.
        type: list
    serviceengine_limits:
        description:
            - System limits that apply to a serviceengine.
            - Field introduced in 20.1.1.
        type: dict
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid for the system limits object.
            - Field introduced in 20.1.1.
        type: str
extends_documentation_fragment:
    - vmware.nsx_alb
'''

EXAMPLES = """
- name: Example to create SystemLimits object
  avi_systemlimits:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_systemlimits
"""

RETURN = '''
obj:
    description: SystemLimits (api/systemlimits) object
    returned: success, changed
    type: dict
'''


