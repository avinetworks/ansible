#!/usr/bin/python3
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
from __future__ import (absolute_import, division, print_function)


DOCUMENTATION = '''
---
module: avi_scheduler
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of Scheduler Avi RESTful Object
description:
    - This module is used to configure Scheduler object
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
            - Backup configuration to be executed by this scheduler.
            - It is a reference to an object of type backupconfiguration.
        type: str
    enabled:
        description:
            - Boolean flag to set enabled.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    end_date_time:
        description:
            - Scheduler end date and time.
        type: str
    frequency:
        description:
            - Frequency at which custom scheduler will run.
            - Allowed values are 0-60.
        type: int
    frequency_unit:
        description:
            - Unit at which custom scheduler will run.
            - Enum options - SCHEDULER_FREQUENCY_UNIT_MIN, SCHEDULER_FREQUENCY_UNIT_HOUR, SCHEDULER_FREQUENCY_UNIT_DAY, SCHEDULER_FREQUENCY_UNIT_WEEK,
            - SCHEDULER_FREQUENCY_UNIT_MONTH.
        type: str
    name:
        description:
            - Name of scheduler.
        required: true
        type: str
    run_mode:
        description:
            - Scheduler run mode.
            - Enum options - RUN_MODE_PERIODIC, RUN_MODE_AT, RUN_MODE_NOW.
        type: str
    run_script_ref:
        description:
            - Control script to be executed by this scheduler.
            - It is a reference to an object of type alertscriptconfig.
        type: str
    scheduler_action:
        description:
            - Define scheduler action.
            - Enum options - SCHEDULER_ACTION_RUN_A_SCRIPT, SCHEDULER_ACTION_BACKUP.
            - Default value when not specified in API or module is interpreted by Avi Controller as SCHEDULER_ACTION_BACKUP.
        type: str
    start_date_time:
        description:
            - Scheduler start date and time.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
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
    - vmware.nsx_alb
'''

EXAMPLES = """
- name: Example to create Scheduler object
  avi_scheduler:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_scheduler
"""

RETURN = '''
obj:
    description: Scheduler (api/scheduler) object
    returned: success, changed
    type: dict
'''


