# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
lookup: avi
author: Eric Anderson <eanderson@avinetworks.com>
version_added: 2.8
short_description: Look up ``Avi`` objects.
description:
    - Given an object_type, fetch all the objects of that type or fetch
      the specific object that matches the name/uuid given via options.

options:
    obj_type:
        description:
            - type of object to query
        required: True
    obj_name:
        description:
            - name of the object to query
    obj_uuid:
        description:
            - UUID of the object to query
extends_documentation_fragment: avi
"""

EXAMPLES = """
- debug: msg="{{ lookup('avi', obj_type='virtualservice',
    tenant='admin', controller_ip='controller_ip', username='username', password='password') }}"
- debug: msg="{{ lookup('avi', obj_name='vs1', obj_type='virtualservice',
    tenant='admin', controller_ip='controller_ip', username='username', password='password') }}"
- debug: msg="{{ lookup('avi', obj_uuid='virtualservice-5c0e183a-690a-45d8-8d6f-88c30a52550d',
    obj_type='virtualservice', tenant='admin', controller_ip='controller_ip', username='username',
    password='password') }}"
"""

RETURN = """
 _list:
     description:
         - One ore more objects returned from ``Avi`` API.
     type: list
     elements: dictionary
"""

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display
from ansible.module_utils.networks.avi.avi_api import ApiSession

display = Display()


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        try:
            session_params = {
                'controller_ip': kwargs.get('controller_ip', None),
                'username': kwargs.get('username', None),
                'password': kwargs.get('password', None),
                'token': kwargs.get('token', None),
                'tenant': kwargs.get('tenant', None),
                'tenant_uuid': kwargs.get('tenant_uuid', None),
                'verify': kwargs.get('verify', None),
                'port': kwargs.get('port', None),
                'timeout': kwargs.get('timeout', None),
                'api_version': kwargs.get('api_version', None),
                'retry_conxn_errors': kwargs.get('retry_conxn_errors', None),
                'data_log': kwargs.get('data_log', None),
                'avi_credentials': kwargs.get('avi_credentials', None),
                'session_id': kwargs.get('session_id', None),
                'csrftoken': kwargs.get('csrftoken', None),
                'lazy_authentication': kwargs.get('lazy_authentication', None),
                'max_api_retries': kwargs.get('max_api_retries', None),
            }
            get_params = {
                'tenant': kwargs.get('tenant', None),
                'tenant_uuid': kwargs.get('tenant_uuid', None),
                'timeout': kwargs.get('timeout', None),
                'params': kwargs.get('params', None),
                'api_version': kwargs.get('api_version', None),
            }
            avi = ApiSession(**session_params)
            path = kwargs['obj_type']

            if kwargs.get('obj_name', None):
                name = kwargs['obj_name']
                response = [avi.get_object_by_name(path, name, **get_params)]
            elif kwargs.get('obj_uuid', None):
                obj_uuid = kwargs['obj_uuid']
                obj_path = "%s/%s" % (path, obj_uuid)
                response = [avi.get(obj_path, **get_params).json()]
            else:
                response = avi.get(path, **get_params).json().get('results', [])

        except AnsibleParserError:
            raise AnsibleError("Unable to query the Avi Controller")

        return response
