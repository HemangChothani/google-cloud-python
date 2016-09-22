# Copyright 2016 Google Inc. All rights reserved.
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

import os
import sys

from setuptools import setup
from setuptools import find_packages


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(PROJECT_ROOT, 'README.rst')) as file_obj:
    README = file_obj.read()


REQUIREMENTS = [
    'httplib2 >= 0.9.1',
    'googleapis-common-protos',
    'oauth2client >= 2.0.1',
    'protobuf >= 3.0.0',
    'six',
]

GRPC_PACKAGES = [
    'grpcio >= 1.0.0',
    'google-gax >= 0.14.1, < 0.15dev',
    'gapic-google-pubsub-v1 >= 0.9.0, < 0.10dev',
    'grpc-google-pubsub-v1 >= 0.9.0, < 0.10dev',
    'gapic-google-logging-v2 >= 0.9.0, < 0.10dev',
    'grpc-google-logging-v2 >= 0.9.0, < 0.10dev',
]

RTD_ENV_VAR = 'READTHEDOCS'
if RTD_ENV_VAR not in os.environ:
    REQUIREMENTS.extend(GRPC_PACKAGES)

setup(
    name='google-cloud',
    version='0.19.0',
    description='API Client library for Google Cloud',
    author='Google Cloud Platform',
    author_email='jjg+google-cloud-python@google.com',
    long_description=README,
    scripts=[],
    url='https://github.com/GoogleCloudPlatform/google-cloud-python',
    namespace_packages=[
        'google',
        'google.cloud',
    ],
    packages=find_packages(),
    license='Apache 2.0',
    platforms='Posix; MacOS X; Windows',
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
    ]
)
