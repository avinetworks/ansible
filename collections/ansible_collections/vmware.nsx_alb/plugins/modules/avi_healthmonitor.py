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
        allow_duplicate_monitors=dict(type='bool',),
        authentication=dict(type='dict',),
        description=dict(type='str',),
        disable_quickstart=dict(type='bool',),
        dns_monitor=dict(type='dict',),
        external_monitor=dict(type='dict',),
        failed_checks=dict(type='int',),
        http_monitor=dict(type='dict',),
        https_monitor=dict(type='dict',),
        imap_monitor=dict(type='dict',),
        imaps_monitor=dict(type='dict',),
        is_federated=dict(type='bool',),
        monitor_port=dict(type='int',),
        name=dict(type='str', required=True),
        pop3_monitor=dict(type='dict',),
        pop3s_monitor=dict(type='dict',),
        radius_monitor=dict(type='dict',),
        receive_timeout=dict(type='int',),
        send_interval=dict(type='int',),
        sip_monitor=dict(type='dict',),
        smtp_monitor=dict(type='dict',),
        smtps_monitor=dict(type='dict',),
        successful_checks=dict(type='int',),
        tcp_monitor=dict(type='dict',),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
        udp_monitor=dict(type='dict',),
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

    return avi_ansible_api(module, 'healthmonitor',
                           set())

if __name__ == '__main__':
    main()

