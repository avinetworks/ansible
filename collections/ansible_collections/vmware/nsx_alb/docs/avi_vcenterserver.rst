#!/usr/bin/python3
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
.. vmware.nsx_alb.avi_vcenterserver:


*****************************
vmware.nsx_alb.avi_vcenterserver
*****************************

**Module for setup of VCenterServer Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure VCenterServer object
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
                <b>cloud_ref:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Vcenter belongs to cloud.
                         - It is a reference to an object of type cloud.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>content_lib:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                            <div style="font-size: small">
                required: true
                </div>
                        </td>
            <td>
                                     - Vcenter template to create service engine.
                         - Field introduced in 20.1.1.
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
                                     - Availabilty zone where vcenter list belongs to.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tenant_ref:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Vcenter belongs to tenant.
                         - It is a reference to an object of type tenant.
                         - Field introduced in 20.1.1.
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
                                     - Vcenter config uuid.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vcenter_credentials_ref:</b>
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
                                     - Credentials to access vcenter.
                         - It is a reference to an object of type cloudconnectoruser.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vcenter_url:</b>
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
                                     - Vcenter hostname or ip address.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    - name: Example to create VCenterServer object
      avi_vcenterserver:
        controller: 10.10.25.42
        username: admin
        password: something
        state: present
        name: sample_vcenterserver


Status
------


Authors
~~~~~~~

- Gaurav Rastogi (grastogi@avinetworks.com)
- Sandeep Bandi (sbandi@avinetworks.com)



