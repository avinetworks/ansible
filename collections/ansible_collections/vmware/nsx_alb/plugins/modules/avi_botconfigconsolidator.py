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
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_botconfigconsolidator
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of BotConfigConsolidator Avi RESTful Object
description:
    - This module is used to configure BotConfigConsolidator object
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
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        choices: ["add", "replace", "delete"]
        type: str
    description:
        description:
            - Human-readable description of this consolidator.
            - Field introduced in 21.1.1.
        type: str
    name:
        description:
            - The name of this consolidator.
            - Field introduced in 21.1.1.
        required: true
        type: str
    script:
        description:
            - Script that consolidates results from all components.
            - Field introduced in 21.1.1.
        type: str
    tenant_ref:
        description:
            - The unique identifier of the tenant to which this mapping belongs.
            - It is a reference to an object of type tenant.
            - Field introduced in 21.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - A unique identifier to this consolidator.
            - Field introduced in 21.1.1.
        type: str
extends_documentation_fragment:
    - vmware.nsx_alb.avi
'''

EXAMPLES = """
- name: Example to create BotConfigConsolidator object
  avi_botconfigconsolidator:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_botconfigconsolidator
"""

RETURN = '''
obj:
    description: BotConfigConsolidator (api/botconfigconsolidator) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from avi.sdk.utils.ansible_utils import (
        avi_ansible_api, avi_common_argument_spec)
    HAS_AVI = True
except ImportError:
    from ansible_collections.vmware.nsx_alb.plugins.module_utils.avi import (
        avi_common_argument_spec, avi_ansible_api, HAS_AVI)


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        description=dict(type='str',),
        name=dict(type='str', required=True),
        script=dict(type='str',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg='Avi python API SDK (avisdk>=17.1) or requests is not installed. '
                                    'For more details visit https://github.com/avinetworks/sdk.')

    return avi_ansible_api(module, 'botconfigconsolidator',
                           set())


if __name__ == "__main__":
    main()
