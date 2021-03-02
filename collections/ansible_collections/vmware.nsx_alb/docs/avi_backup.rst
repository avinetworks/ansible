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


DOCUMENTATION = '''
---
module: avi_backup
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of Backup Avi RESTful Object
description:
    - This module is used to configure Backup object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.4"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        version_added: "2.5"
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        version_added: "2.5"
        choices: ["add", "replace", "delete"]
        type: str
    backup_config_ref:
        description:
            - Backupconfiguration information.
            - It is a reference to an object of type backupconfiguration.
        type: str
    file_name:
        description:
            - The file name of backup.
        required: true
        type: str
    local_file_url:
        description:
            - Url to download the backup file.
        type: str
    remote_file_url:
        description:
            - Url to download the backup file.
        type: str
    scheduler_ref:
        description:
            - Scheduler information.
            - It is a reference to an object of type scheduler.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    timestamp:
        description:
            - Unix timestamp of when the backup file is created.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Unique object identifier of the object.
        type: str
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create Backup object
  avi_backup:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_backup
"""

RETURN = '''
obj:
    description: Backup (api/backup) object
    returned: success, changed
    type: dict
'''


