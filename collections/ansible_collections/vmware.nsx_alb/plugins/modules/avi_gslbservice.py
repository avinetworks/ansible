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
        application_persistence_profile_ref=dict(type='str',),
        controller_health_status_enabled=dict(type='bool',),
        created_by=dict(type='str',),
        description=dict(type='str',),
        domain_names=dict(type='list', required=True),
        down_response=dict(type='dict',),
        enabled=dict(type='bool',),
        groups=dict(type='list', required=True),
        health_monitor_refs=dict(type='list',),
        health_monitor_scope=dict(type='str',),
        hm_off=dict(type='bool',),
        is_federated=dict(type='bool',),
        labels=dict(type='list',),
        min_members=dict(type='int',),
        name=dict(type='str', required=True),
        num_dns_ip=dict(type='int',),
        pool_algorithm=dict(type='str',),
        resolve_cname=dict(type='bool',),
        site_persistence_enabled=dict(type='bool',),
        tenant_ref=dict(type='str',),
        ttl=dict(type='int',),
        url=dict(type='str',),
        use_edns_client_subnet=dict(type='bool',),
        uuid=dict(type='str',),
        wildcard_match=dict(type='bool',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'gslbservice',
                           set())

if __name__ == '__main__':
    main()

