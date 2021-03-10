.. vmware.nsx_alb.avi_gslb:


*****************************
vmware.nsx_alb.avi_gslb
*****************************

**Module for setup of Gslb Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure Gslb object
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
                <b>async_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Frequency with which messages are propagated to vs mgr.
                </div><br>
                                <div style="font-size: small">
                 - Value of 0 disables async behavior and rpc are sent inline.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 0-5.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.3.
                </div><br>
                                <div style="font-size: small">
                 - Unit is sec.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>clear_on_max_retries:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Max retries after which the remote site is treated as a fresh start.
                </div><br>
                                <div style="font-size: small">
                 - In fresh start all the configs are downloaded.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-1024.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 20.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>client_ip_addr_group:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Group to specify if the client ip addresses are public or private.
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
                <b>dns_configs:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Sub domain configuration for the gslb.
                </div><br>
                                <div style="font-size: small">
                 - Gslb service's fqdn must be a match one of these subdomains.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>error_resync_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Frequency with which errored messages are resynced to follower sites.
                </div><br>
                                <div style="font-size: small">
                 - Value of 0 disables resync behavior.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 60-3600.
                </div><br>
                                <div style="font-size: small">
                 - Special values are 0 - 'disable'.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.3.
                </div><br>
                                <div style="font-size: small">
                 - Unit is sec.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 300.
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
                <b>leader_cluster_uuid:</b>
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
                 - Mark this site as leader of gslb configuration.
                </div><br>
                                <div style="font-size: small">
                 - This site is the one among the avi sites.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>maintenance_mode:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - This field disables the configuration operations on the leader for all federated objects.
                </div><br>
                                <div style="font-size: small">
                 - Cud operations on gslb, gslbservice, gslbgeodbprofile and other federated objects will be rejected.
                </div><br>
                                <div style="font-size: small">
                 - The rest-api disabling helps in upgrade scenarios where we don't want configuration sync operations to the gslb member when the member is being
                </div><br>
                                <div style="font-size: small">
                 - upgraded.
                </div><br>
                                <div style="font-size: small">
                 - This configuration programmatically blocks the leader from accepting new gslb configuration when member sites are undergoing upgrade.
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
                 - Name for the gslb object.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>replication_policy:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Policy for replicating configuration to the active follower sites.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 20.1.1.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>send_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Frequency with which group members communicate.
                </div><br>
                                <div style="font-size: small">
                 - Allowed values are 1-3600.
                </div><br>
                                <div style="font-size: small">
                 - Unit is sec.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 15.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>send_interval_prior_to_maintenance_mode:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - The user can specify a send-interval while entering maintenance mode.
                </div><br>
                                <div style="font-size: small">
                 - The validity of this 'maintenance send-interval' is only during maintenance mode.
                </div><br>
                                <div style="font-size: small">
                 - When the user leaves maintenance mode, the original send-interval is reinstated.
                </div><br>
                                <div style="font-size: small">
                 - This internal variable is used to store the original send-interval.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.3.
                </div><br>
                                <div style="font-size: small">
                 - Unit is sec.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sites:</b>
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
                 - Select avi site member belonging to this gslb.
                </div><br>
                                <div style="font-size: small">
                 - Minimum of 1 items required.
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
                <b>tenant_scoped:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - This field indicates tenant visibility for gs pool member selection across the gslb federated objects.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.12,20.1.4.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>third_party_sites:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - Third party site member belonging to this gslb.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 17.1.1.
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
                 - Uuid of the gslb object.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>view_id:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                 - The view-id is used in change-leader mode to differentiate partitioned groups while they have the same gslb namespace.
                </div><br>
                                <div style="font-size: small">
                 - Each partitioned group will be able to operate independently by using the view-id.
                </div><br>
                                <div style="font-size: small">
                 - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                </div><br>
                                            </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    
- name: Example to create Gslb object
  avi_gslb:
    name: "test-gslb"
    avi_credentials:
      username: '{{ username }}'
      password: '{{ password }}'
      controller: '{{ controller }}'
    sites:
      - name: "test-site1"
        username: "gslb_username"
        password: "gslb_password"
        ip_addresses:
          - type: "V4"
            addr: "10.10.28.83"
        enabled: True
        member_type: "GSLB_ACTIVE_MEMBER"
        port: 443
        cluster_uuid: "cluster-d4ee5fcc-3e0a-4d4f-9ae6-4182bc605829"
      - name: "test-site2"
        username: "gslb_username"
        password: "gslb_password"
        ip_addresses:
          - type: "V4"
            addr: "10.10.28.86"
        enabled: True
        member_type: "GSLB_ACTIVE_MEMBER"
        port: 443
        cluster_uuid: "cluster-0c37ae8d-ab62-410c-ad3e-06fa831950b1"
    dns_configs:
      - domain_name: "test1.com"
      - domain_name: "test2.com"
    leader_cluster_uuid: "cluster-d4ee5fcc-3e0a-4d4f-9ae6-4182bc605829"

- name: Update Gslb site's configurations (Patch Add Operation)
  avi_gslb:
    avi_credentials:
      username: '{{ username }}'
      password: '{{ password }}'
      controller: '{{ controller }}'
    avi_api_update_method: patch
    avi_api_patch_op: add
    leader_cluster_uuid: "cluster-d4ee5fcc-3e0a-4d4f-9ae6-4182bc605829"
    name: "test-gslb"
    dns_configs:
      - domain_name: "temp1.com"
      - domain_name: "temp2.com"
    sites:
      - name: "test-site1"
        username: "gslb_username"
        password: "gslb_password"
        ip_addresses:
          - type: "V4"
            addr: "10.10.21.13"
        enabled: True
        member_type: "GSLB_ACTIVE_MEMBER"
        port: 283
        cluster_uuid: "cluster-d4ee5fcc-3e0a-4d4f-9ae6-4182bc605829"

- name: Update Gslb site's configurations (Patch Replace Operation)
  avi_gslb:
    avi_credentials:
      username: "{{ username }}"
      password: "{{ password }}"
      controller: "{{ controller }}"
    # On basis of cluster leader uuid dns_configs is set for that perticular leader cluster
    leader_cluster_uuid: "cluster-84aa795f-8f09-42bb-97a4-5103f4a53da9"
    name: "test-gslb"
    avi_api_update_method: patch
    avi_api_patch_op: replace
    dns_configs:
      - domain_name: "test3.com"
      - domain_name: "temp3.com"
    sites:
      - name: "test-site1"
        username: "gslb_username"
        password: "gslb_password"
        ip_addresses:
          - type: "V4"
            addr: "10.10.11.24"
        enabled: True
        member_type: "GSLB_ACTIVE_MEMBER"
        port: 283
        cluster_uuid: "cluster-d4ee5fcc-3e0a-4d4f-9ae6-4182bc605829"

- name: Delete Gslb site's den_vses configurations (Patch Delete(dns_vses) Operation)
  avi_gslb:
    avi_credentials:
      username: "{{ username }}"
      password: "{{ password }}"
      controller: "{{ controller }}"
    # On basis of cluster leader uuid dns_configs is set for that perticular leader cluster
    leader_cluster_uuid: "cluster-84aa795f-8f09-42bb-97a4-5103f4a53da9"
    name: "test-gslb"
    avi_api_update_method: patch
    avi_api_patch_op: delete
    dns_configs:
    sites:
      - ip_addresses: "10.10.28.83"
      - ip_addresses: "10.10.28.86"

- name: Delete Gslb complete site's configurations (Patch Delete(site) Operation)
  avi_gslb:
    avi_credentials: "{{ avi_credentials }}"
    api_version: 18.2.8
    avi_api_update_method: patch
    avi_api_patch_op: delete
    patch_level: '/site'
    name: gslb.lab2.local
    leader_cluster_uuid: "cluster-84aa795f-8f09-42bb-97a4-5103f4a53da9"
    dns_configs:
    sites:
      - ip_addresses: 10.10.28.83



Status
------


Authors
~~~~~~~

- Gaurav Rastogi (grastogi@avinetworks.com)
- Sandeep Bandi (sbandi@avinetworks.com)



