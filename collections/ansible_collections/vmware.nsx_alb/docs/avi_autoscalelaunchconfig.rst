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
module: avi_autoscalelaunchconfig
author: Chaitanya Deshpande (@chaitanyaavi) <chaitanya.deshpande@avinetworks.com>
short_description: Module for setup of AutoScaleLaunchConfig Avi RESTful Object
description:
    - This module is used to configure AutoScaleLaunchConfig object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.6"
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
    description:
        description:
            - User defined description for the object.
        type: str
    image_id:
        description:
            - Unique id of the amazon machine image (ami)  or openstack vm id.
        type: str
    labels:
        description:
            - Key value pairs for granular object access control.
            - Also allows for classification and tagging of similar objects.
            - Field introduced in 20.1.2.
            - Maximum of 4 items allowed.
        type: list
    mesos:
        description:
            - Autoscalemesossettings settings for autoscalelaunchconfig.
        type: dict
    name:
        description:
            - Name of the object.
        required: true
        type: str
    openstack:
        description:
            - Autoscaleopenstacksettings settings for autoscalelaunchconfig.
        type: dict
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    use_external_asg:
        description:
            - If set to true, serverautoscalepolicy will use the autoscaling group (external_autoscaling_groups) from pool to perform scale up and scale down.
            - Pool should have single autoscaling group configured.
            - Field introduced in 17.2.3.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    uuid:
        description:
            - Unique object identifier of the object.
        type: str
extends_documentation_fragment:
    - vmware.nsx_alb
'''

EXAMPLES = """
  - name: Create an Autoscale Launch configuration.
    avi_autoscalelaunchconfig:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      image_id: default
      name: default-autoscalelaunchconfig
      tenant_ref: /api/tenant?name=admin
"""

RETURN = '''
obj:
    description: AutoScaleLaunchConfig (api/autoscalelaunchconfig) object
    returned: success, changed
    type: dict
'''


