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
        apdex_response_threshold=dict(type='int',),
        apdex_response_tolerated_factor=dict(type='float',),
        apdex_rtt_threshold=dict(type='int',),
        apdex_rtt_tolerated_factor=dict(type='float',),
        apdex_rum_threshold=dict(type='int',),
        apdex_rum_tolerated_factor=dict(type='float',),
        apdex_server_response_threshold=dict(type='int',),
        apdex_server_response_tolerated_factor=dict(type='float',),
        apdex_server_rtt_threshold=dict(type='int',),
        apdex_server_rtt_tolerated_factor=dict(type='float',),
        client_log_config=dict(type='dict',),
        client_log_streaming_config=dict(type='dict',),
        conn_lossy_ooo_threshold=dict(type='int',),
        conn_lossy_timeo_rexmt_threshold=dict(type='int',),
        conn_lossy_total_rexmt_threshold=dict(type='int',),
        conn_lossy_zero_win_size_event_threshold=dict(type='int',),
        conn_server_lossy_ooo_threshold=dict(type='int',),
        conn_server_lossy_timeo_rexmt_threshold=dict(type='int',),
        conn_server_lossy_total_rexmt_threshold=dict(type='int',),
        conn_server_lossy_zero_win_size_event_threshold=dict(type='int',),
        description=dict(type='str',),
        disable_ondemand_metrics=dict(type='bool',),
        disable_se_analytics=dict(type='bool',),
        disable_server_analytics=dict(type='bool',),
        disable_vs_analytics=dict(type='bool',),
        enable_adaptive_config=dict(type='bool',),
        enable_advanced_analytics=dict(type='bool',),
        enable_ondemand_metrics=dict(type='bool',),
        enable_se_analytics=dict(type='bool',),
        enable_server_analytics=dict(type='bool',),
        enable_vs_analytics=dict(type='bool',),
        exclude_client_close_before_request_as_error=dict(type='bool',),
        exclude_dns_policy_drop_as_significant=dict(type='bool',),
        exclude_gs_down_as_error=dict(type='bool',),
        exclude_http_error_codes=dict(type='list',),
        exclude_invalid_dns_domain_as_error=dict(type='bool',),
        exclude_invalid_dns_query_as_error=dict(type='bool',),
        exclude_issuer_revoked_ocsp_responses_as_error=dict(type='bool',),
        exclude_no_dns_record_as_error=dict(type='bool',),
        exclude_no_valid_gs_member_as_error=dict(type='bool',),
        exclude_persistence_change_as_error=dict(type='bool',),
        exclude_revoked_ocsp_responses_as_error=dict(type='bool',),
        exclude_server_dns_error_as_error=dict(type='bool',),
        exclude_server_tcp_reset_as_error=dict(type='bool',),
        exclude_sip_error_codes=dict(type='list',),
        exclude_stale_ocsp_responses_as_error=dict(type='bool',),
        exclude_syn_retransmit_as_error=dict(type='bool',),
        exclude_tcp_reset_as_error=dict(type='bool',),
        exclude_unavailable_ocsp_responses_as_error=dict(type='bool',),
        exclude_unsupported_dns_query_as_error=dict(type='bool',),
        healthscore_max_server_limit=dict(type='int',),
        hs_event_throttle_window=dict(type='int',),
        hs_max_anomaly_penalty=dict(type='int',),
        hs_max_resources_penalty=dict(type='int',),
        hs_max_security_penalty=dict(type='int',),
        hs_min_dos_rate=dict(type='int',),
        hs_performance_boost=dict(type='int',),
        hs_pscore_traffic_threshold_l4_client=dict(type='float',),
        hs_pscore_traffic_threshold_l4_server=dict(type='float',),
        hs_security_certscore_expired=dict(type='float',),
        hs_security_certscore_gt30d=dict(type='float',),
        hs_security_certscore_le07d=dict(type='float',),
        hs_security_certscore_le30d=dict(type='float',),
        hs_security_chain_invalidity_penalty=dict(type='float',),
        hs_security_cipherscore_eq000b=dict(type='float',),
        hs_security_cipherscore_ge128b=dict(type='float',),
        hs_security_cipherscore_lt128b=dict(type='float',),
        hs_security_encalgo_score_none=dict(type='float',),
        hs_security_encalgo_score_rc4=dict(type='float',),
        hs_security_hsts_penalty=dict(type='float',),
        hs_security_nonpfs_penalty=dict(type='float',),
        hs_security_ocsp_revoked_score=dict(type='float',),
        hs_security_selfsignedcert_penalty=dict(type='float',),
        hs_security_ssl30_score=dict(type='float',),
        hs_security_tls10_score=dict(type='float',),
        hs_security_tls11_score=dict(type='float',),
        hs_security_tls12_score=dict(type='float',),
        hs_security_tls13_score=dict(type='float',),
        hs_security_weak_signature_algo_penalty=dict(type='float',),
        labels=dict(type='list',),
        name=dict(type='str', required=True),
        ondemand_metrics_idle_timeout=dict(type='int',),
        ranges=dict(type='list',),
        resp_code_block=dict(type='list',),
        sensitive_log_profile=dict(type='dict',),
        sip_log_depth=dict(type='int',),
        tenant_ref=dict(type='str',),
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

    return avi_ansible_api(module, 'analyticsprofile',
                           set())

if __name__ == '__main__':
    main()

