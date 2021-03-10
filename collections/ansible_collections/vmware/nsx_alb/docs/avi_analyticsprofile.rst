.. vmware.nsx_alb.avi_analyticsprofile:


*****************************
vmware.nsx_alb.avi_analyticsprofile
*****************************

**Module for setup of AnalyticsProfile Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure AnalyticsProfile object
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
            <th> width="100%">Comments</th>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <div style="font-size: small">
                    default: present
                    choices: ["absent", "present"]
                </div>
            </td>
            <td>
                <div style="font-size: small">
                    - The state that should be applied on the entity.
                </div>
                <br>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_api_update_method</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <div style="font-size: small">
                    default: put
                    choices: ["put", "patch"]
                </div>
            </td>
            <td>
                <div style="font-size: small">
                    - Default method for object update is HTTP PUT.
                </div><br>
                <div style="font-size: small">
                    - Setting to patch will override that behavior to use HTTP PATCH.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_api_patch_op</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <div style="font-size: small">
                    choices: ["add", "replace", "delete"]
                </div>
            </td>
            <td>
                <div style="font-size: small">
                    - Patch operation to use when using avi_api_update_method as patch.
                </div>
            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>apdex_response_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - If a client receives an http response in less than the satisfactory latency threshold, the request is considered satisfied.
                </div><br>
                                <div style="font-size: small">
                 - It is considered tolerated if it is not satisfied and less than tolerated latency factor multiplied by the satisfactory latency threshold.
                </div><br>
                                <div style="font-size: small">
                 - Greater than this number and the client's request is considered frustrated.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-30000.
                </div><br>
                                <div style="font-size: small">
                 - Unit is milliseconds.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 500) edition, essentials(allowed values- 500) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 500.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>apdex_response_tolerated_factor:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Client tolerated response latency factor.
                </div><br>
                                <div style="font-size: small">
                 - Client must receive a response within this factor times the satisfactory threshold (apdex_response_threshold) to be considered tolerated.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-1000.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 4) edition, essentials(allowed values- 4) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>apdex_rtt_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Satisfactory client to avi round trip time(rtt).
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-2000.
                </div><br>
                                <div style="font-size: small">
                 - Unit is milliseconds.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 250) edition, essentials(allowed values- 250) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 250.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>apdex_rtt_tolerated_factor:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Tolerated client to avi round trip time(rtt) factor.
                </div><br>
                                <div style="font-size: small">
                 - It is a multiple of apdex_rtt_tolerated_factor.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-1000.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 4) edition, essentials(allowed values- 4) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>apdex_rum_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - If a client is able to load a page in less than the satisfactory latency threshold, the pageload is considered satisfied.
                </div><br>
                                <div style="font-size: small">
                 - It is considered tolerated if it is greater than satisfied but less than the tolerated latency multiplied by satisifed latency.
                </div><br>
                                <div style="font-size: small">
                 - Greater than this number and the client's request is considered frustrated.
                </div><br>
                                <div style="font-size: small">
                 - A pageload includes the time for dns lookup, download of all http objects, and page render time.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-30000.
                </div><br>
                                <div style="font-size: small">
                 - Unit is milliseconds.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 5000) edition, essentials(allowed values- 5000) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 5000.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>apdex_rum_tolerated_factor:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Virtual service threshold factor for tolerated page load time (plt) as multiple of apdex_rum_threshold.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-1000.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 4) edition, essentials(allowed values- 4) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>apdex_server_response_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - A server http response is considered satisfied if latency is less than the satisfactory latency threshold.
                </div><br>
                                <div style="font-size: small">
                 - The response is considered tolerated when it is greater than satisfied but less than the tolerated latency factor * s_latency.
                </div><br>
                                <div style="font-size: small">
                 - Greater than this number and the server response is considered frustrated.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-30000.
                </div><br>
                                <div style="font-size: small">
                 - Unit is milliseconds.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 400) edition, essentials(allowed values- 400) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 400.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>apdex_server_response_tolerated_factor:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Server tolerated response latency factor.
                </div><br>
                                <div style="font-size: small">
                 - Servermust response within this factor times the satisfactory threshold (apdex_server_response_threshold) to be considered tolerated.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-1000.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 4) edition, essentials(allowed values- 4) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>apdex_server_rtt_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Satisfactory client to avi round trip time(rtt).
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-2000.
                </div><br>
                                <div style="font-size: small">
                 - Unit is milliseconds.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 125) edition, essentials(allowed values- 125) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 125.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>apdex_server_rtt_tolerated_factor:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Tolerated client to avi round trip time(rtt) factor.
                </div><br>
                                <div style="font-size: small">
                 - It is a multiple of apdex_rtt_tolerated_factor.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-1000.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 4) edition, essentials(allowed values- 4) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>client_log_config:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Configure which logs are sent to the avi controller from ses and how they are processed.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>client_log_streaming_config:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Configure to stream logs to an external server.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.1.1.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic edition, essentials edition, enterprise edition.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>conn_lossy_ooo_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - A connection between client and avi is considered lossy when more than this percentage of out of order packets are received.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-100.
                </div><br>
                                <div style="font-size: small">
                 - Unit is percent.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 50) edition, essentials(allowed values- 50) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 50.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>conn_lossy_timeo_rexmt_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - A connection between client and avi is considered lossy when more than this percentage of packets are retransmitted due to timeout.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-100.
                </div><br>
                                <div style="font-size: small">
                 - Unit is percent.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 20) edition, essentials(allowed values- 20) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 20.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>conn_lossy_total_rexmt_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - A connection between client and avi is considered lossy when more than this percentage of packets are retransmitted.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-100.
                </div><br>
                                <div style="font-size: small">
                 - Unit is percent.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 50) edition, essentials(allowed values- 50) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 50.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>conn_lossy_zero_win_size_event_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - A client connection is considered lossy when percentage of times a packet could not be trasmitted due to tcp zero window is above this threshold.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-100.
                </div><br>
                                <div style="font-size: small">
                 - Unit is percent.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 2) edition, essentials(allowed values- 2) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 2.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>conn_server_lossy_ooo_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - A connection between avi and server is considered lossy when more than this percentage of out of order packets are received.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-100.
                </div><br>
                                <div style="font-size: small">
                 - Unit is percent.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 50) edition, essentials(allowed values- 50) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 50.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>conn_server_lossy_timeo_rexmt_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - A connection between avi and server is considered lossy when more than this percentage of packets are retransmitted due to timeout.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-100.
                </div><br>
                                <div style="font-size: small">
                 - Unit is percent.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 20) edition, essentials(allowed values- 20) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 20.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>conn_server_lossy_total_rexmt_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - A connection between avi and server is considered lossy when more than this percentage of packets are retransmitted.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-100.
                </div><br>
                                <div style="font-size: small">
                 - Unit is percent.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 50) edition, essentials(allowed values- 50) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 50.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>conn_server_lossy_zero_win_size_event_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - A server connection is considered lossy when percentage of times a packet could not be trasmitted due to tcp zero window is above this threshold.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-100.
                </div><br>
                                <div style="font-size: small">
                 - Unit is percent.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 2) edition, essentials(allowed values- 2) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 2.
                </div><br>
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
                                                <div style="font-size: small">
                 - User defined description for the object.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>disable_ondemand_metrics:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Virtual service (vs) metrics are processed only when there is live data traffic on the vs.
                </div><br>
                                <div style="font-size: small">
                 - In case, vs is idle for a period of time as specified by ondemand_metrics_idle_timeout then metrics processing is suspended for that vs.
                </div><br>
                                <div style="font-size: small">
                 - Field deprecated in 20.1.3.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.1.1.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>disable_se_analytics:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Disable node (service engine) level analytics forvs metrics.
                </div><br>
                                <div style="font-size: small">
                 - Field deprecated in 20.1.3.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>disable_server_analytics:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Disable analytics on backend servers.
                </div><br>
                                <div style="font-size: small">
                 - This may be desired in container environment when there are large number of ephemeral servers.
                </div><br>
                                <div style="font-size: small">
                 - Additionally, no healthscore of servers is computed when server analytics is disabled.
                </div><br>
                                <div style="font-size: small">
                 - Field deprecated in 20.1.3.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>disable_vs_analytics:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Disable virtualservice (frontend) analytics.
                </div><br>
                                <div style="font-size: small">
                 - This flag disables metrics and healthscore for virtualservice.
                </div><br>
                                <div style="font-size: small">
                 - Field deprecated in 20.1.3.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.1.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_adaptive_config:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Enable adaptive configuration for optimizing resource usage.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.1.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_advanced_analytics:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Enables advanced analytics features like anomaly detection.
                </div><br>
                                <div style="font-size: small">
                 - If set to false, anomaly computation (and associated rules/events) for vs, pool and server metrics will be deactivated.
                </div><br>
                                <div style="font-size: small">
                 - However, setting it to false reduces cpu and memory requirements for analytics subsystem.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.2.13, 18.1.5, 18.2.1.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Special default for basic edition is false, essentials edition is false, enterprise is true.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_ondemand_metrics:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Virtual service (vs) metrics are processed only when there is live data traffic on the vs.
                </div><br>
                                <div style="font-size: small">
                 - In case, vs is idle for a period of time as specified by ondemand_metrics_idle_timeout then metrics processing is suspended for that vs.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.3.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_se_analytics:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Enable node (service engine) level analytics forvs metrics.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.3.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_server_analytics:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Enables analytics on backend servers.
                </div><br>
                                <div style="font-size: small">
                 - This may be desired in container environment when there are large number of ephemeral servers.
                </div><br>
                                <div style="font-size: small">
                 - Additionally, no healthscore of servers is computed when server analytics is enabled.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.3.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_vs_analytics:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Enable virtualservice (frontend) analytics.
                </div><br>
                                <div style="font-size: small">
                 - This flag enables metrics and healthscore for virtualservice.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.3.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_client_close_before_request_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude client closed connection before an http request could be completed from being classified as an error.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_dns_policy_drop_as_significant:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude dns policy drops from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.2.2.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_gs_down_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude queries to gslb services that are operationally down from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_http_error_codes:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - List of http status codes to be excluded from being classified as an error.
                </div><br>
                                <div style="font-size: small">
                 - Error connections or responses impacts health score, are included as significant logs, and may be classified as part of a dos attack.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_invalid_dns_domain_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude dns queries to domains outside the domains configured in the dns application profile from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_invalid_dns_query_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude invalid dns queries from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_issuer_revoked_ocsp_responses_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude the issuer-revoked ocsp responses from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.1.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_no_dns_record_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude queries to domains that did not have configured services/records from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_no_valid_gs_member_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude queries to gslb services that have no available members from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_persistence_change_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude persistence server changed while load balancing' from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_revoked_ocsp_responses_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude the revoked ocsp certificate status responses from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.1.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_server_dns_error_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude server dns error response from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_server_tcp_reset_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude server tcp reset from errors.
                </div><br>
                                <div style="font-size: small">
                 - It is common for applications like ms exchange.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_sip_error_codes:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - List of sip status codes to be excluded from being classified as an error.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.2.13, 18.1.5, 18.2.1.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic edition, essentials edition, enterprise edition.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_stale_ocsp_responses_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude the stale ocsp certificate status responses from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.1.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_syn_retransmit_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude 'server unanswered syns' from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_tcp_reset_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude tcp resets by client from the list of potential errors.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_unavailable_ocsp_responses_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude the unavailable ocsp responses from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.1.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>exclude_unsupported_dns_query_as_error:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Exclude unsupported dns queries from the list of errors.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>healthscore_max_server_limit:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Skips health score computation of pool servers when number of servers in a pool is more than this setting.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5000.
                </div><br>
                                <div style="font-size: small">
                 - Special values are 0- 'server health score is deactivated'.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.2.13, 18.1.4.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Special default for basic edition is 0, essentials edition is 0, enterprise is 20.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 20.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_event_throttle_window:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Time window (in secs) within which only unique health change events should occur.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 1209600) edition, essentials(allowed values- 1209600) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 1209600.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_max_anomaly_penalty:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Maximum penalty that may be deducted from health score for anomalies.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-100.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 10) edition, essentials(allowed values- 10) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 10.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_max_resources_penalty:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Maximum penalty that may be deducted from health score for high resource utilization.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-100.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 25) edition, essentials(allowed values- 25) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 25.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_max_security_penalty:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Maximum penalty that may be deducted from health score based on security assessment.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-100.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 100) edition, essentials(allowed values- 100) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 100.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_min_dos_rate:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Dos connection rate below which the dos security assessment will not kick in.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 1000) edition, essentials(allowed values- 1000) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 1000.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_performance_boost:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Adds free performance score credits to health score.
                </div><br>
                                <div style="font-size: small">
                 - It can be used for compensating health score for known slow applications.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-100.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_pscore_traffic_threshold_l4_client:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 10) edition, essentials(allowed values- 10) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 10.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_pscore_traffic_threshold_l4_server:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 10) edition, essentials(allowed values- 10) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 10.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_certscore_expired:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when the certificate has expired.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 0.0) edition, essentials(allowed values- 0.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 0.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_certscore_gt30d:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when the certificate expires in more than 30 days.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 5.0) edition, essentials(allowed values- 5.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_certscore_le07d:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when the certificate expires in less than or equal to 7 days.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 2.0) edition, essentials(allowed values- 2.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 2.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_certscore_le30d:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when the certificate expires in less than or equal to 30 days.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 4.0) edition, essentials(allowed values- 4.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_chain_invalidity_penalty:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Penalty for allowing certificates with invalid chain.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 1.0) edition, essentials(allowed values- 1.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 1.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_cipherscore_eq000b:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when the minimum cipher strength is 0 bits.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 0.0) edition, essentials(allowed values- 0.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 0.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_cipherscore_ge128b:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when the minimum cipher strength is greater than equal to 128 bits.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 5.0) edition, essentials(allowed values- 5.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_cipherscore_lt128b:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when the minimum cipher strength is less than 128 bits.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 3.5) edition, essentials(allowed values- 3.5) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 3.5.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_encalgo_score_none:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when no algorithm is used for encryption.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 0.0) edition, essentials(allowed values- 0.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 0.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_encalgo_score_rc4:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when rc4 algorithm is used for encryption.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 2.5) edition, essentials(allowed values- 2.5) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 2.5.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_hsts_penalty:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Penalty for not enabling hsts.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 1.0) edition, essentials(allowed values- 1.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 1.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_nonpfs_penalty:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Penalty for allowing non-pfs handshakes.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 1.0) edition, essentials(allowed values- 1.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 1.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_ocsp_revoked_score:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when ocsp certificate status is set to revoked or issuer revoked.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0.0-5.0.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.1.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 0.0) edition, essentials(allowed values- 0.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 0.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_selfsignedcert_penalty:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Deprecated.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 1.0) edition, essentials(allowed values- 1.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 1.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_ssl30_score:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when supporting ssl3.0 encryption protocol.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 3.5) edition, essentials(allowed values- 3.5) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 3.5.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_tls10_score:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when supporting tls1.0 encryption protocol.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 5.0) edition, essentials(allowed values- 5.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_tls11_score:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when supporting tls1.1 encryption protocol.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 5.0) edition, essentials(allowed values- 5.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_tls12_score:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when supporting tls1.2 encryption protocol.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 5.0) edition, essentials(allowed values- 5.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_tls13_score:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Score assigned when supporting tls1.3 encryption protocol.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.6.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 5.0) edition, essentials(allowed values- 5.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hs_security_weak_signature_algo_penalty:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Penalty for allowing weak signature algorithm(s).
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 1.0) edition, essentials(allowed values- 1.0) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 1.0.
                </div><br>
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
                                                <div style="font-size: small">
                 - Key value pairs for granular object access control.
                </div><br>
                                <div style="font-size: small">
                 - Also allows for classification and tagging of similar objects.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.2.
                </div><br>
                                <div style="font-size: small">
                 - Maximum of 4 items allowed.
                </div><br>
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
                                                <div style="font-size: small">
                 - The name of the analytics profile.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ondemand_metrics_idle_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - This flag sets the time duration of no live data traffic after which virtual service metrics processing is suspended.
                </div><br>
                                <div style="font-size: small">
                 - It is applicable only when enable_ondemand_metrics is set to false.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.1.1.
                </div><br>
                                <div style="font-size: small">
                 - Unit is seconds.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 1800.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ranges:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - List of http status code ranges to be excluded from being classified as an error.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>resp_code_block:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Block of http response codes to be excluded from being classified as an error.
                </div><br>
                                <div style="font-size: small">
                 - Enum options - AP_HTTP_RSP_4XX, AP_HTTP_RSP_5XX.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sensitive_log_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Rules applied to the http application log for filtering sensitive information.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.2.10, 18.1.2.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic edition, essentials edition, enterprise edition.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sip_log_depth:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Maximum number of sip messages added in logs for a sip transaction.
                </div><br>
                                <div style="font-size: small">
                 - By default, this value is 20.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-1000.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.2.13, 18.1.5, 18.2.1.
                </div><br>
                                <div style="font-size: small">
                 - Allowed in basic(allowed values- 20) edition, essentials(allowed values- 20) edition, enterprise edition.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 20.
                </div><br>
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
                                                <div style="font-size: small">
                 - It is a reference to an object of type tenant.
                </div><br>
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
                                                <div style="font-size: small">
                 - Avi controller URL of the object.
                </div><br>
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
                                                <div style="font-size: small">
                 - Uuid of the analytics profile.
                </div><br>
                                            </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    
  - name: Create a custom Analytics profile object
    avi_analyticsprofile:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      apdex_response_threshold: 500
      apdex_response_tolerated_factor: 4.0
      apdex_rtt_threshold: 250
      apdex_rtt_tolerated_factor: 4.0
      apdex_rum_threshold: 5000
      apdex_rum_tolerated_factor: 4.0
      apdex_server_response_threshold: 400
      apdex_server_response_tolerated_factor: 4.0
      apdex_server_rtt_threshold: 125
      apdex_server_rtt_tolerated_factor: 4.0
      conn_lossy_ooo_threshold: 50
      conn_lossy_timeo_rexmt_threshold: 20
      conn_lossy_total_rexmt_threshold: 50
      conn_lossy_zero_win_size_event_threshold: 2
      conn_server_lossy_ooo_threshold: 50
      conn_server_lossy_timeo_rexmt_threshold: 20
      conn_server_lossy_total_rexmt_threshold: 50
      conn_server_lossy_zero_win_size_event_threshold: 2
      enable_se_analytics: true
      enable_server_analytics: true
      exclude_client_close_before_request_as_error: false
      exclude_persistence_change_as_error: false
      exclude_server_tcp_reset_as_error: false
      exclude_syn_retransmit_as_error: false
      exclude_tcp_reset_as_error: false
      hs_event_throttle_window: 1209600
      hs_max_anomaly_penalty: 10
      hs_max_resources_penalty: 25
      hs_max_security_penalty: 100
      hs_min_dos_rate: 1000
      hs_performance_boost: 20
      hs_pscore_traffic_threshold_l4_client: 10.0
      hs_pscore_traffic_threshold_l4_server: 10.0
      hs_security_certscore_expired: 0.0
      hs_security_certscore_gt30d: 5.0
      hs_security_certscore_le07d: 2.0
      hs_security_certscore_le30d: 4.0
      hs_security_chain_invalidity_penalty: 1.0
      hs_security_cipherscore_eq000b: 0.0
      hs_security_cipherscore_ge128b: 5.0
      hs_security_cipherscore_lt128b: 3.5
      hs_security_encalgo_score_none: 0.0
      hs_security_encalgo_score_rc4: 2.5
      hs_security_hsts_penalty: 0.0
      hs_security_nonpfs_penalty: 1.0
      hs_security_selfsignedcert_penalty: 1.0
      hs_security_ssl30_score: 3.5
      hs_security_tls10_score: 5.0
      hs_security_tls11_score: 5.0
      hs_security_tls12_score: 5.0
      hs_security_weak_signature_algo_penalty: 1.0
      name: jason-analytics-profile
      tenant_ref: /api/tenant?name=Demo



Status
------


Authors
~~~~~~~

- Gaurav Rastogi (grastogi@avinetworks.com)
- Sandeep Bandi (sbandi@avinetworks.com)



