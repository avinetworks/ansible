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
module: avi_certificatemanagementprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of CertificateManagementProfile Avi RESTful Object
description:
    - This module is used to configure CertificateManagementProfile object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
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
            - Name of the pki profile.
        required: true
        type: str
    run_script_ref:
        description:
            - Alert script config object for certificate management profile.
            - It is a reference to an object of type alertscriptconfig.
            - Field introduced in 20.1.3.
        required: true
        type: str
    script_params:
        description:
            - List of customparams.
        type: list
    script_path:
        description:
            - Field deprecated in 20.1.3.
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
    - avi
'''

EXAMPLES = """
- name: Example to create CertificateManagementProfile object
  avi_certificatemanagementprofile:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_certificatemanagementprofile
"""

RETURN = '''
obj:
    description: CertificateManagementProfile (api/certificatemanagementprofile) object
    returned: success, changed
    type: dict
'''


