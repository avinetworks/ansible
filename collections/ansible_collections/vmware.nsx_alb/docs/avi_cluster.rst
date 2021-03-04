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
module: avi_cluster
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of Cluster Avi RESTful Object
description:
    - This module is used to configure Cluster object
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
    name:
        description:
            - Name of the object.
        required: true
        type: str
    nodes:
        description:
            - Minimum of 1 items required.
            - Maximum of 7 items allowed.
        required: true
        type: list
    rejoin_nodes_automatically:
        description:
            - Re-join cluster nodes automatically in the event one of the node is reset to factory.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
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
    virtual_ip:
        description:
            - A virtual ip address.
            - This ip address will be dynamically reconfigured so that it always is the ip of the cluster leader.
        type: dict
extends_documentation_fragment:
    - vmware.nsx_alb
'''

EXAMPLES = """
- name: Example to create Cluster object
  avi_cluster:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_cluster
"""

RETURN = '''
obj:
    description: Cluster (api/cluster) object
    returned: success, changed
    type: dict
'''


