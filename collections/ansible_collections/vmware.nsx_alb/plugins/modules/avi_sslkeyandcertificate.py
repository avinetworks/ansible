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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

from __future__ import (absolute_import, division, print_function)



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
        ca_certs=dict(type='list',),
        certificate=dict(type='dict', required=True),
        certificate_base64=dict(type='bool',),
        certificate_management_profile_ref=dict(type='str',),
        created_by=dict(type='str',),
        dynamic_params=dict(type='list',),
        enable_ocsp_stapling=dict(type='bool',),
        enckey_base64=dict(type='str',),
        enckey_name=dict(type='str',),
        format=dict(type='str',),
        hardwaresecuritymodulegroup_ref=dict(type='str',),
        key=dict(type='str', no_log=True,),
        key_base64=dict(type='bool',),
        key_params=dict(type='dict',),
        key_passphrase=dict(type='str', no_log=True,),
        labels=dict(type='list',),
        name=dict(type='str', required=True),
        ocsp_config=dict(type='dict',),
        ocsp_error_status=dict(type='str',),
        ocsp_responder_url_list_from_certs=dict(type='list',),
        ocsp_response_info=dict(type='dict',),
        status=dict(type='str',),
        tenant_ref=dict(type='str',),
        type=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'sslkeyandcertificate',
                           {'key_passphrase', 'key'})

if __name__ == '__main__':
    main()

