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
.. vmware.nsx_alb.avi_serviceenginegroup:


*****************************
vmware.nsx_alb.avi_serviceenginegroup
*****************************

**Module for setup of ServiceEngineGroup Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure ServiceEngineGroup object
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
                <b>accelerated_networking:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable accelerated networking option for azure se.
                         - Accelerated networking enables single root i/o virtualization (sr-iov) to a se vm.
                         - This improves networking performance.
                         - Field introduced in 17.2.14,18.1.5,18.2.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>active_standby:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Service engines in active/standby mode for ha failover.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>additional_config_memory:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Indicates the percent of config memory used for config updates.
                         - Allowed values are 0-90.
                         - Field deprecated in 18.1.2.
                         - Field introduced in 18.1.1.
                         - Unit is percent.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>advertise_backend_networks:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Advertise reach-ability of backend server networks via adc through bgp for default gateway feature.
                         - Field deprecated in 18.2.5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>aggressive_failure_detection:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable aggressive failover configuration for ha.
                         - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>algo:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - In compact placement, virtual services are placed on existing ses until max_vs_per_se limit is reached.
                         - Enum options - PLACEMENT_ALGO_PACKED, PLACEMENT_ALGO_DISTRIBUTED.
                         - Default value when not specified in API or module is interpreted by Avi Controller as PLACEMENT_ALGO_PACKED.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>allow_burst:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Allow ses to be created using burst license.
                         - Field introduced in 17.2.5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>app_cache_percent:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - A percent value of total se memory reserved for applicationcaching.
                         - This is an se bootup property and requires se restart.requires se reboot.
                         - Allowed values are 0 - 100.
                         - Special values are 0- 'disable'.
                         - Field introduced in 18.2.3.
                         - Unit is percent.
                         - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
                         - Special default for basic edition is 0, essentials edition is 0, enterprise is 10.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 10.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>app_cache_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - The max memory that can be allocated for the app cache.
                         - This value will act as an upper bound on the cache size specified in app_cache_percent.
                         - Special values are 0- 'disable'.
                         - Field introduced in 20.1.1.
                         - Unit is gb.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>app_learning_memory_percent:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - A percent value of total se memory reserved for application learning.
                         - This is an se bootup property and requires se restart.
                         - Allowed values are 0 - 10.
                         - Field introduced in 18.2.3.
                         - Unit is percent.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>archive_shm_limit:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Amount of se memory in gb until which shared memory is collected in core archive.
                         - Field introduced in 17.1.3.
                         - Unit is gb.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 8.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>async_ssl:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Ssl handshakes will be handled by dedicated ssl threads.requires se reboot.
                         - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>async_ssl_threads:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of async ssl threads per se_dp.requires se reboot.
                         - Allowed values are 1-16.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>auto_rebalance:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - If set, virtual services will be automatically migrated when load on an se is less than minimum or more than maximum thresholds.
                         - Only alerts are generated when the auto_rebalance is not set.
                         - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>auto_rebalance_capacity_per_se:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Capacities of se for auto rebalance for each criteria.
                         - Field introduced in 17.2.4.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>auto_rebalance_criteria:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Set of criteria for se auto rebalance.
                         - Enum options - SE_AUTO_REBALANCE_CPU, SE_AUTO_REBALANCE_PPS, SE_AUTO_REBALANCE_MBPS, SE_AUTO_REBALANCE_OPEN_CONNS, SE_AUTO_REBALANCE_CPS.
                         - Field introduced in 17.2.3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>auto_rebalance_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Frequency of rebalance, if 'auto rebalance' is enabled.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 300.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>auto_redistribute_active_standby_load:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Redistribution of virtual services from the takeover se to the replacement se can cause momentary traffic loss.
                         - If the auto-redistribute load option is left in its default off state, any desired rebalancing requires calls to rest api.
                         - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>availability_zone_refs:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Availability zones for virtual service high availability.
                         - It is a reference to an object of type availabilityzone.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>bgp_state_update_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Bgp peer state update interval.
                         - Allowed values are 5-100.
                         - Field introduced in 17.2.14,18.1.5,18.2.1.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 60.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>buffer_se:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Excess service engine capacity provisioned for ha failover.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
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
                                     - It is a reference to an object of type cloud.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>compress_ip_rules_for_each_ns_subnet:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Compress ip rules into a single subnet based ip rule for each north-south ipam subnet configured in pcap mode in openshift/kubernetes node.
                         - Field introduced in 18.2.9, 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>config_debugs_on_all_cores:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable config debugs on all cores of se.
                         - Field introduced in 17.2.13,18.1.5,18.2.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>connection_memory_percentage:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Percentage of memory for connection state.
                         - This will come at the expense of memory used for http in-memory cache.
                         - Allowed values are 10-90.
                         - Unit is percent.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 50.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>core_shm_app_cache:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Include shared memory for app cache in core file.requires se reboot.
                         - Field introduced in 18.2.8, 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>core_shm_app_learning:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Include shared memory for app learning in core file.requires se reboot.
                         - Field introduced in 18.2.8, 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>cpu_reserve:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Boolean flag to set cpu_reserve.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>cpu_socket_affinity:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Allocate all the cpu cores for the service engine virtual machines  on the same cpu socket.
                         - Applicable only for vcenter cloud.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>custom_securitygroups_data:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Custom security groups to be associated with data vnics for se instances in openstack and aws clouds.
                         - Field introduced in 17.1.3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>custom_securitygroups_mgmt:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Custom security groups to be associated with management vnic for se instances in openstack and aws clouds.
                         - Field introduced in 17.1.3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>custom_tag:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Custom tag will be used to create the tags for se instance in aws.
                         - Note this is not the same as the prefix for se name.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>data_network_id:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Subnet used to spin up the data nic for service engines, used only for azure cloud.
                         - Overrides the cloud level setting for service engine subnet.
                         - Field introduced in 18.2.3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>datascript_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of instructions before datascript times out.
                         - Allowed values are 0-100000000.
                         - Field introduced in 18.2.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1000000.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dedicated_dispatcher_core:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Dedicate the core that handles packet receive/transmit from the network to just the dispatching function.
                         - Don't use it for tcp/ip and ssl functions.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
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
                <b>disable_avi_securitygroups:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - By default, avi creates and manages security groups along with custom sg provided by user.
                         - Set this to true to disallow avi to create and manage new security groups.
                         - Avi will only make use of custom security groups provided by user.
                         - This option is supported for aws and openstack cloud types.
                         - Field introduced in 17.2.13,18.1.4,18.2.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>disable_csum_offloads:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Stop using tcp/udp and ip checksum offload features of nics.
                         - Field introduced in 17.1.14, 17.2.5, 18.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>disable_flow_probes:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Disable flow probes for scaled out vs'es.
                         - Field introduced in 20.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>disable_gro:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Disable generic receive offload (gro) in dpdk poll-mode driver packet receive path.
                         - Gro is on by default on nics that do not support lro (large receive offload) or do not gain performance boost from lro.
                         - Field introduced in 17.2.5, 18.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>disable_se_memory_check:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - If set, disable the config memory check done in service engine.
                         - Field introduced in 18.1.2.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>disable_tso:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Disable tcp segmentation offload (tso) in dpdk poll-mode driver packet transmit path.
                         - Tso is on by default on nics that support it.
                         - Field introduced in 17.2.5, 18.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>disk_per_se:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Amount of disk space for each of the service engine virtual machines.
                         - Unit is gb.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 15.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>distribute_load_active_standby:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Use both the active and standby service engines for virtual service placement in the legacy active standby ha mode.
                         - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>distribute_queues:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Distributes queue ownership among cores so multiple cores handle dispatcher duties.
                         - Requires se reboot.
                         - Deprecated from 18.2.8, instead use max_queues_per_vnic.
                         - Field introduced in 17.2.8.
                         - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>distribute_vnics:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Distributes vnic ownership among cores so multiple cores handle dispatcher duties.requires se reboot.
                         - Field introduced in 18.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dp_aggressive_deq_interval_msec:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Dequeue interval for receive queue from se_dp in aggressive mode.
                         - Allowed values are 1-1000.
                         - Field introduced in 21.1.1.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dp_aggressive_enq_interval_msec:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enqueue interval for request queue to se_dp in aggressive mode.
                         - Allowed values are 1-1000.
                         - Field introduced in 21.1.1.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dp_aggressive_hb_frequency:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Frequency of se - se hb messages when aggressive failure mode detection is enabled.
                         - Field introduced in 20.1.3.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 100.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dp_aggressive_hb_timeout_count:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Consecutive hb failures after which failure is reported to controller,when aggressive failure mode detection is enabled.
                         - Field introduced in 20.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 10.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dp_deq_interval_msec:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Dequeue interval for receive queue from se_dp.
                         - Allowed values are 1-1000.
                         - Field introduced in 21.1.1.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 20.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dp_enq_interval_msec:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enqueue interval for request queue to se_dp.
                         - Allowed values are 1-1000.
                         - Field introduced in 21.1.1.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 20.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dp_hb_frequency:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Frequency of se - se hb messages when aggressive failure mode detection is not enabled.
                         - Field introduced in 20.1.3.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 100.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dp_hb_timeout_count:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Consecutive hb failures after which failure is reported to controller, when aggressive failure mode detection is not enabled.
                         - Field introduced in 20.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 10.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_gratarp_permanent:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable gratarp for vip_ip.
                         - Field introduced in 18.2.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_hsm_priming:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - (this is a beta feature).
                         - Enable hsm key priming.
                         - If enabled, key handles on the hsm will be synced to se before processing client connections.
                         - Field introduced in 17.2.7, 18.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_multi_lb:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Applicable only for azure cloud with basic sku lb.
                         - If set, additional azure lbs will be automatically created if resources in existing lb are exhausted.
                         - Field introduced in 17.2.10, 18.1.2.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_pcap_tx_ring:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable tx ring support in pcap mode of operation.
                         - Tso feature is not supported with tx ring enabled.
                         - Deprecated from 18.2.8, instead use pcap_tx_mode.
                         - Requires se reboot.
                         - Field introduced in 18.2.5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_routing:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable routing for this serviceenginegroup.
                         - Field deprecated in 18.2.5.
                         - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_vip_on_all_interfaces:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable vip on all interfaces of se.
                         - Field deprecated in 18.2.5.
                         - Field introduced in 17.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_vmac:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Use virtual mac address for interfaces on which floating interface ips are placed.
                         - Field deprecated in 18.2.5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ephemeral_portrange_end:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - End local ephemeral port number for outbound connections.
                         - Field introduced in 17.2.13, 18.1.5, 18.2.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ephemeral_portrange_start:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Start local ephemeral port number for outbound connections.
                         - Field introduced in 17.2.13, 18.1.5, 18.2.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>extra_config_multiplier:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Multiplier for extra config to support large vs/pool config.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>extra_shared_config_memory:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Extra config memory to support large geo db configuration.
                         - Field introduced in 17.1.1.
                         - Unit is mb.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>floating_intf_ip:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - If serviceenginegroup is configured for legacy 1+1 active standby ha mode, floating ip's will be advertised only by the active se in the pair.
                         - Virtual services in this group must be disabled/enabled for any changes to the floating ip's to take effect.
                         - Only active se hosting vs tagged with active standby se 1 tag will advertise this floating ip when manual load distribution is enabled.
                         - Field deprecated in 18.2.5.
                         - Maximum of 32 items allowed.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>floating_intf_ip_se_2:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - If serviceenginegroup is configured for legacy 1+1 active standby ha mode, floating ip's will be advertised only by the active se in the pair.
                         - Virtual services in this group must be disabled/enabled for any changes to the floating ip's to take effect.
                         - Only active se hosting vs tagged with active standby se 2 tag will advertise this floating ip when manual load distribution is enabled.
                         - Field deprecated in 18.2.5.
                         - Maximum of 32 items allowed.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>flow_table_new_syn_max_entries:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Maximum number of flow table entries that have not completed tcp three-way handshake yet.
                         - Field introduced in 17.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>free_list_size:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of entries in the free list.
                         - Field introduced in 17.2.10, 18.1.2.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1024.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>gcp_config:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Google cloud platform, service engine group configuration.
                         - Field introduced in 20.1.3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>gratarp_permanent_periodicity:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Gratarp periodicity for vip-ip.
                         - Allowed values are 5-30.
                         - Field introduced in 18.2.3.
                         - Unit is min.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 10.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ha_mode:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - High availability mode for all the virtual services using this service engine group.
                         - Enum options - HA_MODE_SHARED_PAIR, HA_MODE_SHARED, HA_MODE_LEGACY_ACTIVE_STANDBY.
                         - Allowed in basic(allowed values- ha_mode_legacy_active_standby) edition, essentials(allowed values- ha_mode_legacy_active_standby) edition,
                         - enterprise edition.
                         - Special default for basic edition is ha_mode_legacy_active_standby, essentials edition is ha_mode_legacy_active_standby, enterprise is
                         - ha_mode_shared.
                         - Default value when not specified in API or module is interpreted by Avi Controller as HA_MODE_SHARED.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>handle_per_pkt_attack:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Configuration to handle per packet attack handling.for example, dns reflection attack is a type of attack where a response packet is sent to the
                         - dns vs.this configuration tells if such packets should be dropped without further processing.
                         - Field introduced in 20.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hardwaresecuritymodulegroup_ref:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - It is a reference to an object of type hardwaresecuritymodulegroup.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>heap_minimum_config_memory:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Minimum required heap memory to apply any configuration.
                         - Allowed values are 0-100.
                         - Field introduced in 18.1.2.
                         - Unit is mb.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 8.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hm_on_standby:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable active health monitoring from the standby se for all placed virtual services.
                         - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                         - Special default for basic edition is false, essentials edition is false, enterprise is true.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>host_attribute_key:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Key of a (key, value) pair identifying a label for a set of nodes usually in container clouds.
                         - Needs to be specified together with host_attribute_value.
                         - Ses can be configured differently including ha modes across different se groups.
                         - May also be used for isolation between different classes of virtualservices.
                         - Virtualservices' se group may be specified via annotations/labels.
                         - A openshift/kubernetes namespace maybe annotated with a matching se group label as openshift.io/node-selector  apptype=prod.
                         - When multiple se groups are used in a cloud with host attributes specified,just a single se group can exist as a match-all se group without a
                         - host_attribute_key.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>host_attribute_value:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Value of a (key, value) pair identifying a label for a set of nodes usually in container clouds.
                         - Needs to be specified together with host_attribute_key.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>host_gateway_monitor:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable the host gateway monitor when service engine is deployed as docker container.
                         - Disabled by default.
                         - Field introduced in 17.2.4.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>hypervisor:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Override default hypervisor.
                         - Enum options - DEFAULT, VMWARE_ESX, KVM, VMWARE_VSAN, XEN.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ignore_rtt_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Ignore rtt samples if it is above threshold.
                         - Field introduced in 17.1.6,17.2.2.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 5000.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ingress_access_data:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Program se security group ingress rules to allow vip data access from remote cidr type.
                         - Enum options - SG_INGRESS_ACCESS_NONE, SG_INGRESS_ACCESS_ALL, SG_INGRESS_ACCESS_VPC.
                         - Field introduced in 17.1.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as SG_INGRESS_ACCESS_ALL.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ingress_access_mgmt:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Program se security group ingress rules to allow ssh/icmp management access from remote cidr type.
                         - Enum options - SG_INGRESS_ACCESS_NONE, SG_INGRESS_ACCESS_ALL, SG_INGRESS_ACCESS_VPC.
                         - Field introduced in 17.1.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as SG_INGRESS_ACCESS_ALL.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>instance_flavor:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Instance/flavor name for se instance.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>instance_flavor_info:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Additional information associated with instance_flavor.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>iptables:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Iptable rules.
                         - Maximum of 128 items allowed.
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
                                     - Labels associated with this se group.
                         - Field introduced in 20.1.1.
                         - Maximum of 1 items allowed.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>least_load_core_selection:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Select core with least load for new flow.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>license_tier:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Specifies the license tier which would be used.
                         - This field by default inherits the value from cloud.
                         - Enum options - ENTERPRISE_16, ENTERPRISE, ENTERPRISE_18, BASIC, ESSENTIALS.
                         - Field introduced in 17.2.5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>license_type:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - If no license type is specified then default license enforcement for the cloud type is chosen.
                         - Enum options - LIC_BACKEND_SERVERS, LIC_SOCKETS, LIC_CORES, LIC_HOSTS, LIC_SE_BANDWIDTH, LIC_METERED_SE_BANDWIDTH.
                         - Field introduced in 17.2.5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>log_disksz:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Maximum disk capacity (in mb) to be allocated to an se.
                         - This is exclusively used for debug and log data.
                         - Unit is mb.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 10000.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>log_malloc_failure:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Se will log memory allocation related failure to the se_trace file, wherever available.
                         - Field introduced in 20.1.2.
                         - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>max_concurrent_external_hm:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Maximum number of external health monitors that can run concurrently in a service engine.
                         - This helps control the cpu and memory use by external health monitors.
                         - Special values are 0- 'value will be internally calculated based on cpu and memory'.
                         - Field introduced in 18.2.7.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>max_cpu_usage:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - When cpu usage on an se exceeds this threshold, virtual services hosted on this se may be rebalanced to other ses to reduce load.
                         - A new se may be created as part of this process.
                         - Allowed values are 40-90.
                         - Unit is percent.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 80.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>max_memory_per_mempool:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Max bytes that can be allocated in a single mempool.
                         - Field introduced in 18.1.5.
                         - Unit is mb.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 64.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>max_num_se_dps:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Configures the maximum number of se_dp processes created on the se, requires se reboot.
                         - If not configured, defaults to the number of cpus on the se.
                         - This should only be used if user wants to limit the number of se_dps to less than the available cpus on the se.
                         - Allowed values are 1-128.
                         - Field introduced in 20.1.1.
                         - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>max_public_ips_per_lb:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Applicable to azure platform only.
                         - Maximum number of public ips per azure lb.
                         - Field introduced in 17.2.12, 18.1.2.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 30.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>max_queues_per_vnic:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Maximum number of queues per vnic setting to '0' utilises all queues that are distributed across dispatcher cores.
                         - Allowed values are 0,1,2,4,8,16.
                         - Field introduced in 18.2.7, 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>max_rules_per_lb:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Applicable to azure platform only.
                         - Maximum number of rules per azure lb.
                         - Field introduced in 17.2.12, 18.1.2.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 150.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>max_scaleout_per_vs:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Maximum number of active service engines for the virtual service.
                         - Allowed values are 1-64.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 4.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>max_se:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Maximum number of services engines in this group.
                         - Allowed values are 0-1000.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 10.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>max_vs_per_se:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Maximum number of virtual services that can be placed on a single service engine.
                         - Allowed values are 1-1000.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 10.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>mem_reserve:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Boolean flag to set mem_reserve.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>memory_for_config_update:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Indicates the percent of memory reserved for config updates.
                         - Allowed values are 0-100.
                         - Field introduced in 18.1.2.
                         - Unit is percent.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 15.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>memory_per_se:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Amount of memory for each of the service engine virtual machines.
                         - Changes to this setting do not affect existing ses.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 2048.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>mgmt_network_ref:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Management network to use for avi service engines.
                         - It is a reference to an object of type network.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>mgmt_subnet:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Management subnet to use for avi service engines.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>min_cpu_usage:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - When cpu usage on an se falls below the minimum threshold, virtual services hosted on the se may be consolidated onto other underutilized ses.
                         - After consolidation, unused service engines may then be eligible for deletion.
                         - Allowed values are 20-60.
                         - Unit is percent.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 30.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>min_scaleout_per_vs:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Minimum number of active service engines for the virtual service.
                         - Allowed values are 1-64.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>min_se:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Minimum number of services engines in this group (relevant for se autorebalance only).
                         - Allowed values are 0-1000.
                         - Field introduced in 17.2.13,18.1.3,18.2.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>minimum_connection_memory:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Indicates the percent of memory reserved for connections.
                         - Allowed values are 0-100.
                         - Field introduced in 18.1.2.
                         - Unit is percent.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 20.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>minimum_required_config_memory:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Required available config memory to apply any configuration.
                         - Allowed values are 0-90.
                         - Field deprecated in 18.1.2.
                         - Field introduced in 18.1.1.
                         - Unit is percent.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>n_log_streaming_threads:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of threads to use for log streaming.
                         - Allowed values are 1-100.
                         - Field introduced in 17.2.12, 18.1.2.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
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
                <b>nat_flow_tcp_closed_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Idle timeout in seconds for nat tcp flows in closed state.
                         - Allowed values are 1-3600.
                         - Field deprecated in 18.2.5.
                         - Field introduced in 18.2.5.
                         - Unit is seconds.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>nat_flow_tcp_established_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Idle timeout in seconds for nat tcp flows in established state.
                         - Allowed values are 1-3600.
                         - Field deprecated in 18.2.5.
                         - Field introduced in 18.2.5.
                         - Unit is seconds.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>nat_flow_tcp_half_closed_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Idle timeout in seconds for nat tcp flows in half closed state.
                         - Allowed values are 1-3600.
                         - Field deprecated in 18.2.5.
                         - Field introduced in 18.2.5.
                         - Unit is seconds.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>nat_flow_tcp_handshake_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Idle timeout in seconds for nat tcp flows in handshake state.
                         - Allowed values are 1-3600.
                         - Field deprecated in 18.2.5.
                         - Field introduced in 18.2.5.
                         - Unit is seconds.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>nat_flow_udp_noresponse_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Idle timeout in seconds for nat udp flows in noresponse state.
                         - Allowed values are 1-3600.
                         - Field deprecated in 18.2.5.
                         - Field introduced in 18.2.5.
                         - Unit is seconds.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>nat_flow_udp_response_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Idle timeout in seconds for nat udp flows in response state.
                         - Allowed values are 1-3600.
                         - Field deprecated in 18.2.5.
                         - Field introduced in 18.2.5.
                         - Unit is seconds.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>netlink_poller_threads:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of threads to poll for netlink messages excluding the thread for default namespace.
                         - Requires se reboot.
                         - Allowed values are 1-32.
                         - Field introduced in 20.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 2.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>netlink_sock_buf_size:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Socket buffer size for the netlink sockets.
                         - Requires se reboot.
                         - Allowed values are 1-128.
                         - Field introduced in 20.1.3.
                         - Unit is mega_bytes.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 4.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>non_significant_log_throttle:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - This setting limits the number of non-significant logs generated per second per core on this se.
                         - Default is 100 logs per second.
                         - Set it to zero (0) to deactivate throttling.
                         - Field introduced in 17.1.3.
                         - Unit is per_second.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 100.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ns_helper_deq_interval_msec:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Dequeue interval for receive queue from ns helper.
                         - Allowed values are 1-1000.
                         - Field introduced in 21.1.1.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 20.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>num_dispatcher_cores:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of dispatcher cores (0,1,2,4,8 or 16).
                         - If set to 0, then number of dispatcher cores is deduced automatically.requires se reboot.
                         - Allowed values are 0,1,2,4,8,16.
                         - Field introduced in 17.2.12, 18.1.3, 18.2.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>num_flow_cores_sum_changes_to_ignore:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of changes in num flow cores sum to ignore.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 8.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>objsync_config:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Configuration knobs for interse object distribution.
                         - Field introduced in 20.1.3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>objsync_port:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Tcp port on se management interface for interse object distribution.
                         - Supported only for externally managed security groups.
                         - Not supported on full access deployments.
                         - Requires se reboot.
                         - Field introduced in 20.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 9001.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>openstack_availability_zone:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Field deprecated in 17.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>openstack_availability_zones:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Field introduced in 17.1.1.
                         - Maximum of 5 items allowed.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>openstack_mgmt_network_name:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Avi management network name.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>openstack_mgmt_network_uuid:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Management network uuid.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>os_reserved_memory:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Amount of extra memory to be reserved for use by the operating system on a service engine.
                         - Unit is mb.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>pcap_tx_mode:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Determines the pcap transmit mode of operation.
                         - Requires se reboot.
                         - Enum options - PCAP_TX_AUTO, PCAP_TX_SOCKET, PCAP_TX_RING.
                         - Field introduced in 18.2.8, 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as PCAP_TX_AUTO.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>pcap_tx_ring_rd_balancing_factor:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - In pcap mode, reserve a configured portion of tx ring resources for itself and the remaining portion for the rx ring to achieve better balance in
                         - terms of queue depth.
                         - Requires se reboot.
                         - Allowed values are 10-100.
                         - Field introduced in 20.1.3.
                         - Unit is percent.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 10.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>per_app:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Per-app se mode is designed for deploying dedicated load balancers per app (vs).
                         - In this mode, each se is limited to a max of 2 vss.
                         - Vcpus in per-app ses count towards licensing usage at 25% rate.
                         - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>per_vs_admission_control:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable/disable per vs level admission control.enabling this feature will cause the connection and packet throttling on a particular vs that has
                         - high packet buffer consumption.
                         - Field introduced in 20.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>placement_mode:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - If placement mode is 'auto', virtual services are automatically placed on service engines.
                         - Enum options - PLACEMENT_MODE_AUTO.
                         - Default value when not specified in API or module is interpreted by Avi Controller as PLACEMENT_MODE_AUTO.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>realtime_se_metrics:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable or deactivate real time se metrics.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>reboot_on_panic:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Reboot the vm or host on kernel panic.
                         - Field introduced in 18.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>reboot_on_stop:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Reboot the system if the se is stopped.
                         - Field deprecated in 18.2.5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>resync_time_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Time interval to re-sync se's time with wall clock time.
                         - Allowed values are 8-600000.
                         - Field introduced in 20.1.1.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 65536.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_bandwidth_type:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Select the se bandwidth for the bandwidth license.
                         - Enum options - SE_BANDWIDTH_UNLIMITED, SE_BANDWIDTH_25M, SE_BANDWIDTH_200M, SE_BANDWIDTH_1000M, SE_BANDWIDTH_10000M.
                         - Field introduced in 17.2.5.
                         - Allowed in basic(allowed values- se_bandwidth_unlimited) edition, essentials(allowed values- se_bandwidth_unlimited) edition, enterprise edition.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_delayed_flow_delete:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Delay the cleanup of flowtable entry.
                         - To be used under surveillance of avi support.
                         - Field introduced in 20.1.2.
                         - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_deprovision_delay:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Duration to preserve unused service engine virtual machines before deleting them.
                         - If traffic to a virtual service were to spike up abruptly, this se would still be available to be utilized again rather than creating a new se.
                         - If this value is set to 0, controller will never delete any ses and administrator has to manually cleanup unused ses.
                         - Allowed values are 0-525600.
                         - Unit is min.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 120.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_dos_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Dosthresholdprofile settings for serviceenginegroup.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_dp_hm_drops:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Internal only.
                         - Used to simulate se - se hb failure.
                         - Field introduced in 20.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_dp_max_hb_version:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - The highest supported se-se heartbeat protocol version.
                         - This version is reported by secondary se to primary se in heartbeat response messages.
                         - Allowed values are 1-3.
                         - Field introduced in 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 2.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_dp_vnic_queue_stall_event_sleep:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Time (in seconds) service engine waits for after generating a vnic transmit queue stall event before resetting thenic.
                         - Field introduced in 18.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_dp_vnic_queue_stall_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of consecutive transmit failures to look for before generating a vnic transmit queue stall event.
                         - Field introduced in 18.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 2000.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_dp_vnic_queue_stall_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Time (in milliseconds) to wait for network/nic recovery on detecting a transmit queue stall after which service engine resets the nic.
                         - Field introduced in 18.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 10000.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_dp_vnic_restart_on_queue_stall_count:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of consecutive transmit queue stall events in se_dp_vnic_stall_se_restart_window to look for before restarting se.
                         - Field introduced in 18.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_dp_vnic_stall_se_restart_window:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Window of time (in seconds) during which se_dp_vnic_restart_on_queue_stall_count number of consecutive stalls results in a se restart.
                         - Field introduced in 18.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 3600.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_dpdk_pmd:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Determines if dpdk pool mode driver should be used or not   0  automatically determine based on hypervisor/nic type 1  unconditionally use dpdk
                         - poll mode driver 2  don't use dpdk poll mode driver.requires se reboot.
                         - Allowed values are 0-2.
                         - Field introduced in 18.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_flow_probe_retries:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Flow probe retry count if no replies are received.requires se reboot.
                         - Allowed values are 0-5.
                         - Field introduced in 18.1.4, 18.2.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 2.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_flow_probe_retry_timer:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Timeout in milliseconds for flow probe retries.requires se reboot.
                         - Allowed values are 20-50.
                         - Field introduced in 18.2.5.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 40.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_flow_probe_timer:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Timeout in milliseconds for flow probe entries.
                         - Allowed values are 10-200.
                         - Field deprecated in 18.2.5.
                         - Field introduced in 18.1.4, 18.2.1.
                         - Unit is milliseconds.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_group_analytics_policy:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Analytics policy for serviceenginegroup.
                         - Field introduced in 20.1.3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_hyperthreaded_mode:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Controls the distribution of se data path processes on cpus which support hyper-threading.
                         - Requires hyper-threading to be enabled at host level.
                         - Requires se reboot.
                         - For more details please refer to se placement kb.
                         - Enum options - SE_CPU_HT_AUTO, SE_CPU_HT_SPARSE_DISPATCHER_PRIORITY, SE_CPU_HT_SPARSE_PROXY_PRIORITY, SE_CPU_HT_PACKED_CORES.
                         - Field introduced in 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as SE_CPU_HT_AUTO.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_ip_encap_ipc:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Determines if se-se ipc messages are encapsulated in an ip header       0        automatically determine based on hypervisor type    1        use
                         - ip encap unconditionally    ~[0,1]   don't use ip encaprequires se reboot.
                         - Field introduced in 20.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_ipc_udp_port:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Udp port for se_dp ipc in docker bridge mode.
                         - Field deprecated in 20.1.1.
                         - Field introduced in 17.1.2.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_kni_burst_factor:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - This knob controls the resource availability and burst size used between se datapath and kni.
                         - This helps in minimising packet drops when there is higher kni traffic (non-vip traffic from and to linux).
                         - The factor takes the following values      0-default.
                         - 1-doubles the burst size and kni resources.
                         - 2-quadruples the burst size and kni resources.
                         - Allowed values are 0-2.
                         - Field introduced in 18.2.6.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_l3_encap_ipc:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Determines if se-se ipc messages use se interface ip instead of vip        0        automatically determine based on hypervisor type    1
                         - use se interface ip unconditionally    ~[0,1]   don't use se interface iprequires se reboot.
                         - Field introduced in 20.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_lro:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable or disable large receive optimization for vnics.
                         - Requires se reboot.
                         - Field introduced in 18.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_mp_ring_retry_count:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - The retry count for the multi-producer enqueue before yielding the cpu.
                         - To be used under surveillance of avi support.
                         - Field introduced in 20.1.3.
                         - Allowed in basic(allowed values- 500) edition, essentials(allowed values- 500) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 500.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_mtu:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Mtu for the vnics of ses in the se group.
                         - Allowed values are 512-9000.
                         - Field introduced in 18.2.8, 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_name_prefix:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Prefix to use for virtual machine name of service engines.
                         - Default value when not specified in API or module is interpreted by Avi Controller as Avi.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_pcap_lookahead:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enables lookahead mode of packet receive in pcap mode.
                         - Introduced to overcome an issue with hv_netvsc driver.
                         - Lookahead mode attempts to ensure that application and kernel's view of the receive rings are consistent.
                         - Field introduced in 18.2.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_pcap_pkt_count:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Max number of packets the pcap interface can hold and if the value is 0 the optimum value will be chosen.
                         - The optimum value will be chosen based on se-memory, cloud type and number of interfaces.requires se reboot.
                         - Field introduced in 18.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_pcap_pkt_sz:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Max size of each packet in the pcap interface.
                         - Requires se reboot.
                         - Field introduced in 18.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 69632.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_pcap_qdisc_bypass:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Bypass the kernel's traffic control layer, to deliver packets directly to the driver.
                         - Enabling this feature results in egress packets not being captured in host tcpdump.
                         - Note   brief packet reordering or loss may occur upon toggle.
                         - Field introduced in 18.2.6.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_pcap_reinit_frequency:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Frequency in seconds at which periodically a pcap reinit check is triggered.
                         - May be used in conjunction with the configuration pcap_reinit_threshold.
                         - (valid range   15 mins - 12 hours, 0 - disables).
                         - Allowed values are 900-43200.
                         - Special values are 0- 'disable'.
                         - Field introduced in 17.2.13, 18.1.3, 18.2.1.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_pcap_reinit_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Threshold for input packet receive errors in pcap mode exceeding which a pcap reinit is triggered.
                         - If not set, an unconditional reinit is performed.
                         - This value is checked every pcap_reinit_frequency interval.
                         - Field introduced in 17.2.13, 18.1.3, 18.2.1.
                         - Unit is metric_count.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_probe_port:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Tcp port on se where echo service will be run.
                         - Field introduced in 17.2.2.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 7.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_remote_punt_udp_port:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Udp port for punted packets in docker bridge mode.
                         - Field deprecated in 20.1.1.
                         - Field introduced in 17.1.2.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_rl_prop:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Rate limiter properties.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_routing:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable routing via service engine datapath.
                         - When disabled, routing is done by the linux kernel.
                         - Ip routing needs to be enabled in service engine group for se routing to be effective.
                         - Field deprecated in 18.2.5.
                         - Field introduced in 18.2.3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_rum_sampling_nav_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Minimum time to wait on server between taking sampleswhen sampling the navigation timing data from the end user client.
                         - Field introduced in 18.2.6.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_rum_sampling_nav_percent:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Percentage of navigation timing data from the end user client, used for sampling to get client insights.
                         - Field introduced in 18.2.6.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_rum_sampling_res_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Minimum time to wait on server between taking sampleswhen sampling the resource timing data from the end user client.
                         - Field introduced in 18.2.6.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 2.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_rum_sampling_res_percent:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Percentage of resource timing data from the end user client used for sampling to get client insight.
                         - Field introduced in 18.2.6.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 100.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_sb_dedicated_core:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Sideband traffic will be handled by a dedicated core.requires se reboot.
                         - Field introduced in 16.5.2, 17.1.9, 17.2.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_sb_threads:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of sideband threads per se.requires se reboot.
                         - Allowed values are 1-128.
                         - Field introduced in 16.5.2, 17.1.9, 17.2.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_thread_multiplier:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Multiplier for se threads based on vcpu.
                         - Allowed values are 1-10.
                         - Allowed in basic(allowed values- 1) edition, essentials(allowed values- 1) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_tracert_port_range:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Traceroute port range.
                         - Field introduced in 17.2.8.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_tunnel_mode:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Determines if direct secondary return (dsr) from secondary se is active or not  0  automatically determine based on hypervisor type.
                         - 1  enable tunnel mode - dsr is unconditionally disabled.
                         - 2  disable tunnel mode - dsr is unconditionally enabled.
                         - Tunnel mode can be enabled or disabled at run-time.
                         - Allowed values are 0-2.
                         - Field introduced in 17.1.1.
                         - Allowed in basic(allowed values- 0) edition, essentials(allowed values- 0) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_tunnel_udp_port:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Udp port for tunneled packets from secondary to primary se in docker bridge mode.requires se reboot.
                         - Field introduced in 17.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1550.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_tx_batch_size:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of packets to batch for transmit to the nic.
                         - Requires se reboot.
                         - Field introduced in 18.2.5.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 64.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_txq_threshold:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Once the tx queue of the dispatcher reaches this threshold, hardware queues are not polled for further packets.
                         - To be used under surveillance of avi support.
                         - Allowed values are 512-32768.
                         - Field introduced in 20.1.2.
                         - Allowed in basic(allowed values- 2048) edition, essentials(allowed values- 2048) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 2048.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_udp_encap_ipc:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Determines if se-se ipc messages are encapsulated in a udp header  0  automatically determine based on hypervisor type.
                         - 1  use udp encap unconditionally.requires se reboot.
                         - Allowed values are 0-1.
                         - Field introduced in 17.1.2.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_use_dpdk:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Determines if dpdk library should be used or not   0  automatically determine based on hypervisor type 1  use dpdk if pcap is not enabled 2
                         - don't use dpdk.
                         - Allowed values are 0-2.
                         - Field introduced in 18.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_vnic_tx_sw_queue_flush_frequency:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Configure the frequency in milliseconds of software transmit spillover queue flush when enabled.
                         - This is necessary to flush any packets in the spillover queue in the absence of a packet transmit in the normal course of operation.
                         - Allowed values are 50-500.
                         - Special values are 0- 'disable'.
                         - Field introduced in 20.1.1.
                         - Unit is milliseconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_vnic_tx_sw_queue_size:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Configure the size of software transmit spillover queue when enabled.
                         - Requires se reboot.
                         - Allowed values are 128-2048.
                         - Field introduced in 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 256.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_vs_hb_max_pkts_in_batch:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Maximum number of aggregated vs heartbeat packets to send in a batch.
                         - Allowed values are 1-256.
                         - Field introduced in 17.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 64.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_vs_hb_max_vs_in_pkt:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Maximum number of virtualservices for which heartbeat messages are aggregated in one packet.
                         - Allowed values are 1-1024.
                         - Field introduced in 17.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 256.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>self_se_election:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable ses to elect a primary amongst themselves in the absence of a connectivity to controller.
                         - Field introduced in 18.1.2.
                         - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>send_se_ready_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Timeout for sending se_ready without ns helper registration completion.
                         - Allowed values are 10-600.
                         - Field introduced in 21.1.1.
                         - Unit is seconds.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 300.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>service_ip6_subnets:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Ipv6 subnets assigned to the se group.
                         - Required for vs group placement.
                         - Field introduced in 18.1.1.
                         - Maximum of 128 items allowed.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>service_ip_subnets:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Subnets assigned to the se group.
                         - Required for vs group placement.
                         - Field introduced in 17.1.1.
                         - Maximum of 128 items allowed.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>shm_minimum_config_memory:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Minimum required shared memory to apply any configuration.
                         - Allowed values are 0-100.
                         - Field introduced in 18.1.2.
                         - Unit is mb.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 4.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>significant_log_throttle:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - This setting limits the number of significant logs generated per second per core on this se.
                         - Default is 100 logs per second.
                         - Set it to zero (0) to deactivate throttling.
                         - Field introduced in 17.1.3.
                         - Unit is per_second.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 100.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ssl_preprocess_sni_hostname:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - (beta) preprocess ssl client hello for sni hostname extension.if set to true, this will apply sni child's ssl protocol(s), if they are different
                         - from sni parent's allowed ssl protocol(s).
                         - Field introduced in 17.2.12, 18.1.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
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
                                     - It is a reference to an object of type tenant.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>transient_shared_memory_max:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - The threshold for the transient shared config memory in the se.
                         - Allowed values are 0-100.
                         - Field introduced in 20.1.1.
                         - Unit is percent.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 30.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>udf_log_throttle:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - This setting limits the number of udf logs generated per second per core on this se.
                         - Udf logs are generated due to the configured client log filters or the rules with logging enabled.
                         - Default is 100 logs per second.
                         - Set it to zero (0) to deactivate throttling.
                         - Field introduced in 17.1.3.
                         - Unit is per_second.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 100.
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
                <b>use_hyperthreaded_cores:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enables the use of hyper-threaded cores on se.
                         - Requires se reboot.
                         - Field introduced in 20.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>use_objsync:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable interse objsyc distribution framework.
                         - Field introduced in 20.1.3.
                         - Allowed in basic edition, essentials edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>use_standard_alb:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Use standard sku azure load balancer.
                         - By default cloud level flag is set.
                         - If not set, it inherits/uses the use_standard_alb flag from the cloud.
                         - Field introduced in 18.2.3.
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
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vcenter_clusters:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Vcenterclusters settings for serviceenginegroup.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vcenter_datastore_mode:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enum options - VCENTER_DATASTORE_ANY, VCENTER_DATASTORE_LOCAL, VCENTER_DATASTORE_SHARED.
                         - Default value when not specified in API or module is interpreted by Avi Controller as VCENTER_DATASTORE_ANY.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vcenter_datastores:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - List of vcenterdatastore.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vcenter_datastores_include:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Boolean flag to set vcenter_datastores_include.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vcenter_folder:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Folder to place all the service engine virtual machines in vcenter.
                         - Default value when not specified in API or module is interpreted by Avi Controller as AviSeFolder.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vcenter_hosts:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Vcenterhosts settings for serviceenginegroup.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vcenters:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Vcenter information for scoping at host/cluster level.
                         - Field introduced in 20.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vcpus_per_se:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Number of vcpus for each of the service engine virtual machines.
                         - Changes to this setting do not affect existing ses.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vip_asg:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - When vip_asg is set, vip configuration will be managed by avi.user will be able to configure vip_asg or vips individually at the time of create.
                         - Field introduced in 17.2.12, 18.1.2.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vnic_dhcp_ip_check_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Dhcp ip check interval.
                         - Allowed values are 1-1000.
                         - Field introduced in 21.1.1.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 6.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vnic_dhcp_ip_max_retries:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Dhcp ip max retries.
                         - Field introduced in 21.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 10.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vnic_ip_delete_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Wait interval before deleting ip.
                         - Field introduced in 21.1.1.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vnic_probe_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Probe vnic interval.
                         - Field introduced in 21.1.1.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vnic_rpc_retry_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Time interval for retrying the failed vnic rpc requests.
                         - Field introduced in 21.1.1.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vnicdb_cmd_history_size:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Size of vnicdb command history.
                         - Allowed values are 0-65535.
                         - Field introduced in 21.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 256.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vs_host_redundancy:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Ensure primary and secondary service engines are deployed on different physical hosts.
                         - Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.
                         - Special default for basic edition is true, essentials edition is true, enterprise is true.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vs_scalein_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Time to wait for the scaled in se to drain existing flows before marking the scalein done.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 30.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vs_scalein_timeout_for_upgrade:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - During se upgrade, time to wait for the scaled-in se to drain existing flows before marking the scalein done.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 30.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vs_scaleout_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Time to wait for the scaled out se to become ready before marking the scaleout done.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 600.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vs_se_scaleout_additional_wait_time:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Wait time for sending scaleout ready notification after virtual service is marked up.
                         - In certain deployments, there may be an additional delay to accept traffic.
                         - For example, for bgp, some time is needed for route advertisement.
                         - Allowed values are 0-20.
                         - Field introduced in 18.1.5,18.2.1.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vs_se_scaleout_ready_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Timeout in seconds for service engine to sendscaleout ready notification of a virtual service.
                         - Allowed values are 0-90.
                         - Field introduced in 18.1.5,18.2.1.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 60.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vs_switchover_timeout:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - During se upgrade in a legacy active/standby segroup, time to wait for the new primary se to accept flows before marking the switchover done.
                         - Field introduced in 17.2.13,18.1.4,18.2.1.
                         - Unit is sec.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 300.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vss_placement:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Parameters to place virtual services on only a subset of the cores of an se.
                         - Field introduced in 17.2.5.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vss_placement_enabled:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - If set, virtual services will be placed on only a subset of the cores of an se.
                         - Field introduced in 18.1.1.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>waf_learning_interval:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Frequency with which se publishes waf learning.
                         - Allowed values are 1-43200.
                         - Field deprecated in 18.2.3.
                         - Field introduced in 18.1.2.
                         - Unit is min.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>waf_learning_memory:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Amount of memory reserved on se for waf learning.
                         - This can be atmost 5% of se memory.
                         - Field deprecated in 18.2.3.
                         - Field introduced in 18.1.2.
                         - Unit is mb.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>waf_mempool:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Enable memory pool for waf.requires se reboot.
                         - Field introduced in 17.2.3.
                         - Default value when not specified in API or module is interpreted by Avi Controller as True.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>waf_mempool_size:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Memory pool size used for waf.requires se reboot.
                         - Field introduced in 17.2.3.
                         - Unit is kb.
                         - Default value when not specified in API or module is interpreted by Avi Controller as 64.
                                    </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    - name: Example to create ServiceEngineGroup object
      avi_serviceenginegroup:
        controller: 10.10.25.42
        username: admin
        password: something
        state: present
        name: sample_serviceenginegroup


Status
------


Authors
~~~~~~~

- Gaurav Rastogi (grastogi@avinetworks.com)
- Sandeep Bandi (sbandi@avinetworks.com)



