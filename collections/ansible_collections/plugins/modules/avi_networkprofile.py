#!/usr/bin/python3
# module_check: supported

# Avi Version: 17.1.1
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_networkprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>

short_description: Module for setup of NetworkProfile Avi RESTful Object
description:
    - This module is used to configure NetworkProfile object
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
    connection_mirror:
        description:
            - When enabled, avi mirrors all tcp fastpath connections to standby.
            - Applicable only in legacy ha mode.
            - Field introduced in 18.1.3,18.2.1.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    description:
        description:
            - User defined description for the object.
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
            - The name of the network profile.
        required: true
        type: str
    profile:
        description:
            - Networkprofileunion settings for networkprofile.
        required: true
        type: dict
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
            - Uuid of the network profile.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
  - name: Create a network profile for an UDP application
    vmware.alb.avi_networkprofile:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      name: System-UDP-Fast-Path
      profile:
        type: PROTOCOL_TYPE_UDP_FAST_PATH
        udp_fast_path_profile:
          per_pkt_loadbalance: false
          session_idle_timeout: 10
          snat: true
      tenant_ref: /api/tenant?name=admin
"""

RETURN = '''
obj:
    description: NetworkProfile (api/networkprofile) object
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
        connection_mirror=dict(type='bool',),
        description=dict(type='str',),
        labels=dict(type='list',),
        name=dict(type='str', required=True),
        profile=dict(type='dict', required=True),
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
    return avi_ansible_api(module, 'networkprofile',
                           set())


if __name__ == '__main__':
    main()
