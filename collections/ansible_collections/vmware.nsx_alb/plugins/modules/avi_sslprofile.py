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
        accepted_ciphers=dict(type='str',),
        accepted_versions=dict(type='list', required=True),
        cipher_enums=dict(type='list',),
        ciphersuites=dict(type='str',),
        description=dict(type='str',),
        dhparam=dict(type='str',),
        ec_named_curve=dict(type='str',),
        enable_early_data=dict(type='bool',),
        enable_ssl_session_reuse=dict(type='bool',),
        labels=dict(type='list',),
        name=dict(type='str', required=True),
        prefer_client_cipher_ordering=dict(type='bool',),
        send_close_notify=dict(type='bool',),
        signature_algorithm=dict(type='str',),
        ssl_rating=dict(type='dict',),
        ssl_session_timeout=dict(type='int',),
        tags=dict(type='list',),
        tenant_ref=dict(type='str',),
        type=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    if not HAS_AVI:
        return sys.exit(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.')
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)

    return avi_ansible_api(module, 'sslprofile',
                           set())

if __name__ == '__main__':
    main()

