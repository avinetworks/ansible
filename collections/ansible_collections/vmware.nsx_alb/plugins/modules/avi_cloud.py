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
        apic_configuration=dict(type='dict',),
        apic_mode=dict(type='bool',),
        autoscale_polling_interval=dict(type='int',),
        aws_configuration=dict(type='dict',),
        azure_configuration=dict(type='dict',),
        cloudstack_configuration=dict(type='dict',),
        custom_tags=dict(type='list',),
        dhcp_enabled=dict(type='bool',),
        dns_provider_ref=dict(type='str',),
        dns_resolution_on_se=dict(type='bool',),
        docker_configuration=dict(type='dict',),
        east_west_dns_provider_ref=dict(type='str',),
        east_west_ipam_provider_ref=dict(type='str',),
        enable_vip_on_all_interfaces=dict(type='bool',),
        enable_vip_static_routes=dict(type='bool',),
        gcp_configuration=dict(type='dict',),
        ip6_autocfg_enabled=dict(type='bool',),
        ipam_provider_ref=dict(type='str',),
        license_tier=dict(type='str',),
        license_type=dict(type='str',),
        linuxserver_configuration=dict(type='dict',),
        mesos_configuration=dict(type='dict',),
        mtu=dict(type='int',),
        name=dict(type='str', required=True),
        nsx_configuration=dict(type='dict',),
        nsxt_configuration=dict(type='dict',),
        obj_name_prefix=dict(type='str',),
        openstack_configuration=dict(type='dict',),
        oshiftk8s_configuration=dict(type='dict',),
        prefer_static_routes=dict(type='bool',),
        proxy_configuration=dict(type='dict',),
        rancher_configuration=dict(type='dict',),
        se_group_template_ref=dict(type='str',),
        state_based_dns_registration=dict(type='bool',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vca_configuration=dict(type='dict',),
        vcenter_configuration=dict(type='dict',),
        vtype=dict(type='str', required=True),
    )
    if not HAS_AVI:
        return sys.exit(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.')
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)

    return avi_ansible_api(module, 'cloud',
                           set())

if __name__ == '__main__':
    main()

