# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import google.cloud.datastore
import pytest

from google.cloud.ndb import key as key_module
import tests.unit.utils


def test___all__():
    tests.unit.utils.verify___all__(key_module)


class TestKey:
    @staticmethod
    def test_constructor():
        key = key_module.Key("Kind", project="foo")
        ds_key = key._key
        assert isinstance(ds_key, google.cloud.datastore.Key)
        assert ds_key._flat_path == ("Kind",)
        assert ds_key._namespace is None
        assert ds_key._project == "foo"
        assert ds_key._path == [{"kind": "Kind"}]
