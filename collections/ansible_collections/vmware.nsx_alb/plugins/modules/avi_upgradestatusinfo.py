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
        after_reboot_rollback_fnc=dict(type='str',),
        after_reboot_task_name=dict(type='str',),
        clean=dict(type='bool',),
        duration=dict(type='int',),
        enable_patch_rollback=dict(type='bool',),
        enable_rollback=dict(type='bool',),
        end_time=dict(type='str',),
        enqueue_time=dict(type='str',),
        history=dict(type='list',),
        image_path=dict(type='str',),
        image_ref=dict(type='str',),
        name=dict(type='str',),
        node_type=dict(type='str',),
        obj_cloud_ref=dict(type='str',),
        obj_state=dict(type='dict',),
        params=dict(type='dict',),
        patch_image_path=dict(type='str',),
        patch_image_ref=dict(type='str',),
        patch_list=dict(type='list',),
        patch_reboot=dict(type='bool',),
        patch_version=dict(type='str',),
        prev_image_path=dict(type='str',),
        prev_patch_image_path=dict(type='str',),
        previous_image_ref=dict(type='str',),
        previous_patch_image_ref=dict(type='str',),
        previous_patch_list=dict(type='list',),
        previous_patch_version=dict(type='str',),
        previous_version=dict(type='str',),
        progress=dict(type='int',),
        se_patch_image_path=dict(type='str',),
        se_patch_image_ref=dict(type='str',),
        se_upgrade_events=dict(type='list',),
        seg_params=dict(type='dict',),
        seg_status=dict(type='dict',),
        start_time=dict(type='str',),
        system=dict(type='bool',),
        tasks_completed=dict(type='int',),
        tenant_ref=dict(type='str',),
        total_tasks=dict(type='int',),
        upgrade_events=dict(type='list',),
        upgrade_ops=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        version=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'upgradestatusinfo',
                           set())

if __name__ == '__main__':
    main()

