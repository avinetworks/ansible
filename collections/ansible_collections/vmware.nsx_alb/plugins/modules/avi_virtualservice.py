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
        active_standby_se_tag=dict(type='str',),
        advertise_down_vs=dict(type='bool',),
        allow_invalid_client_cert=dict(type='bool',),
        analytics_policy=dict(type='dict',),
        analytics_profile_ref=dict(type='str',),
        apic_contract_graph=dict(type='str',),
        application_profile_ref=dict(type='str',),
        auto_allocate_floating_ip=dict(type='bool',),
        auto_allocate_ip=dict(type='bool',),
        availability_zone=dict(type='str',),
        avi_allocated_fip=dict(type='bool',),
        avi_allocated_vip=dict(type='bool',),
        azure_availability_set=dict(type='str',),
        bot_policy_ref=dict(type='str',),
        bulk_sync_kvcache=dict(type='bool',),
        client_auth=dict(type='dict',),
        close_client_conn_on_config_update=dict(type='bool',),
        cloud_config_cksum=dict(type='str',),
        cloud_ref=dict(type='str',),
        cloud_type=dict(type='str',),
        connections_rate_limit=dict(type='dict',),
        content_rewrite=dict(type='dict',),
        created_by=dict(type='str',),
        delay_fairness=dict(type='bool',),
        description=dict(type='str',),
        discovered_network_ref=dict(type='list',),
        discovered_networks=dict(type='list',),
        discovered_subnet=dict(type='list',),
        dns_info=dict(type='list',),
        dns_policies=dict(type='list',),
        east_west_placement=dict(type='bool',),
        enable_autogw=dict(type='bool',),
        enable_rhi=dict(type='bool',),
        enable_rhi_snat=dict(type='bool',),
        enabled=dict(type='bool',),
        error_page_profile_ref=dict(type='str',),
        floating_ip=dict(type='dict',),
        floating_subnet_uuid=dict(type='str',),
        flow_dist=dict(type='str',),
        flow_label_type=dict(type='str',),
        fqdn=dict(type='str',),
        host_name_xlate=dict(type='str',),
        http_policies=dict(type='list',),
        icap_request_profile_refs=dict(type='list',),
        ign_pool_net_reach=dict(type='bool',),
        ip_address=dict(type='dict',),
        ipam_network_subnet=dict(type='dict',),
        jwt_config=dict(type='dict',),
        l4_policies=dict(type='list',),
        labels=dict(type='list',),
        limit_doser=dict(type='bool',),
        max_cps_per_client=dict(type='int',),
        microservice_ref=dict(type='str',),
        min_pools_up=dict(type='int',),
        name=dict(type='str', required=True),
        network_profile_ref=dict(type='str',),
        network_ref=dict(type='str',),
        network_security_policy_ref=dict(type='str',),
        nsx_securitygroup=dict(type='list',),
        performance_limits=dict(type='dict',),
        pool_group_ref=dict(type='str',),
        pool_ref=dict(type='str',),
        port_uuid=dict(type='str',),
        remove_listening_port_on_vs_down=dict(type='bool',),
        requests_rate_limit=dict(type='dict',),
        saml_sp_config=dict(type='dict',),
        scaleout_ecmp=dict(type='bool',),
        se_group_ref=dict(type='str',),
        security_policy_ref=dict(type='str',),
        server_network_profile_ref=dict(type='str',),
        service_metadata=dict(type='str',),
        service_pool_select=dict(type='list',),
        services=dict(type='list',),
        sideband_profile=dict(type='dict',),
        snat_ip=dict(type='list',),
        sp_pool_refs=dict(type='list',),
        ssl_key_and_certificate_refs=dict(type='list',),
        ssl_profile_ref=dict(type='str',),
        ssl_profile_selectors=dict(type='list',),
        ssl_sess_cache_avg_size=dict(type='int',),
        sso_policy=dict(type='dict',),
        sso_policy_ref=dict(type='str',),
        static_dns_records=dict(type='list',),
        subnet=dict(type='dict',),
        subnet_uuid=dict(type='str',),
        tenant_ref=dict(type='str',),
        test_se_datastore_level_1_ref=dict(type='str',),
        topology_policies=dict(type='list',),
        traffic_clone_profile_ref=dict(type='str',),
        traffic_enabled=dict(type='bool',),
        type=dict(type='str',),
        url=dict(type='str',),
        use_bridge_ip_as_vip=dict(type='bool',),
        use_vip_as_snat=dict(type='bool',),
        uuid=dict(type='str',),
        vh_domain_name=dict(type='list',),
        vh_matches=dict(type='list',),
        vh_parent_vs_uuid=dict(type='str',),
        vh_type=dict(type='str',),
        vip=dict(type='list',),
        vrf_context_ref=dict(type='str',),
        vs_datascripts=dict(type='list',),
        vsvip_cloud_config_cksum=dict(type='str',),
        vsvip_ref=dict(type='str',),
        waf_policy_ref=dict(type='str',),
        weight=dict(type='int',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'virtualservice',
                           set())

if __name__ == '__main__':
    main()

