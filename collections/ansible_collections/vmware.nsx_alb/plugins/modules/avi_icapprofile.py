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
        allow_204=dict(type='bool',),
        buffer_size=dict(type='int',),
        buffer_size_exceed_action=dict(type='str',),
        cloud_ref=dict(type='str',),
        description=dict(type='str',),
        enable_preview=dict(type='bool',),
        fail_action=dict(type='str',),
        name=dict(type='str', required=True),
        pool_group_ref=dict(type='str', required=True),
        preview_size=dict(type='int',),
        response_timeout=dict(type='int',),
        service_uri=dict(type='str', required=True),
        slow_response_warning_threshold=dict(type='int',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vendor=dict(type='str',),
    )
    if not HAS_AVI:
        return sys.exit(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.')
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)

    return avi_ansible_api(module, 'icapprofile',
                           set())

if __name__ == '__main__':
    main()

