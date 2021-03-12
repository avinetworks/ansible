.. vmware.nsx_alb.avi_botconfigconsolidator:


*****************************
vmware.nsx_alb.avi_botconfigconsolidator
*****************************

**Module for setup of BotConfigConsolidator Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure BotConfigConsolidator object
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
                <b>description</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  Human-readable description of this consolidator.
                </div>
                                <div style="font-size: small">
                  Field introduced in 21.1.1.
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
                  The name of this consolidator.
                </div>
                                <div style="font-size: small">
                  Field introduced in 21.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>script</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  Script that consolidates results from all components.
                </div>
                                <div style="font-size: small">
                  Field introduced in 21.1.1.
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
                  The unique identifier of the tenant to which this mapping belongs.
                </div>
                                <div style="font-size: small">
                  It is a reference to an object of type tenant.
                </div>
                                <div style="font-size: small">
                  Field introduced in 21.1.1.
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
                  A unique identifier to this consolidator.
                </div>
                                <div style="font-size: small">
                  Field introduced in 21.1.1.
                </div>
                                            </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml
    - name: Example to create BotConfigConsolidator object
      vmware.nsx_alb.avi_botconfigconsolidator:
        controller: 192.168.15.18
        username: admin
        password: something
        state: present
        name: sample_botconfigconsolidator
Status
------

Authors
~~~~~~~
- Amol Shinde (samol@vmware.com)



