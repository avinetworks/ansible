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
.. vmware.nsx_alb.avi_tenant:


*****************************
vmware.nsx_alb.avi_tenant
*****************************

**Module for setup of Tenant Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure Tenant object
- more examples at U(https://github.com/avinetworks/devops)


Requirements
------------
The below requirements are needed on the host that executes this module.

- avisdk


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>config_settings:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Tenantconfiguration settings for tenant.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>created_by:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Creator of this tenant.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>description:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - User defined description for the object.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>local:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Boolean flag to set local.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>name:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                            <div style="font-size: small">
                required: true
                </div>
                        </td>
            <td>
                                     - Name of the object.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>suggested_object_labels:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Suggestive pool of key value pairs for recommending assignment of labels to objects in the user interface.
                         - Every entry is unique in both key and value.
                         - Field introduced in 20.1.2.
                         - Maximum of 256 items allowed.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>url:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Avi controller URL of the object.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>uuid:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Unique object identifier of the object.
                                    </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    
  - name: Create Tenant using Service Engines in provider mode
    avi_tenant:
      controller: '{{ controller }}'
      password: '{{ password }}'
      username: '{{ username }}'
      config_settings:
        se_in_provider_context: false
        tenant_access_to_provider_se: true
        tenant_vrf: false
      description: VCenter, Open Stack, AWS Virtual services
      local: true
      name: Demo



Status
------


Authors
~~~~~~~

- Gaurav Rastogi (grastogi@avinetworks.com)
- Sandeep Bandi (sbandi@avinetworks.com)



