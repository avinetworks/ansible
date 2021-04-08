#!/usr/bin/python3
# module_check: supported
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_vcenterserver
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of VCenterServer Avi RESTful Object
description:
    - This module is used to configure VCenterServer object
    - more examples at U(https://github.com/avinetworks/devops)
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
    cloud_ref:
        description:
            - Vcenter belongs to cloud.
            - It is a reference to an object of type cloud.
            - Field introduced in 20.1.1.
        type: str
    content_lib:
        description:
            - Vcenter template to create service engine.
            - Field introduced in 20.1.1.
        required: true
        type: dict
    name:
        description:
            - Availabilty zone where vcenter list belongs to.
            - Field introduced in 20.1.1.
        required: true
        type: str
    tenant_ref:
        description:
            - Vcenter belongs to tenant.
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Vcenter config uuid.
            - Field introduced in 20.1.1.
        type: str
    vcenter_credentials_ref:
        description:
            - Credentials to access vcenter.
            - It is a reference to an object of type cloudconnectoruser.
            - Field introduced in 20.1.1.
        required: true
        type: str
    vcenter_url:
        description:
            - Vcenter hostname or ip address.
            - Field introduced in 20.1.1.
        required: true
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Example to create VCenterServer object
  vmware.alb.avi_vcenterserver:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_vcenterserver
"""

RETURN = '''
obj:
    description: VCenterServer (api/vcenterserver) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
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
        cloud_ref=dict(type='str',),
        content_lib=dict(type='dict', required=True),
        name=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vcenter_credentials_ref=dict(type='str', required=True),
        vcenter_url=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg='python API `requests` is not installed.')
    return avi_ansible_api(module, 'vcenterserver',
                           set())


if __name__ == '__main__':
    main()
