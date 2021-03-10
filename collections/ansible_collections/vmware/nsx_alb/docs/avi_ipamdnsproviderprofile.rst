#!/usr/bin/python3
#
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
#
# Copyright: (c) 2017 Gaurav Rastogi, <grastogi@avinetworks.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
.. vmware.nsx_alb.avi_ipamdnsproviderprofile:


*****************************
vmware.nsx_alb.avi_ipamdnsproviderprofile
*****************************

**Module for setup of IpamDnsProviderProfile Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure IpamDnsProviderProfile object
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
                <b>allocate_ip_in_vrf:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - If this flag is set, only allocate ip from networks in the virtual service vrf.
                         - Applicable for avi vantage ipam only.
                         - Field introduced in 17.2.4.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>aws_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Provider details if type is aws.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>azure_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Provider details if type is microsoft azure.
                         - Field introduced in 17.2.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>custom_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Provider details if type is custom.
                         - Field introduced in 17.1.1.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>gcp_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Provider details if type is google cloud.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>infoblox_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Provider details if type is infoblox.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>internal_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Provider details if type is avi.
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
                                     - Name for the ipam/dns provider profile.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>oci_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Provider details for oracle cloud.
                         - Field introduced in 18.2.1,18.1.3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>openstack_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Provider details if type is openstack.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>proxy_configuration:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Field introduced in 17.1.1.
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
                <b>tencent_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Provider details for tencent cloud.
                         - Field introduced in 18.2.3.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>type:</b>
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
                                     - Provider type for the ipam/dns provider profile.
                         - Enum options - IPAMDNS_TYPE_INFOBLOX, IPAMDNS_TYPE_AWS, IPAMDNS_TYPE_OPENSTACK, IPAMDNS_TYPE_GCP, IPAMDNS_TYPE_INFOBLOX_DNS, IPAMDNS_TYPE_CUSTOM,
                         - IPAMDNS_TYPE_CUSTOM_DNS, IPAMDNS_TYPE_AZURE, IPAMDNS_TYPE_OCI, IPAMDNS_TYPE_TENCENT, IPAMDNS_TYPE_INTERNAL, IPAMDNS_TYPE_INTERNAL_DNS,
                         - IPAMDNS_TYPE_AWS_DNS, IPAMDNS_TYPE_AZURE_DNS.
                         - Allowed in basic(allowed values- ipamdns_type_internal) edition, essentials(allowed values- ipamdns_type_internal) edition, enterprise edition.
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
                                     - Uuid of the ipam/dns provider profile.
                                    </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    
  - name: Create IPAM DNS provider setting
    avi_ipamdnsproviderprofile:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      internal_profile:
        dns_service_domain:
        - domain_name: ashish.local
          num_dns_ip: 1
          pass_through: true
          record_ttl: 100
        - domain_name: guru.local
          num_dns_ip: 1
          pass_through: true
          record_ttl: 200
        ttl: 300
      name: Ashish-DNS
      tenant_ref: /api/tenant?name=Demo
      type: IPAMDNS_TYPE_INTERNAL



Status
------


Authors
~~~~~~~

- Gaurav Rastogi (grastogi@avinetworks.com)
- Sandeep Bandi (sbandi@avinetworks.com)



