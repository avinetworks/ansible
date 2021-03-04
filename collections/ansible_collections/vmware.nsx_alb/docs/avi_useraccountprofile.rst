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
module: avi_useraccountprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of UserAccountProfile Avi RESTful Object
description:
    - This module is used to configure UserAccountProfile object
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
    account_lock_timeout:
        description:
            - Lock timeout period (in minutes).
            - Default is 30 minutes.
            - Unit is min.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    credentials_timeout_threshold:
        description:
            - The time period after which credentials expire.
            - Default is 180 days.
            - Unit is days.
            - Default value when not specified in API or module is interpreted by Avi Controller as 180.
        type: int
    max_concurrent_sessions:
        description:
            - Maximum number of concurrent sessions allowed.
            - There are unlimited sessions by default.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    max_login_failure_count:
        description:
            - Number of login attempts before lockout.
            - Default is 3 attempts.
            - Allowed values are 3-20.
            - Special values are 0 - 'unlimited login attempts allowed.'.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    max_password_history_count:
        description:
            - Maximum number of passwords to be maintained in the password history.
            - Default is 4 passwords.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    name:
        description:
            - Name of the object.
        required: true
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
    - vmware.nsx_alb
'''

EXAMPLES = """
- name: Example to create UserAccountProfile object
  avi_useraccountprofile:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_useraccountprofile
"""

RETURN = '''
obj:
    description: UserAccountProfile (api/useraccountprofile) object
    returned: success, changed
    type: dict
'''


