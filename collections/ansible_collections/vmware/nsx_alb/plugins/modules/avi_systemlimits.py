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
module: avi_systemlimits
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of SystemLimits Avi RESTful Object
description:
    - This module is used to configure SystemLimits object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
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
    - vmware.nsx_alb.avi
'''

EXAMPLES = """
- name: Example to create SystemLimits object
  vmware.nsx_alb.avi_systemlimits:
    controller: 192.168.15.18
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

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.nsx_alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, avi_ansible_api)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        controller_limits=dict(type='dict',),
        controller_sizes=dict(type='list',),
        serviceengine_limits=dict(type='dict',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg='python API `requests` is not installed.')
    return avi_ansible_api(module, 'systemlimits',
                           set())


if __name__ == '__main__':
    main()
