# Copyright 2014 Google Inc.
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

"""Connections to Google Cloud Datastore API servers."""

import os

from google.rpc import status_pb2

from google.cloud import _http as connection_module
from google.cloud.environment_vars import DISABLE_GRPC
from google.cloud import exceptions
from google.cloud.proto.datastore.v1 import datastore_pb2 as _datastore_pb2

from google.cloud.datastore import __version__
try:
    from google.cloud.datastore._gax import _DatastoreAPIOverGRPC
    _HAVE_GRPC = True
except ImportError:  # pragma: NO COVER
    _DatastoreAPIOverGRPC = None
    _HAVE_GRPC = False


DATASTORE_API_HOST = 'datastore.googleapis.com'
"""Datastore API request host."""
API_BASE_URL = 'https://' + DATASTORE_API_HOST
"""The base of the API call URL."""
API_VERSION = 'v1'
"""The version of the API, used in building the API call's URL."""
API_URL_TEMPLATE = ('{api_base}/{api_version}/projects'
                    '/{project}:{method}')
"""A template for the URL of a particular API call."""

_DISABLE_GRPC = os.getenv(DISABLE_GRPC, False)
_USE_GRPC = _HAVE_GRPC and not _DISABLE_GRPC
_CLIENT_INFO = connection_module.CLIENT_INFO_TEMPLATE.format(__version__)


def _request(http, project, method, data, base_url):
    """Make a request over the Http transport to the Cloud Datastore API.

    :type http: :class:`~httplib2.Http`
    :param http: HTTP object to make requests.

    :type project: str
    :param project: The project to make the request for.

    :type method: str
    :param method: The API call method name (ie, ``runQuery``,
                   ``lookup``, etc)

    :type data: str
    :param data: The data to send with the API call.
                 Typically this is a serialized Protobuf string.

    :type base_url: str
    :param base_url: The base URL where the API lives.

    :rtype: str
    :returns: The string response content from the API call.
    :raises: :class:`google.cloud.exceptions.GoogleCloudError` if the
             response code is not 200 OK.
    """
    headers = {
        'Content-Type': 'application/x-protobuf',
        'Content-Length': str(len(data)),
        'User-Agent': connection_module.DEFAULT_USER_AGENT,
        connection_module.CLIENT_INFO_HEADER: _CLIENT_INFO,
    }
    api_url = build_api_url(project, method, base_url)
    headers, content = http.request(
        uri=api_url, method='POST', headers=headers, body=data)

    status = headers['status']
    if status != '200':
        error_status = status_pb2.Status.FromString(content)
        raise exceptions.make_exception(
            headers, error_status.message, use_json=False)

    return content


def _rpc(http, project, method, base_url, request_pb, response_pb_cls):
    """Make a protobuf RPC request.

    :type http: :class:`~httplib2.Http`
    :param http: HTTP object to make requests.

    :type project: str
    :param project: The project to connect to. This is
                    usually your project name in the cloud console.

    :type method: str
    :param method: The name of the method to invoke.

    :type base_url: str
    :param base_url: The base URL where the API lives.

    :type request_pb: :class:`google.protobuf.message.Message` instance
    :param request_pb: the protobuf instance representing the request.

    :type response_pb_cls: A :class:`google.protobuf.message.Message`
                           subclass.
    :param response_pb_cls: The class used to unmarshall the response
                            protobuf.

    :rtype: :class:`google.protobuf.message.Message`
    :returns: The RPC message parsed from the response.
    """
    req_data = request_pb.SerializeToString()
    response = _request(
        http, project, method, req_data, base_url)
    return response_pb_cls.FromString(response)


def build_api_url(project, method, base_url):
    """Construct the URL for a particular API call.

    This method is used internally to come up with the URL to use when
    making RPCs to the Cloud Datastore API.

    :type project: str
    :param project: The project to connect to. This is
                    usually your project name in the cloud console.

    :type method: str
    :param method: The API method to call (e.g. 'runQuery', 'lookup').

    :type base_url: str
    :param base_url: The base URL where the API lives.

    :rtype: str
    :returns: The API URL created.
    """
    return API_URL_TEMPLATE.format(
        api_base=base_url, api_version=API_VERSION,
        project=project, method=method)


class _DatastoreAPIOverHttp(object):
    """Helper mapping datastore API methods.

    Makes requests to send / receive protobuf content over HTTP/1.1.

    Methods make bare API requests without any helpers for constructing
    the requests or parsing the responses.

    :type connection: :class:`Connection`
    :param connection: A connection object that contains helpful
                       information for making requests.
    """

    def __init__(self, connection):
        self.connection = connection

    def lookup(self, project, request_pb):
        """Perform a ``lookup`` request.

        :type project: str
        :param project: The project to connect to. This is
                        usually your project name in the cloud console.

        :type request_pb: :class:`.datastore_pb2.LookupRequest`
        :param request_pb: The request protobuf object.

        :rtype: :class:`.datastore_pb2.LookupResponse`
        :returns: The returned protobuf response object.
        """
        return _rpc(self.connection.http, project, 'lookup',
                    self.connection.api_base_url,
                    request_pb, _datastore_pb2.LookupResponse)


class Connection(connection_module.Connection):
    """A connection to the Google Cloud Datastore via the Protobuf API.

    This class should understand only the basic types (and protobufs)
    in method arguments, however it should be capable of returning advanced
    types.

    :type client: :class:`~google.cloud.datastore.client.Client`
    :param client: The client that owns the current connection.
    """

    def __init__(self, client):
        super(Connection, self).__init__(client)
        self.api_base_url = client._base_url
        if _USE_GRPC:
            self._datastore_api = _DatastoreAPIOverGRPC(self)
        else:
            self._datastore_api = _DatastoreAPIOverHttp(self)

    def lookup(self, project, key_pbs,
               eventual=False, transaction_id=None):
        """Lookup keys from a project in the Cloud Datastore.

        Maps the ``DatastoreService.Lookup`` protobuf RPC.

        This uses mostly protobufs
        (:class:`.entity_pb2.Key` as input and :class:`.entity_pb2.Entity`
        as output). It is used under the hood in
        :meth:`Client.get() <.datastore.client.Client.get>`:

        .. code-block:: python

          >>> from google.cloud import datastore
          >>> client = datastore.Client(project='project')
          >>> key = client.key('MyKind', 1234)
          >>> client.get(key)
          [<Entity object>]

        Using a :class:`Connection` directly:

        .. code-block:: python

          >>> connection.lookup('project', [key.to_protobuf()])
          [<Entity protobuf>]

        :type project: str
        :param project: The project to look up the keys in.

        :type key_pbs: list of
                       :class:`.entity_pb2.Key`
        :param key_pbs: The keys to retrieve from the datastore.

        :type eventual: bool
        :param eventual: If False (the default), request ``STRONG`` read
                         consistency.  If True, request ``EVENTUAL`` read
                         consistency.

        :type transaction_id: str
        :param transaction_id: If passed, make the request in the scope of
                               the given transaction.  Incompatible with
                               ``eventual==True``.

        :rtype: :class:`.datastore_pb2.LookupResponse`
        :returns: The returned protobuf for the lookup request.
        """
        lookup_request = _datastore_pb2.LookupRequest(keys=key_pbs)
        _set_read_options(lookup_request, eventual, transaction_id)
        return self._datastore_api.lookup(project, lookup_request)


class HTTPDatastoreAPI(object):
    """An API object that sends proto-over-HTTP requests.

    Intended to provide the same methods as the GAPIC ``DatastoreClient``.

    :type client: :class:`~google.cloud.datastore.client.Client`
    :param client: The client that provides configuration.
    """

    def __init__(self, client):
        self.client = client

    def run_query(self, project, partition_id, read_options,
                  query=None, gql_query=None):
        """Perform a ``runQuery`` request.

        :type project: str
        :param project: The project to connect to. This is
                        usually your project name in the cloud console.

        :type partition_id: :class:`.entity_pb2.PartitionId`
        :param partition_id: Partition ID corresponding to an optional
                             namespace and project ID.

        :type read_options: :class:`.datastore_pb2.ReadOptions`
        :param read_options: The options for this query. Contains a
                             either the transaction for the read or
                             ``STRONG`` or ``EVENTUAL`` read consistency.

        :type query: :class:`.query_pb2.Query`
        :param query: (Optional) The query protobuf to run. At most one of
                      ``query`` and ``gql_query`` can be specified.

        :type gql_query: :class:`.query_pb2.GqlQuery`
        :param gql_query: (Optional) The GQL query to run. At most one of
                          ``query`` and ``gql_query`` can be specified.

        :rtype: :class:`.datastore_pb2.RunQueryResponse`
        :returns: The returned protobuf response object.
        """
        request_pb = _datastore_pb2.RunQueryRequest(
            project_id=project,
            partition_id=partition_id,
            read_options=read_options,
            query=query,
            gql_query=gql_query,
        )
        return _rpc(self.client._http, project, 'runQuery',
                    self.client._base_url,
                    request_pb, _datastore_pb2.RunQueryResponse)

    def begin_transaction(self, project):
        """Perform a ``beginTransaction`` request.

        :type project: str
        :param project: The project to connect to. This is
                        usually your project name in the cloud console.

        :rtype: :class:`.datastore_pb2.BeginTransactionResponse`
        :returns: The returned protobuf response object.
        """
        request_pb = _datastore_pb2.BeginTransactionRequest()
        return _rpc(self.client._http, project, 'beginTransaction',
                    self.client._base_url,
                    request_pb, _datastore_pb2.BeginTransactionResponse)

    def commit(self, project, mode, mutations, transaction=None):
        """Perform a ``commit`` request.

        :type project: str
        :param project: The project to connect to. This is
                        usually your project name in the cloud console.

        :type mode: :class:`.gapic.datastore.v1.enums.CommitRequest.Mode`
        :param mode: The type of commit to perform. Expected to be one of
                     ``TRANSACTIONAL`` or ``NON_TRANSACTIONAL``.

        :type mutations: list
        :param mutations: List of :class:`.datastore_pb2.Mutation`, the
                          mutations to perform.

        :type transaction: bytes
        :param transaction: (Optional) The transaction ID returned from
                            :meth:`begin_transaction`.  Non-transactional
                            commits must pass :data:`None`.

        :rtype: :class:`.datastore_pb2.CommitResponse`
        :returns: The returned protobuf response object.
        """
        request_pb = _datastore_pb2.CommitRequest(
            project_id=project,
            mode=mode,
            transaction=transaction,
            mutations=mutations,
        )
        return _rpc(self.client._http, project, 'commit',
                    self.client._base_url,
                    request_pb, _datastore_pb2.CommitResponse)

    def rollback(self, project, transaction_id):
        """Perform a ``rollback`` request.

        :type project: str
        :param project: The project to connect to. This is
                        usually your project name in the cloud console.

        :type transaction_id: bytes
        :param transaction_id: The transaction ID to rollback.

        :rtype: :class:`.datastore_pb2.RollbackResponse`
        :returns: The returned protobuf response object.
        """
        request_pb = _datastore_pb2.RollbackRequest(
            project_id=project,
            transaction=transaction_id,
        )
        # Response is empty (i.e. no fields) but we return it anyway.
        return _rpc(self.client._http, project, 'rollback',
                    self.client._base_url,
                    request_pb, _datastore_pb2.RollbackResponse)

    def allocate_ids(self, project, key_pbs):
        """Perform an ``allocateIds`` request.

        :type project: str
        :param project: The project to connect to. This is
                        usually your project name in the cloud console.

        :type key_pbs: list of :class:`.entity_pb2.Key`
        :param key_pbs: The keys for which the backend should allocate IDs.

        :rtype: :class:`.datastore_pb2.AllocateIdsResponse`
        :returns: The returned protobuf response object.
        """
        request_pb = _datastore_pb2.AllocateIdsRequest(keys=key_pbs)
        return _rpc(self.client._http, project, 'allocateIds',
                    self.client._base_url,
                    request_pb, _datastore_pb2.AllocateIdsResponse)


def _set_read_options(request, eventual, transaction_id):
    """Validate rules for read options, and assign to the request.

    Helper method for ``lookup()`` and ``run_query``.

    :raises: :class:`ValueError` if ``eventual`` is ``True`` and the
             ``transaction_id`` is not ``None``.
    """
    if eventual and (transaction_id is not None):
        raise ValueError('eventual must be False when in a transaction')

    opts = request.read_options
    if eventual:
        opts.read_consistency = _datastore_pb2.ReadOptions.EVENTUAL
    elif transaction_id:
        opts.transaction = transaction_id
