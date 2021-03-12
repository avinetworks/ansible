.. vmware.nsx_alb.avi_ipreputationdb:


*****************************
vmware.nsx_alb.avi_ipreputationdb
*****************************

**Module for setup of IPReputationDB Avi RESTful Object**


Version added: "1.0.0"

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure IPReputationDB object
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
                <b>base_file_refs</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  Ip reputation db base file.
                </div>
                                <div style="font-size: small">
                  It is a reference to an object of type fileobject.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  Maximum of 1 items allowed.
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
                  Description.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>incremental_file_refs</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  Ip reputation db incremental update files.
                </div>
                                <div style="font-size: small">
                  It is a reference to an object of type fileobject.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>labels</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  Key value pairs for granular object access control.
                </div>
                                <div style="font-size: small">
                  Also allows for classification and tagging of similar objects.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.2.
                </div>
                                <div style="font-size: small">
                  Maximum of 4 items allowed.
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
                  Ip reputation db name.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>service_status</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  If this object is managed by the ip reputation service, this field contain the status of this syncronization.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.1.
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
                  Tenant that this object belongs to.
                </div>
                                <div style="font-size: small">
                  It is a reference to an object of type tenant.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.1.
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
                  Uuid of this object.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vendor</b>
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
                  Organization providing ip reputation data.
                </div>
                                <div style="font-size: small">
                  Enum options - IP_REPUTATION_VENDOR_WEBROOT.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>version</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  A version number for this database object.
                </div>
                                <div style="font-size: small">
                  This is informal for the consumer of this api only, a tool which manages this object can store version information here.
                </div>
                                <div style="font-size: small">
                  Field introduced in 20.1.1.
                </div>
                                            </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml
    - name: Example to create IPReputationDB object
      vmware.nsx_alb.avi_ipreputationdb:
        controller: 192.168.15.18
        username: admin
        password: something
        state: present
        name: sample_ipreputationdb
Status
------

Authors
~~~~~~~
- Amol Shinde (samol@vmware.com)



