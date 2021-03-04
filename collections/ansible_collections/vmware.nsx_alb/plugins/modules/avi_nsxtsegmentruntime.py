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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


import sys
from ansible.module_utils.basic import AnsibleModule
try:
    from avi.sdk.utils.ansible_utils import avi_common_argument_spec
    from avi.sdk.utils.ansible_utils import (
        avi_ansible_api, avi_common_argument_spec)
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        cloud_ref=dict(type='str',),
        dhcp6_ranges=dict(type='list',),
        dhcp_enabled=dict(type='bool',),
        dhcp_ranges=dict(type='list',),
        name=dict(type='str',),
        nw_name=dict(type='str',),
        nw_ref=dict(type='str',),
        opaque_network_id=dict(type='str',),
        segment_gw=dict(type='str',),
        segment_gw6=dict(type='str',),
        segment_id=dict(type='str',),
        segname=dict(type='str',),
        subnet=dict(type='str',),
        subnet6=dict(type='str',),
        tenant_ref=dict(type='str',),
        tier1_id=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vrf_context_ref=dict(type='str',),
    )
    if not HAS_AVI:
        return sys.exit(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.')
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)

    return avi_ansible_api(module, 'nsxtsegmentruntime',
                           set())

if __name__ == '__main__':
    main()

