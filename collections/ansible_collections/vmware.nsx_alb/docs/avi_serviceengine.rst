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
module: avi_serviceengine
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of ServiceEngine Avi RESTful Object
description:
    - This module is used to configure ServiceEngine object
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
    availability_zone:
        description:
            - Availability_zone of serviceengine.
        type: str
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
        type: str
    container_mode:
        description:
            - Boolean flag to set container_mode.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    container_type:
        description:
            - Enum options - CONTAINER_TYPE_BRIDGE, CONTAINER_TYPE_HOST, CONTAINER_TYPE_HOST_DPDK.
            - Default value when not specified in API or module is interpreted by Avi Controller as CONTAINER_TYPE_HOST.
        type: str
    controller_created:
        description:
            - Boolean flag to set controller_created.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    controller_ip:
        description:
            - Controller_ip of serviceengine.
        type: str
    data_vnics:
        description:
            - List of vnic.
        type: list
    enable_state:
        description:
            - Inorder to disable se set this field appropriately.
            - Enum options - SE_STATE_ENABLED, SE_STATE_DISABLED_FOR_PLACEMENT, SE_STATE_DISABLED, SE_STATE_DISABLED_FORCE.
            - Default value when not specified in API or module is interpreted by Avi Controller as SE_STATE_ENABLED.
        type: str
    flavor:
        description:
            - Flavor of serviceengine.
        type: str
    host_ref:
        description:
            - It is a reference to an object of type vimgrhostruntime.
        type: str
    hypervisor:
        description:
            - Enum options - DEFAULT, VMWARE_ESX, KVM, VMWARE_VSAN, XEN.
        type: str
    mgmt_vnic:
        description:
            - Vnic settings for serviceengine.
        type: dict
    name:
        description:
            - Name of the object.
            - Default value when not specified in API or module is interpreted by Avi Controller as VM name unknown.
        type: str
    resources:
        description:
            - Seresources settings for serviceengine.
        type: dict
    se_group_ref:
        description:
            - It is a reference to an object of type serviceenginegroup.
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
- name: Example to create ServiceEngine object
  avi_serviceengine:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_serviceengine
"""

RETURN = '''
obj:
    description: ServiceEngine (api/serviceengine) object
    returned: success, changed
    type: dict
'''


