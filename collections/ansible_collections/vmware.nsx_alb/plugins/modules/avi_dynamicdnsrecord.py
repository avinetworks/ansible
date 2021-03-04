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
        algorithm=dict(type='str',),
        cname=dict(type='dict',),
        delegated=dict(type='bool',),
        description=dict(type='str',),
        dns_vs_uuid=dict(type='str',),
        fqdn=dict(type='str',),
        ip6_address=dict(type='list',),
        ip_address=dict(type='list',),
        metadata=dict(type='str',),
        mx_records=dict(type='list',),
        name=dict(type='str',),
        ns=dict(type='list',),
        num_records_in_response=dict(type='int',),
        service_locators=dict(type='list',),
        tenant_ref=dict(type='str',),
        ttl=dict(type='int',),
        txt_records=dict(type='list',),
        type=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        wildcard_match=dict(type='bool',),
    )
    if not HAS_AVI:
        return sys.exit(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.')
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)

    return avi_ansible_api(module, 'dynamicdnsrecord',
                           set())

if __name__ == '__main__':
    main()

