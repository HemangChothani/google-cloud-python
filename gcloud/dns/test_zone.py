# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest2


class TestManagedZone(unittest2.TestCase):
    PROJECT = 'project'
    ZONE_NAME = 'zone-name'
    DESCRIPTION = 'ZONE DESCRIPTION'
    DNS_NAME = 'test.example.com'

    def _getTargetClass(self):
        from gcloud.dns.zone import ManagedZone
        return ManagedZone

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def _setUpConstants(self):
        import datetime
        import os
        import time
        from gcloud._helpers import UTC

        self.WHEN_TS = time.time()
        self.WHEN = datetime.datetime.utcfromtimestamp(self.WHEN_TS).replace(
            tzinfo=UTC)
        self.ZONE_ID = os.getpid()

    def _makeResource(self):
        self._setUpConstants()
        return {
            'name': self.ZONE_NAME,
            'dnsName': self.DNS_NAME,
            'description': self.DESCRIPTION,
            'id': self.ZONE_ID,
            'creationTime': self.WHEN_TS * 1000,
            'nameServers': [
                'ns-cloud1.googledomains.com',
                'ns-cloud2.googledomains.com',
            ],
        }

    def _verifyReadonlyResourceProperties(self, zone, resource):

        self.assertEqual(zone.zone_id, resource.get('id'))

        if 'creationTime' in resource:
            self.assertEqual(zone.created, self.WHEN)
        else:
            self.assertEqual(zone.created, None)

        if 'nameServers' in resource:
            self.assertEqual(zone.name_servers, resource['nameServers'])
        else:
            self.assertEqual(zone.name_servers, None)

    def _verifyResourceProperties(self, zone, resource):

        self._verifyReadonlyResourceProperties(zone, resource)

        self.assertEqual(zone.name, resource.get('name'))
        self.assertEqual(zone.dns_name, resource.get('dnsName'))
        self.assertEqual(zone.description, resource.get('description'))
        self.assertEqual(zone.zone_id, resource.get('id'))
        self.assertEqual(zone.name_server_set, resource.get('nameServerSet'))

    def test_ctor(self):
        client = _Client(self.PROJECT)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client)
        self.assertEqual(zone.name, self.ZONE_NAME)
        self.assertEqual(zone.dns_name, self.DNS_NAME)
        self.assertTrue(zone._client is client)
        self.assertEqual(zone.project, client.project)
        self.assertEqual(
            zone.path,
            '/projects/%s/managedZones/%s' % (self.PROJECT, self.ZONE_NAME))

        self.assertEqual(zone.zone_id, None)
        self.assertEqual(zone.created, None)

        self.assertEqual(zone.description, None)

    def test_from_api_repr_missing_identity(self):
        self._setUpConstants()
        client = _Client(self.PROJECT)
        RESOURCE = {}
        klass = self._getTargetClass()
        with self.assertRaises(KeyError):
            klass.from_api_repr(RESOURCE, client=client)

    def test_from_api_repr_bare(self):
        self._setUpConstants()
        client = _Client(self.PROJECT)
        RESOURCE = {
            'name': self.ZONE_NAME,
            'dnsName': self.DNS_NAME,
        }
        klass = self._getTargetClass()
        zone = klass.from_api_repr(RESOURCE, client=client)
        self.assertTrue(zone._client is client)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_from_api_repr_w_properties(self):
        self._setUpConstants()
        client = _Client(self.PROJECT)
        RESOURCE = self._makeResource()
        klass = self._getTargetClass()
        zone = klass.from_api_repr(RESOURCE, client=client)
        self.assertTrue(zone._client is client)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_description_setter_bad_value(self):
        client = _Client(self.PROJECT)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client)
        with self.assertRaises(ValueError):
            zone.description = 12345

    def test_description_setter(self):
        client = _Client(self.PROJECT)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client)
        zone.description = 'DESCRIPTION'
        self.assertEqual(zone.description, 'DESCRIPTION')

    def test_name_server_set_setter_bad_value(self):
        client = _Client(self.PROJECT)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client)
        with self.assertRaises(ValueError):
            zone.name_server_set = 12345

    def test_name_server_set_setter(self):
        client = _Client(self.PROJECT)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client)
        zone.name_server_set = 'NAME_SERVER_SET'
        self.assertEqual(zone.name_server_set, 'NAME_SERVER_SET')

    def test_create_w_bound_client(self):
        PATH = 'projects/%s/managedZones' % self.PROJECT
        RESOURCE = self._makeResource()
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client)

        zone.create()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'POST')
        self.assertEqual(req['path'], '/%s' % PATH)
        SENT = {
            'name': self.ZONE_NAME,
            'dnsName': self.DNS_NAME,
        }
        self.assertEqual(req['data'], SENT)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_create_w_alternate_client(self):
        PATH = 'projects/%s/managedZones' % self.PROJECT
        DESCRIPTION = 'DESCRIPTION'
        NAME_SERVER_SET = 'NAME_SERVER_SET'
        RESOURCE = self._makeResource()
        RESOURCE['nameServerSet'] = NAME_SERVER_SET
        RESOURCE['description'] = DESCRIPTION
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client1)
        zone.name_server_set = NAME_SERVER_SET
        zone.description = DESCRIPTION

        zone.create(client=client2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req['method'], 'POST')
        self.assertEqual(req['path'], '/%s' % PATH)
        SENT = {
            'name': self.ZONE_NAME,
            'dnsName': self.DNS_NAME,
            'nameServerSet': NAME_SERVER_SET,
            'description': DESCRIPTION,
        }
        self.assertEqual(req['data'], SENT)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_create_w_missing_output_properties(self):
        # In the wild, the resource returned from 'zone.create' sometimes
        # lacks 'creationTime' / 'lastModifiedTime'
        PATH = 'projects/%s/managedZones' % (self.PROJECT,)
        RESOURCE = self._makeResource()
        del RESOURCE['creationTime']
        del RESOURCE['id']
        del RESOURCE['nameServers']
        self.WHEN = None
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client)

        zone.create()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'POST')
        self.assertEqual(req['path'], '/%s' % PATH)
        SENT = {
            'name': self.ZONE_NAME,
            'dnsName': self.DNS_NAME,
        }
        self.assertEqual(req['data'], SENT)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_exists_miss_w_bound_client(self):
        PATH = 'projects/%s/managedZones/%s' % (self.PROJECT, self.ZONE_NAME)
        conn = _Connection()
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client)

        self.assertFalse(zone.exists())

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'GET')
        self.assertEqual(req['path'], '/%s' % PATH)
        self.assertEqual(req['query_params'], {'fields': 'id'})

    def test_exists_hit_w_alternate_client(self):
        PATH = 'projects/%s/managedZones/%s' % (self.PROJECT, self.ZONE_NAME)
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection({})
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client1)

        self.assertTrue(zone.exists(client=client2))

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req['method'], 'GET')
        self.assertEqual(req['path'], '/%s' % PATH)
        self.assertEqual(req['query_params'], {'fields': 'id'})

    def test_reload_w_bound_client(self):
        PATH = 'projects/%s/managedZones/%s' % (self.PROJECT, self.ZONE_NAME)
        RESOURCE = self._makeResource()
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client)

        zone.reload()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'GET')
        self.assertEqual(req['path'], '/%s' % PATH)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_reload_w_alternate_client(self):
        PATH = 'projects/%s/managedZones/%s' % (self.PROJECT, self.ZONE_NAME)
        RESOURCE = self._makeResource()
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client1)

        zone.reload(client=client2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req['method'], 'GET')
        self.assertEqual(req['path'], '/%s' % PATH)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_delete_w_bound_client(self):
        PATH = 'projects/%s/managedZones/%s' % (self.PROJECT, self.ZONE_NAME)
        conn = _Connection({})
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client)

        zone.delete()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req['method'], 'DELETE')
        self.assertEqual(req['path'], '/%s' % PATH)

    def test_delete_w_alternate_client(self):
        PATH = 'projects/%s/managedZones/%s' % (self.PROJECT, self.ZONE_NAME)
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection({})
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = self._makeOne(self.ZONE_NAME, self.DNS_NAME, client1)

        zone.delete(client=client2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req['method'], 'DELETE')
        self.assertEqual(req['path'], '/%s' % PATH)


class _Client(object):

    def __init__(self, project='project', connection=None):
        self.project = project
        self.connection = connection


class _Connection(object):

    def __init__(self, *responses):
        self._responses = responses
        self._requested = []

    def api_request(self, **kw):
        from gcloud.exceptions import NotFound
        self._requested.append(kw)

        try:
            response, self._responses = self._responses[0], self._responses[1:]
        except:
            raise NotFound('miss')
        else:
            return response
