.. vmware.nsx_alb.avi_pingaccessagent:


*****************************
vmware.nsx_alb.avi_pingaccessagent
*****************************

**Module for setup of PingAccessAgent Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure PingAccessAgent object
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
                 - Field introduced in 18.2.3.
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
                 - Name of the pingaccess agent.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.3.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>pingaccess_pool_ref:</b>
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
                 - Pool containing a primary pingaccess server, as well as any failover servers included in the agent.properties file.
                </div><br>
                                <div style="font-size: small">
                 - It is a reference to an object of type pool.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.3.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>primary_server:</b>
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
                                                <div style="font-size: small">
                 - The ip and port of the primary pingaccess server.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.3.
                </div><br>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>properties_file_data:</b>
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
                 - Pingaccessagent's agent.properties file generated by pingaccess server.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.3.
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
                                <div style="font-size: small">
                 - Field introduced in 18.2.3.
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
                 - Uuid of the pingaccess agent.
                </div><br>
                                <div style="font-size: small">
                 - Field introduced in 18.2.3.
                </div><br>
                                            </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    - name: Example to create PingAccessAgent object
      avi_pingaccessagent:
        controller: 10.10.25.42
        username: admin
        password: something
        state: present
        name: sample_pingaccessagent


Status
------


Authors
~~~~~~~

- Gaurav Rastogi (grastogi@avinetworks.com)
- Sandeep Bandi (sbandi@avinetworks.com)



