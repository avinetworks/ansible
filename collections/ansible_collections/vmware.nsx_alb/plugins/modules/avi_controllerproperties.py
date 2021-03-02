#!/usr/bin/python3
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
# Avi Version: 17.1.2
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
        allow_admin_network_updates=dict(type='bool',),
        allow_ip_forwarding=dict(type='bool',),
        allow_unauthenticated_apis=dict(type='bool',),
        allow_unauthenticated_nodes=dict(type='bool',),
        api_idle_timeout=dict(type='int',),
        api_perf_logging_threshold=dict(type='int',),
        appviewx_compat_mode=dict(type='bool',),
        async_patch_merge_period=dict(type='int',),
        async_patch_request_cleanup_duration=dict(type='int',),
        attach_ip_retry_interval=dict(type='int',),
        attach_ip_retry_limit=dict(type='int',),
        bm_use_ansible=dict(type='bool',),
        cleanup_expired_authtoken_timeout_period=dict(type='int',),
        cleanup_sessions_timeout_period=dict(type='int',),
        cloud_reconcile=dict(type='bool',),
        cluster_ip_gratuitous_arp_period=dict(type='int',),
        consistency_check_timeout_period=dict(type='int',),
        controller_resource_info_collection_period=dict(type='int',),
        crashed_se_reboot=dict(type='int',),
        dead_se_detection_timer=dict(type='int',),
        default_minimum_api_timeout=dict(type='int',),
        dns_refresh_period=dict(type='int',),
        dummy=dict(type='int',),
        edit_system_limits=dict(type='bool',),
        enable_api_sharding=dict(type='bool',),
        enable_memory_balancer=dict(type='bool',),
        fatal_error_lease_time=dict(type='int',),
        federated_datastore_cleanup_duration=dict(type='int',),
        file_object_cleanup_period=dict(type='int',),
        max_dead_se_in_grp=dict(type='int',),
        max_pcap_per_tenant=dict(type='int',),
        max_se_spawn_interval_delay=dict(type='int',),
        max_seq_attach_ip_failures=dict(type='int',),
        max_seq_vnic_failures=dict(type='int',),
        max_threads_cc_vip_bg_worker=dict(type='int',),
        permission_scoped_shared_admin_networks=dict(type='bool',),
        persistence_key_rotate_period=dict(type='int',),
        portal_request_burst_limit=dict(type='int',),
        portal_request_rate_limit=dict(type='int',),
        portal_token=dict(type='str', no_log=True,),
        process_locked_useraccounts_timeout_period=dict(type='int',),
        process_pki_profile_timeout_period=dict(type='int',),
        query_host_fail=dict(type='int',),
        resmgr_log_caching_period=dict(type='int',),
        safenet_hsm_version=dict(type='str',),
        se_create_timeout=dict(type='int',),
        se_failover_attempt_interval=dict(type='int',),
        se_from_marketplace=dict(type='str',),
        se_offline_del=dict(type='int',),
        se_spawn_retry_interval=dict(type='int',),
        se_vnic_cooldown=dict(type='int',),
        se_vnic_gc_wait_time=dict(type='int',),
        secure_channel_cleanup_timeout=dict(type='int',),
        secure_channel_controller_token_timeout=dict(type='int',),
        secure_channel_se_token_timeout=dict(type='int',),
        seupgrade_copy_pool_size=dict(type='int',),
        seupgrade_fabric_pool_size=dict(type='int',),
        seupgrade_segroup_min_dead_timeout=dict(type='int',),
        shared_ssl_certificates=dict(type='bool',),
        ssl_certificate_expiry_warning_days=dict(type='list',),
        unresponsive_se_reboot=dict(type='int',),
        upgrade_dns_ttl=dict(type='int',),
        upgrade_fat_se_lease_time=dict(type='int',),
        upgrade_lease_time=dict(type='int',),
        upgrade_se_per_vs_scale_ops_txn_time=dict(type='int',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vnic_op_fail_time=dict(type='int',),
        vs_apic_scaleout_timeout=dict(type='int',),
        vs_awaiting_se_timeout=dict(type='int',),
        vs_key_rotate_period=dict(type='int',),
        vs_scaleout_ready_check_interval=dict(type='int',),
        vs_se_attach_ip_fail=dict(type='int',),
        vs_se_bootup_fail=dict(type='int',),
        vs_se_create_fail=dict(type='int',),
        vs_se_ping_fail=dict(type='int',),
        vs_se_vnic_fail=dict(type='int',),
        vs_se_vnic_ip_fail=dict(type='int',),
        warmstart_se_reconnect_wait_time=dict(type='int',),
        warmstart_vs_resync_wait_time=dict(type='int',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'controllerproperties',
                           {'portal_token'})

if __name__ == '__main__':
    main()

