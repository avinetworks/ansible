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
module: avi_wafapplicationsignatureprovider
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of WafApplicationSignatureProvider Avi RESTful Object
description:
    - This module is used to configure WafApplicationSignatureProvider object
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
    available_applications:
        description:
            - Available application names and the ruleset version, when the rules for an application changed the last time.
            - Field introduced in 20.1.1.
        type: list
    last_check_for_updates_error:
        description:
            - The error message indicating why the last update check failed.
            - Field deprecated in 20.1.3.
            - Field introduced in 20.1.1.
        type: str
    last_failed_check_for_updates:
        description:
            - The last time that we checked for updates but did not get a result because of an error.
            - Field deprecated in 20.1.3.
            - Field introduced in 20.1.1.
        type: dict
    last_successful_check_for_updates:
        description:
            - The last time that we checked for updates sucessfully.
            - Field deprecated in 20.1.3.
            - Field introduced in 20.1.1.
        type: dict
    name:
        description:
            - Name of application specific ruleset provider.
            - Field introduced in 20.1.1.
        type: str
    ruleset_version:
        description:
            - Version of signatures.
            - Field introduced in 20.1.1.
        type: str
    service_status:
        description:
            - If this object is managed by the application signatures update  service, this field contain the status of this syncronization.
            - Field introduced in 20.1.3.
        type: dict
    signatures:
        description:
            - The waf rules.
            - Not visible in the api.
            - Field introduced in 20.1.1.
        type: list
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Field introduced in 20.1.1.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- name: Example to create WafApplicationSignatureProvider object
  vmware.alb.avi_wafapplicationsignatureprovider:
    controller: 192.168.15.18
    username: admin
    password: something
    state: present
    name: sample_wafapplicationsignatureprovider
"""

RETURN = '''
obj:
    description: WafApplicationSignatureProvider (api/wafapplicationsignatureprovider) object
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
        available_applications=dict(type='list',),
        last_check_for_updates_error=dict(type='str',),
        last_failed_check_for_updates=dict(type='dict',),
        last_successful_check_for_updates=dict(type='dict',),
        name=dict(type='str',),
        ruleset_version=dict(type='str',),
        service_status=dict(type='dict',),
        signatures=dict(type='list',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
                    'Python requests package is not installed. '
                    'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'wafapplicationsignatureprovider',
                           set())


if __name__ == '__main__':
    main()
