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
        aws_access_key=dict(type='str', no_log=True,),
        aws_bucket_id=dict(type='str',),
        aws_secret_access=dict(type='str', no_log=True,),
        backup_file_prefix=dict(type='str',),
        backup_passphrase=dict(type='str', no_log=True,),
        maximum_backups_stored=dict(type='int',),
        name=dict(type='str', required=True),
        remote_directory=dict(type='str',),
        remote_hostname=dict(type='str',),
        save_local=dict(type='bool',),
        ssh_user_ref=dict(type='str',),
        tenant_ref=dict(type='str',),
        upload_to_remote_host=dict(type='bool',),
        upload_to_s3=dict(type='bool',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) or requests is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'backupconfiguration',
                           {'aws_secret_access', 'aws_access_key', 'backup_passphrase'})

if __name__ == '__main__':
    main()

