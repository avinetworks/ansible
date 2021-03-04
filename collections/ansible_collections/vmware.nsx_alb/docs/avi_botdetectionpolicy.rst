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
module: avi_botdetectionpolicy
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of BotDetectionPolicy Avi RESTful Object
description:
    - This module is used to configure BotDetectionPolicy object
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
    allow_list:
        description:
            - Allow the user to skip botmanagement for selected requests.
            - Field introduced in 21.1.1.
        type: dict
    bot_mapping_uuids:
        description:
            - System- and user-defined rules for classification.
            - Field introduced in 21.1.1.
        type: list
    consolidator_ref:
        description:
            - The installation provides an updated ruleset for consolidating the results of different decider phases.
            - It is a reference to an object of type botconfigconsolidator.
            - Field introduced in 21.1.1.
        type: str
    description:
        description:
            - Human-readable description of this bot detection policy.
            - Field introduced in 21.1.1.
        type: str
    ip_location_detector:
        description:
            - The ip location configuration used in this policy.
            - Field introduced in 21.1.1.
        required: true
        type: dict
    ip_reputation_detector:
        description:
            - The ip reputation configuration used in this policy.
            - Field introduced in 21.1.1.
        required: true
        type: dict
    name:
        description:
            - The name of this bot detection policy.
            - Field introduced in 21.1.1.
        required: true
        type: str
    tenant_ref:
        description:
            - The unique identifier of the tenant to which this policy belongs.
            - It is a reference to an object of type tenant.
            - Field introduced in 21.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    user_agent_detector:
        description:
            - The user-agent configuration used in this policy.
            - Field introduced in 21.1.1.
        required: true
        type: dict
    uuid:
        description:
            - A unique identifier to this bot detection policy.
            - Field introduced in 21.1.1.
        type: str
extends_documentation_fragment:
    - vmware.nsx_alb
'''

EXAMPLES = """
- name: Example to create BotDetectionPolicy object
  avi_botdetectionpolicy:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_botdetectionpolicy
"""

RETURN = '''
obj:
    description: BotDetectionPolicy (api/botdetectionpolicy) object
    returned: success, changed
    type: dict
'''


