from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
import os
import unittest
# from ansible_collections.avinetworks.avisdk.tests.unit.compat import unittest
from ansible_collections.vmware.nsx_alb.tests.unit.compat.mock import Mock
from ansible_collections.vmware.nsx_alb.tests.unit.modules.utils import set_module_args
from ansible_collections.vmware.nsx_alb.plugins.modules import avi_pool

fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
with open(fixture_path + '/avi_pool.json') as json_file:
    data = json.load(json_file)

class TestAviCloud(unittest.TestCase):

    def test_create_pool(self):
        set_module_args({
            "avi_credentials": {
                "controller": "10.79.168.139",
                "username": "admin",
                "password": "avi123",
                "api_version": "21.1.1"
            },
            "state": "present",
            "name": "testpool1",
            "description": "testpool1",
            "health_monitor_refs": [
                "/api/healthmonitor?name=System-HTTP"
            ],
            "servers": [
                {
                    "ip": {
                        "addr": "10.10.2.20",
                        "type": "V4"
                    }
                },
                {
                    "ip": {
                        "addr": "10.10.2.21",
                        "type": "V4"
                    }
                }
            ]
        })
        avi_pool.avi_ansible_api = Mock(return_value=data['mock_create_resp'])
        response = avi_pool.main()
        assert response['changed']

    def test_put_on_pool(self):
        set_module_args({
            "avi_credentials": {
                "controller": "10.79.168.139",
                "username": "admin",
                "password": "avi123",
                "api_version": "21.1.1"
            },
            "state": "present",
            "avi_api_update_method": "patch",
            "avi_api_patch_op": "replace",
            "uuid": "pool-7d5dc50b-5624-4992-a69a-eb2f0770cd65",
            "name": "testpool1",
            "description": "testpool1",
            "health_monitor_refs": [
                "/api/healthmonitor?name=System-HTTP"
            ],
            "servers": [
                {
                    "ip": {
                        "addr": "10.10.2.20",
                        "type": "V4"
                    }
                },
                {
                    "ip": {
                        "addr": "10.10.2.22",
                        "type": "V4"
                    }
                }
            ]
        })
        avi_pool.avi_ansible_api = Mock(return_value=data['mock_update_resp'])
        response = avi_pool.main()
        print(response)
        assert response['changed']
        assert response['obj']
        assert response['old_obj']

    def test_delete_pool(self):
        set_module_args({
            "avi_credentials": {
                "controller": "10.79.168.139",
                "username": "admin",
                "password": "avi123",
                "api_version": "21.1.1"

            },
            "uuid": "pool-7d5dc50b-5624-4992-a69a-eb2f0770cd65",
            "state": "absent",
            "name": "testpool1"
        })
        avi_pool.avi_ansible_api = Mock(return_value=data['mock_delete_resp'])
        response = avi_pool.main()
        assert response['changed']
        assert not response['obj']
        assert response['old_obj']
