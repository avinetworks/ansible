#!/usr/bin/python3
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
.. vmware.nsx_alb.avi_icapprofile:


*****************************
vmware.nsx_alb.avi_icapprofile
*****************************

**Module for setup of IcapProfile Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure IcapProfile object
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
                <b>allow_204:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Allow icap server to send 204 response as described in rfc 3507 section 4.5.
                         - Service engine will buffer the complete request if alllow_204 is enabled.
                         - If disabled, preview_size request body will be buffered if enable_preview is set to true, and rest of the request body will be streamed to the
                         - icap server.
                         - Field introduced in 20.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>buffer_size:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - The maximum buffer size for the http request body.
                         - If the request body exceeds this size, the request will not be checked by the icap server.
                         - In this case, the configured action will be executed and a significant log entry will be generated.
                         - Allowed values are 1-51200.
                         - Field introduced in 20.1.1.
                         - Unit is kb.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 51200.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>buffer_size_exceed_action:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Decide what should happen if the request body size exceeds the configured buffer size.
                         - If this is set to fail open, the request will not be checked by the icap server.
                         - If this is set to fail closed, the request will be rejected with 413 status code.
                         - Enum options - ICAP_FAIL_OPEN, ICAP_FAIL_CLOSED.
                         - Field introduced in 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as ICAP_FAIL_OPEN.
                                    </td>
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
                                     - The cloud where this object belongs to.
                         - This must match the cloud referenced in the pool group below.
                         - It is a reference to an object of type cloud.
                         - Field introduced in 20.1.1.
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
                                     - A description for this icap profile.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_preview:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Use the icap preview feature as described in rfc 3507 section 4.5.
                         - Field introduced in 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>fail_action:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Decide what should happen if there is a problem with the icap server like communication timeout, protocol error, pool error, etc.
                         - If this is set to fail open, the request will continue, but will create a significant log entry.
                         - If this is set to fail closed, the request will be rejected with a 500 status code.
                         - Enum options - ICAP_FAIL_OPEN, ICAP_FAIL_CLOSED.
                         - Field introduced in 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as ICAP_FAIL_OPEN.
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
                                     - Name of the icap profile.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>pool_group_ref:</b>
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
                                     - The pool group which is used to connect to icap servers.
                         - It is a reference to an object of type poolgroup.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>preview_size:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - The icap preview size as described in rfc 3507 section 4.5.
                         - This should not exceed the size supported by the icap server.
                         - If this is set to 0, only the http header will be sent to the icap server as a preview.
                         - To disable preview completely, set the enable-preview option to false.
                         - Allowed values are 0-5000.
                         - Field introduced in 20.1.1.
                         - Unit is bytes.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 5000.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>response_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Maximum time, client's request will be paused for icap processing.
                         - If this timeout is exceeded, the request to the icap server will be aborted and the configured fail action is executed.
                         - Allowed values are 50-3600000.
                         - Field introduced in 20.1.1.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 60000.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>service_uri:</b>
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
                                     - The path and query component of the icap url.
                         - Host name and port will be taken from the pool.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>slow_response_warning_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - If the icap request takes longer than this value, this request will generate a significant log entry.
                         - Allowed values are 50-3600000.
                         - Field introduced in 20.1.1.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 10000.
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
                                     - Tenant which this object belongs to.
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
                                     - Uuid of the icap profile.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vendor:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - The vendor of the icap server.
                         - Enum options - ICAP_VENDOR_GENERIC, ICAP_VENDOR_OPSWAT.
                         - Field introduced in 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as ICAP_VENDOR_OPSWAT.
                                    </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    - name: Example to create IcapProfile object
      avi_icapprofile:
        controller: 10.10.25.42
        username: admin
        password: something
        state: present
        name: sample_icapprofile


Status
------


Authors
~~~~~~~

- Gaurav Rastogi (grastogi@avinetworks.com)
- Sandeep Bandi (sbandi@avinetworks.com)



