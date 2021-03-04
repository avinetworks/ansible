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
        a_pool=dict(type='str',),
        ab_pool=dict(type='dict',),
        ab_priority=dict(type='int',),
        analytics_policy=dict(type='dict',),
        analytics_profile_ref=dict(type='str',),
        apic_epg_name=dict(type='str',),
        application_persistence_profile_ref=dict(type='str',),
        autoscale_launch_config_ref=dict(type='str',),
        autoscale_networks=dict(type='list',),
        autoscale_policy_ref=dict(type='str',),
        capacity_estimation=dict(type='bool',),
        capacity_estimation_ttfb_thresh=dict(type='int',),
        cloud_config_cksum=dict(type='str',),
        cloud_ref=dict(type='str',),
        conn_pool_properties=dict(type='dict',),
        connection_ramp_duration=dict(type='int',),
        created_by=dict(type='str',),
        default_server_port=dict(type='int',),
        delete_server_on_dns_refresh=dict(type='bool',),
        description=dict(type='str',),
        domain_name=dict(type='list',),
        east_west=dict(type='bool',),
        enable_http2=dict(type='bool',),
        enabled=dict(type='bool',),
        external_autoscale_groups=dict(type='list',),
        fail_action=dict(type='dict',),
        fewest_tasks_feedback_delay=dict(type='int',),
        graceful_disable_timeout=dict(type='int',),
        gslb_sp_enabled=dict(type='bool',),
        health_monitor_refs=dict(type='list',),
        host_check_enabled=dict(type='bool',),
        ignore_server_port=dict(type='bool',),
        inline_health_monitor=dict(type='bool',),
        ipaddrgroup_ref=dict(type='str',),
        labels=dict(type='list',),
        lb_algorithm=dict(type='str',),
        lb_algorithm_consistent_hash_hdr=dict(type='str',),
        lb_algorithm_core_nonaffinity=dict(type='int',),
        lb_algorithm_hash=dict(type='str',),
        lookup_server_by_name=dict(type='bool',),
        max_concurrent_connections_per_server=dict(type='int',),
        max_conn_rate_per_server=dict(type='dict',),
        min_health_monitors_up=dict(type='int',),
        min_servers_up=dict(type='int',),
        name=dict(type='str', required=True),
        networks=dict(type='list',),
        nsx_securitygroup=dict(type='list',),
        pki_profile_ref=dict(type='str',),
        placement_networks=dict(type='list',),
        prst_hdr_name=dict(type='str',),
        request_queue_depth=dict(type='int',),
        request_queue_enabled=dict(type='bool',),
        resolve_pool_by_dns=dict(type='bool',),
        rewrite_host_header_to_server_name=dict(type='bool',),
        rewrite_host_header_to_sni=dict(type='bool',),
        routing_pool=dict(type='bool',),
        server_auto_scale=dict(type='bool',),
        server_count=dict(type='int',),
        server_name=dict(type='str',),
        server_reselect=dict(type='dict',),
        server_timeout=dict(type='int',),
        servers=dict(type='list',),
        service_metadata=dict(type='str',),
        sni_enabled=dict(type='bool',),
        ssl_key_and_certificate_ref=dict(type='str',),
        ssl_profile_ref=dict(type='str',),
        tenant_ref=dict(type='str',),
        tier1_lr=dict(type='str',),
        url=dict(type='str',),
        use_service_port=dict(type='bool',),
        uuid=dict(type='str',),
        vrf_ref=dict(type='str',),
    )
    if not HAS_AVI:
        return sys.exit(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.')
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)

    return avi_ansible_api(module, 'pool',
                           set())

if __name__ == '__main__':
    main()

