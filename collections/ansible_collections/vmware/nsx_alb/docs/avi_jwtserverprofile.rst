.. vmware.nsx_alb.avi_jwtserverprofile:


*****************************
vmware.nsx_alb.avi_jwtserverprofile
*****************************

**Module for setup of JWTServerProfile Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure JWTServerProfile object
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
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <div style="font-size: small">
                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                        <li>absent</li>
                        <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                    </ul>
                </div>
            </td>
            <td>
                <div style="font-size: small">
                    The state that should be applied on the entity.
                </div>
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
                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                        <li><div style="color: blue"><b>put</b>&nbsp;&larr;</div></li>
                        <li>patch</li>
                    </ul>
                </div>
            </td>
            <td>
                <div style="font-size: small">
                    Default method for object update is HTTP PUT.
                </div>
                <div style="font-size: small">
                    Setting to patch will override that behavior to use HTTP PATCH.
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
                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                        <li><div style="color: blue"><b>add</b>&nbsp;&larr;</div></li>
                        <li>replace</li>
                        <li>delete</li>
                    </ul>
                </div>
            </td>
            <td>
                <div style="font-size: small">
                    Patch operation to use when using avi_api_update_method as patch.
                </div>
            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>issuer</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  Uniquely identifiable name of the token issuer.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.3.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>jwks_keys</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  Jwks key set used for validating the jwt.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.3.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  Name of the jwt profile.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.3.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tenant_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  Uuid of the tenant.
                </div>
                                <div style="font-size: small">
                  It is a reference to an object of type tenant.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.3.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>url</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  Avi controller URL of the object.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>uuid</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  Uuid of the jwtprofile.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.3.
                </div>
                                            </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml
    - name: Example to create JWTServerProfile object
      vmware.nsx_alb.avi_jwtserverprofile:
        controller: 192.168.15.18
        username: admin
        password: something
        state: present
        name: sample_jwtserverprofile
Status
------

Authors
~~~~~~~
- Amol Shinde (samol@vmware.com)



