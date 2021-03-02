#!/usr/bin/python3
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
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
        delay_for_server_garbage_collection=dict(type='int',),
        description=dict(type='str',),
        intelligent_autoscale=dict(type='bool',),
        intelligent_scalein_margin=dict(type='int',),
        intelligent_scaleout_margin=dict(type='int',),
        labels=dict(type='list',),
        max_scalein_adjustment_step=dict(type='int',),
        max_scaleout_adjustment_step=dict(type='int',),
        max_size=dict(type='int',),
        min_size=dict(type='int',),
        name=dict(type='str', required=True),
        scalein_alertconfig_refs=dict(type='list',),
        scalein_cooldown=dict(type='int',),
        scaleout_alertconfig_refs=dict(type='list',),
        scaleout_cooldown=dict(type='int',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        use_predicted_load=dict(type='bool',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'serverautoscalepolicy',
                           set())

if __name__ == '__main__':
    main()

