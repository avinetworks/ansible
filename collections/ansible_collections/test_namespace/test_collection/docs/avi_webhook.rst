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
module: avi_webhook
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of Webhook Avi RESTful Object
description:
    - This module is used to configure Webhook object
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
    callback_url:
        description:
            - Callback url for the webhook.
            - Field introduced in 17.1.1.
        type: str
    description:
        description:
            - Field introduced in 17.1.1.
        type: str
    name:
        description:
            - The name of the webhook profile.
            - Field introduced in 17.1.1.
        required: true
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Field introduced in 17.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the webhook profile.
            - Field introduced in 17.1.1.
        type: str
    verification_token:
        description:
            - Verification token sent back with the callback asquery parameters.
            - Field introduced in 17.1.1.
        type: str
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create Webhook object
  avi_webhook:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_webhook
"""

RETURN = '''
obj:
    description: Webhook (api/webhook) object
    returned: success, changed
    type: dict
'''


