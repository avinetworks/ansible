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
.. vmware.nsx_alb.avi_applicationprofile:


*****************************
vmware.nsx_alb.avi_applicationprofile
*****************************

**Module for setup of ApplicationProfile Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure ApplicationProfile object
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
                <b>cloud_config_cksum:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Checksum of application profiles.
                         - Internally set by cloud connector.
                         - Field introduced in 17.2.14, 18.1.5, 18.2.1.
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
                                     - Name of the application profile creator.
                         - Field introduced in 17.2.14, 18.1.5, 18.2.1.
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
                <b>dns_service_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Specifies various dns service related controls for virtual service.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dos_rl_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Specifies various security related controls for virtual service.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>http_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Specifies the http application proxy profile parameters.
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
                                     - The name of the application profile.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>preserve_client_ip:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Specifies if client ip needs to be preserved for backend connection.
                         - Not compatible with connection multiplexing.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>preserve_client_port:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Specifies if we need to preserve client port while preserving client ip for backend connections.
                         - Field introduced in 17.2.7.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>preserve_dest_ip_port:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Specifies if destination ip and port needs to be preserved for backend connection.
                         - Field introduced in 20.1.1.
                         - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                         - Default value when not specified in API or module is interpreted by Avi Controller as False.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sip_service_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Specifies various sip service related controls for virtual service.
                         - Field introduced in 17.2.8, 18.1.3, 18.2.1.
                         - Allowed in basic edition, essentials edition, enterprise edition.
                                    </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tcp_app_profile:</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                </td>
            <td>
                                     - Specifies the tcp application proxy profile parameters.
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
                                     - Specifies which application layer proxy is enabled for the virtual service.
                         - Enum options - APPLICATION_PROFILE_TYPE_L4, APPLICATION_PROFILE_TYPE_HTTP, APPLICATION_PROFILE_TYPE_SYSLOG, APPLICATION_PROFILE_TYPE_DNS,
                         - APPLICATION_PROFILE_TYPE_SSL, APPLICATION_PROFILE_TYPE_SIP.
                         - Allowed in basic(allowed values- application_profile_type_l4,application_profile_type_http) edition, essentials(allowed values-
                         - application_profile_type_l4) edition, enterprise edition.
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
                                     - Uuid of the application profile.
                                    </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    
  - name: Create an Application Profile for HTTP application enabled for SSL traffic
    avi_applicationprofile:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      http_profile:
        cache_config:
          age_header: true
          aggressive: false
          date_header: true
          default_expire: 600
          enabled: false
          heuristic_expire: false
          max_cache_size: 0
          max_object_size: 4194304
          mime_types_group_refs:
          - admin:System-Cacheable-Resource-Types
          min_object_size: 100
          query_cacheable: false
          xcache_header: true
        client_body_timeout: 0
        client_header_timeout: 10000
        client_max_body_size: 0
        client_max_header_size: 12
        client_max_request_size: 48
        compression_profile:
          compressible_content_ref: admin:System-Compressible-Content-Types
          compression: false
          remove_accept_encoding_header: true
          type: AUTO_COMPRESSION
        connection_multiplexing_enabled: true
        hsts_enabled: false
        hsts_max_age: 365
        http_to_https: false
        httponly_enabled: false
        keepalive_header: false
        keepalive_timeout: 30000
        max_bad_rps_cip: 0
        max_bad_rps_cip_uri: 0
        max_bad_rps_uri: 0
        max_rps_cip: 0
        max_rps_cip_uri: 0
        max_rps_unknown_cip: 0
        max_rps_unknown_uri: 0
        max_rps_uri: 0
        post_accept_timeout: 30000
        secure_cookie_enabled: false
        server_side_redirect_to_https: false
        spdy_enabled: false
        spdy_fwd_proxy_mode: false
        ssl_client_certificate_mode: SSL_CLIENT_CERTIFICATE_NONE
        ssl_everywhere_enabled: false
        websockets_enabled: true
        x_forwarded_proto_enabled: false
        xff_alternate_name: X-Forwarded-For
        xff_enabled: true
      name: System-HTTP
      tenant_ref: /api/tenant?name=admin
      type: APPLICATION_PROFILE_TYPE_HTTP



Status
------


Authors
~~~~~~~

- Gaurav Rastogi (grastogi@avinetworks.com)
- Sandeep Bandi (sbandi@avinetworks.com)



