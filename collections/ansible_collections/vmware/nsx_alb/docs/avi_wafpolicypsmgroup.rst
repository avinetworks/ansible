#!/usr/bin/python3
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
.. vmware.nsx_alb.avi_wafpolicypsmgroup:


*****************************
vmware.nsx_alb.avi_wafpolicypsmgroup
*****************************

**Module for setup of WafPolicyPSMGroup Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure WafPolicyPSMGroup object
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
                <b>description:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Free-text comment about this group.
                         - Field introduced in 18.2.3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable or disable this waf rule group.
                         - Field introduced in 18.2.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hit_action:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - If a rule in this group matches the match_value pattern, this action will be executed.
                         - Allowed actions are waf_action_no_op and waf_action_allow_parameter.
                         - Enum options - WAF_ACTION_NO_OP, WAF_ACTION_BLOCK, WAF_ACTION_ALLOW_PARAMETER.
                         - Field introduced in 18.2.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as WAF_ACTION_ALLOW_PARAMETER.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>is_learning_group:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - This field indicates that this group is used for learning.
                         - Field introduced in 18.2.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>labels:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Key value pairs for granular object access control.
                         - Also allows for classification and tagging of similar objects.
                         - Field introduced in 20.1.2.
                         - Maximum of 4 items allowed.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>locations:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Positive security model locations.
                         - These are used to partition the application name space.
                         - Field introduced in 18.2.3.
                         - Maximum of 16384 items allowed.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>miss_action:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - If a rule in this group does not match the match_value pattern, this action will be executed.
                         - Allowed actions are waf_action_no_op and waf_action_block.
                         - Enum options - WAF_ACTION_NO_OP, WAF_ACTION_BLOCK, WAF_ACTION_ALLOW_PARAMETER.
                         - Field introduced in 18.2.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as WAF_ACTION_NO_OP.
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
                                     - User defined name of the group.
                         - Field introduced in 18.2.3.
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
                                     - Tenant that this object belongs to.
                         - It is a reference to an object of type tenant.
                         - Field introduced in 18.2.3.
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
                                     - Uuid of this object.
                         - Field introduced in 18.2.3.
                                    </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    - name: Example to create WafPolicyPSMGroup object
      avi_wafpolicypsmgroup:
        controller: 10.10.25.42
        username: admin
        password: something
        state: present
        name: sample_wafpolicypsmgroup


Status
------


Authors
~~~~~~~

- Gaurav Rastogi (grastogi@avinetworks.com)
- Sandeep Bandi (sbandi@avinetworks.com)



