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
module: avi_protocolparser
author: Chaitanya Deshpande (@chaitanyaavi) <chaitanya.deshpande@avinetworks.com>
short_description: Module for setup of ProtocolParser Avi RESTful Object
description:
    - This module is used to configure ProtocolParser object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.9"
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
            - Description of the protocol parser.
            - Field introduced in 18.2.3.
        type: str
    labels:
        description:
            - Key value pairs for granular object access control.
            - Also allows for classification and tagging of similar objects.
            - Field introduced in 20.1.2.
            - Maximum of 4 items allowed.
        type: list
    name:
        description:
            - Name of the protocol parser.
            - Field introduced in 18.2.3.
        required: true
        type: str
    parser_code:
        description:
            - Command script provided inline.
            - Field introduced in 18.2.3.
        required: true
        type: str
    tenant_ref:
        description:
            - Tenant uuid of the protocol parser.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.3.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the protocol parser.
            - Field introduced in 18.2.3.
        type: str
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create ProtocolParser object
  avi_protocolparser:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_protocolparser
"""

RETURN = '''
obj:
    description: ProtocolParser (api/protocolparser) object
    returned: success, changed
    type: dict
'''


