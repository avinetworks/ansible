.. vmware.nsx_alb.avi_gslbservice:


*****************************
vmware.nsx_alb.avi_gslbservice
*****************************

**Module for setup of GslbService Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure GslbService object
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
                <b>application_persistence_profile_ref:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - The federated application persistence associated with gslbservice site persistence functionality.
                </div><br>
                                <div style="font-size: small">
                 - It is a reference to an object of type applicationpersistenceprofile.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.2.1.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>controller_health_status_enabled:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Gs member's overall health status is derived based on a combination of controller and datapath health-status inputs.
                </div><br>
                                <div style="font-size: small">
                 - Note that the datapath status is determined by the association of health monitor profiles.
                </div><br>
                                <div style="font-size: small">
                 - Only the controller provided status is determined through this configuration.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
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
                                                <div style="font-size: small">
                 - Creator name.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.1.2.
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
                <b>domain_names:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                required: true
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                 - Fully qualified domain name of the gslb service.
                </div><br>
                                <div style="font-size: small">
                 - Minimum of 1 items required.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>down_response:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Response to the client query when the gslb service is down.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enabled:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Enable or disable the gslb service.
                </div><br>
                                <div style="font-size: small">
                 - If the gslb service is enabled, then the vips are sent in the dns responses based on reachability and configured algorithm.
                </div><br>
                                <div style="font-size: small">
                 - If the gslb service is disabled, then the vips are no longer available in the dns response.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>groups:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                required: true
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                 - Select list of pools belonging to this gslb service.
                </div><br>
                                <div style="font-size: small">
                 - Minimum of 1 items required.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>health_monitor_refs:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Verify vs health by applying one or more health monitors.
                </div><br>
                                <div style="font-size: small">
                 - Active monitors generate synthetic traffic from dns service engine and to mark a vs up or down based on the response.
                </div><br>
                                <div style="font-size: small">
                 - It is a reference to an object of type healthmonitor.
                </div><br>
                                <div style="font-size: small">
                 - Maximum of 6 items allowed.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>health_monitor_scope:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Health monitor probe can be executed for all the members or it can be executed only for third-party members.
                </div><br>
                                <div style="font-size: small">
                 - This operational mode is useful to reduce the number of health monitor probes in case of a hybrid scenario.
                </div><br>
                                <div style="font-size: small">
                 - In such a case, avi members can have controller derived status while non-avi members can be probed by via health monitor probes in dataplane.
                </div><br>
                                <div style="font-size: small">
                 - Enum options - GSLB_SERVICE_HEALTH_MONITOR_ALL_MEMBERS, GSLB_SERVICE_HEALTH_MONITOR_ONLY_NON_AVI_MEMBERS.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as GSLB_SERVICE_HEALTH_MONITOR_ALL_MEMBERS.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hm_off:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - This field is an internal field and is used in se.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.2.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>is_federated:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - This field indicates that this object is replicated across gslb federation.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.1.3.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
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
                <b>min_members:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - The minimum number of members to distribute traffic to.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-65535.
                </div><br>
                                <div style="font-size: small">
                 - Special values are 0 - 'disable'.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.2.4.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 0.
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
                 - Name for the gslb service.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>num_dns_ip:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Number of ip addresses of this gslb service to be returned by the dns service.
                </div><br>
                                <div style="font-size: small">
                 - Enter 0 to return all ip addresses.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-20.
                </div><br>
                                <div style="font-size: small">
                 - Special values are 0- 'return all ip addresses'.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>pool_algorithm:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - The load balancing algorithm will pick a gslb pool within the gslb service list of available pools.
                </div><br>
                                <div style="font-size: small">
                 - Enum options - GSLB_SERVICE_ALGORITHM_PRIORITY, GSLB_SERVICE_ALGORITHM_GEO.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.2.3.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as GSLB_SERVICE_ALGORITHM_PRIORITY.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>resolve_cname:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - This field indicates that for a cname query, respond with resolved cnames in the additional section with a records.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.5.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>site_persistence_enabled:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Enable site-persistence for the gslbservice.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.2.1.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
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
                <b>ttl:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Ttl value (in seconds) for records served for this gslb service by the dns service.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-86400.
                </div><br>
                                <div style="font-size: small">
                 - Unit is sec.
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
                <b>use_edns_client_subnet:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Use the client ip subnet from the edns option as source ipaddress for client geo-location and consistent hash algorithm.
                </div><br>
                                <div style="font-size: small">
                 - Default is true.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.1.1.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
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
                 - Uuid of the gslb service.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>wildcard_match:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Enable wild-card match of fqdn  if an exact match is not found in the dns table, the longest match is chosen by wild-carding the fqdn in the dns
                </div><br>
                                <div style="font-size: small">
                 - request.
                </div><br>
                                <div style="font-size: small">
                 - Default is false.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.1.1.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div><br>
                                            </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    - name: Example to create GslbService object
      avi_gslbservice:
        controller: 10.10.25.42
        username: admin
        password: something
        state: present
        name: sample_gslbservice


Status
------


Authors
~~~~~~~

- Amol Shinde (samol@vmware.com)



