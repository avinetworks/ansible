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
        admin_auth_configuration=dict(type='dict',),
        common_criteria_mode=dict(type='bool',),
        default_license_tier=dict(type='str',),
        dns_configuration=dict(type='dict',),
        dns_virtualservice_refs=dict(type='list',),
        docker_mode=dict(type='bool',),
        email_configuration=dict(type='dict',),
        enable_cors=dict(type='bool',),
        fips_mode=dict(type='bool',),
        global_tenant_config=dict(type='dict',),
        linux_configuration=dict(type='dict',),
        mgmt_ip_access_control=dict(type='dict',),
        ntp_configuration=dict(type='dict',),
        portal_configuration=dict(type='dict',),
        proxy_configuration=dict(type='dict',),
        secure_channel_configuration=dict(type='dict',),
        snmp_configuration=dict(type='dict',),
        ssh_ciphers=dict(type='list',),
        ssh_hmacs=dict(type='list',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        welcome_workflow_complete=dict(type='bool',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'systemconfiguration',
                           set())

if __name__ == '__main__':
    main()

