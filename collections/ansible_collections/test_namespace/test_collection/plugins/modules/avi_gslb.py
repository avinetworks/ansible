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
    from avi.sdk.avi_api import ApiSession, AviCredentials
    from avi.sdk.utils.ansible_utils import (
        avi_ansible_api, avi_common_argument_spec)
    HAS_AVI = True
except ImportError:
    HAS_AVI = False

def patch_add_gslb(module, gslb_obj):
    sites = module.params['sites']
    dns_configs = module.params.get("dns_configs", None)
    if 'dns_configs' in gslb_obj:
        gslb_obj['dns_configs'].extend(dns_configs)
        gslb_obj['dns_configs'] = list({v['domain_name'] : v for v in
                                        gslb_obj['dns_configs']}.values())
    else:
        gslb_obj['dns_configs'] = dns_configs
    if sites:
        for site in sites:
            site_ips = site.get('ip_addresses', None)
            if not site_ips:
                return module.fail_json(msg=(
                        "ip_addr of site %s in a configuration is mandatory. "
                        "Please provide ip_addresses i.e. gslb site's ip." %
                        module.params['name']))
            current_gslb_sites = gslb_obj.get('sites', [])
            for current_gslb_site in current_gslb_sites:
                if current_gslb_site['name'] == site['name']:
                    for key, val in site.items():
                        if (key == 'dns_vses' and 'dns_vses' in
                                current_gslb_site):
                            current_gslb_site['dns_vses'].extend(val)
                            current_gslb_site['dns_vses'] = list(
                                {v['dns_vs_uuid']: v for v in
                                 current_gslb_site['dns_vses']}.values())
                        else:
                            current_gslb_site[key] = val
                    break
            else:
                gslb_obj['sites'].append(site)
    return gslb_obj


def patch_replace_gslb(module, gslb_obj):
    sites = module.params['sites']
    dns_configs = module.params.get("dns_configs", None)
    if dns_configs:
        gslb_obj['dns_configs'] = dns_configs
    if sites:
        for site in sites:
            site_ips = site.get('ip_addresses', None)
            if not site_ips:
                return module.fail_json(msg=(
                        "ip_addr of site %s in a configuration is mandatory. "
                        "Please provide ip_addresses i.e. gslb site's ip." %
                        module.params['name']))
            current_gslb_sites = gslb_obj.get('sites', [])
            for current_gslb_site in current_gslb_sites:
                if current_gslb_site['name'] == site['name']:
                    for key, val in site.items():
                        current_gslb_site[key] = val
    return gslb_obj


def patch_delete_gslb(module, gslb_obj):
    sites = module.params['sites']
    gslb_obj['dns_configs'] = []
    if sites:
        for site in sites:
            site_ips = site.get('ip_addresses', None)
            if not site_ips:
                return module.fail_json(msg=(
                        "ip_addr of site %s in a configuration is mandatory. "
                        "Please provide ip_addresses i.e. gslb site's ip." %
                        module.params['name']))
            current_gslb_sites = gslb_obj.get('sites', [])
            for current_gslb_site in current_gslb_sites:
                if site_ips == current_gslb_site['ip_addresses'][0]['addr']:
                    if module.params['patch_level'] == '/site':
                        gslb_obj['sites'].remove(current_gslb_site)
                    else:
                        current_gslb_site['dns_vses'] = []
    return gslb_obj


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete']),
        patch_level=dict(type='str', default='/site/dns_vses',
                         choices=['/site/dns_vses', '/site']),
        async_interval=dict(type='int',),
        clear_on_max_retries=dict(type='int',),
        client_ip_addr_group=dict(type='dict',),
        description=dict(type='str',),
        dns_configs=dict(type='list',),
        error_resync_interval=dict(type='int',),
        is_federated=dict(type='bool',),
        leader_cluster_uuid=dict(type='str', required=True),
        maintenance_mode=dict(type='bool',),
        name=dict(type='str', required=True),
        replication_policy=dict(type='dict',),
        send_interval=dict(type='int',),
        send_interval_prior_to_maintenance_mode=dict(type='int',),
        sites=dict(type='list', required=True),
        tenant_ref=dict(type='str',),
        tenant_scoped=dict(type='bool',),
        third_party_sites=dict(type='list',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        view_id=dict(type='int',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    api_method = module.params['avi_api_update_method']
    if str(api_method).lower() == 'patch':
        patch_op = module.params['avi_api_patch_op']
        # Create controller session
        api_creds = AviCredentials()
        api_creds.update_from_ansible_module(module)
        api = ApiSession.get_session(
            api_creds.controller, api_creds.username,
            password=api_creds.password, timeout=api_creds.timeout,
            tenant=api_creds.tenant, tenant_uuid=api_creds.tenant_uuid,
            token=api_creds.token, port=api_creds.port)
        # Get existing gslb objects
        rsp = api.get('gslb', api_version=api_creds.api_version)
        existing_gslb = rsp.json()
        gslb = existing_gslb['results']
        for gslb_obj in gslb:
            if (gslb_obj['leader_cluster_uuid'] ==
                    module.params['leader_cluster_uuid']):
                if str(patch_op).lower() == 'add':
                    patch_add_gslb(module, gslb_obj)
                elif str(patch_op).lower() == 'replace':
                    patch_replace_gslb(module, gslb_obj)
                elif str(patch_op).lower() == 'delete':
                    patch_delete_gslb(module, gslb_obj)
            module.params.update(gslb_obj)
            module.params.pop("patch_level")
            module.params.update(
                {
                    'avi_api_update_method': 'put',
                    'state': 'present'
                }
            )

    return avi_ansible_api(module, 'gslb',
                           set())

if __name__ == '__main__':
    main()

