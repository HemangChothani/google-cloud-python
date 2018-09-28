# Copyright 2018 Google LLC
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

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
import synthtool.gcp as gcp
import logging

logging.basicConfig(level=logging.DEBUG)

gapic = gcp.GAPICGenerator()
common = gcp.CommonTemplates()

library = gapic.py_library(
    "dlp", "v2", config_path="/google/privacy/dlp/artman_dlp_v2.yaml"
)

excludes = [
    "README.rst",
    "nox.py",
    "setup.py",
    "docs/index.rst",
]
s.copy(library, excludes=excludes)

# Fix namespace
s.replace(
    "google/**/*.py",
    "google\.cloud\.privacy\.dlp_v2",
    "google.cloud.dlp_v2"
)
s.replace(
    "tests/**/*.py",
    "google\.cloud\.privacy\.dlp_v2",
    "google.cloud.dlp_v2"
)

# Add missing utf-8 marker
s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "# Generated by the protocol buffer compiler.  DO NOT EDIT!",
    "# -*- coding: utf-8 -*-\n\g<0>"
)

# Fix unindentation of bullet list second line
s.replace(
    "google/cloud/dlp_v2/gapic/dlp_service_client.py",
    "(                \* .*\n                )([^\s*])",
    "\g<1>  \g<2>"
)

s.replace(
    "google/cloud/dlp_v2/gapic/dlp_service_client.py",
    "(\s+)\*.*\n\s+::\n\n",
    "\g<1>  ::\n"
)

# Fix raw-latex bits in storage_pb2.py
s.replace(
    "google/cloud/dlp_v2/proto/storage_pb2.py",
    "number regex.*\n(\s+)latex:.*\n",
    "number regex \"(\\d{3}) \\d{3}-\\d{4} \"\\\n"
    "\g<1>could be adjusted upwards if the area code is \\\n"
)

# Fix Docstrings in google/cloud/dlp_v2/proto/storage_pb2.py
s.replace(
    "google/cloud/dlp_v2/proto/storage_pb2.py",
    "(hotword_regex:)\n(\s+Regular expression.*)\n",
    "\g<1> \\\n\g<2> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/storage_pb2.py",
    "(proximity:)\n(\s+Proximity.*)\n(\s+reside..*)\n(\s+characters..*)\n"
    "(\s+the window.*)\n(\s+of the finding.*)\n(\s+number regex.*)\n"
    "(\s+latex:.*)\n(\s+known to be the local.*)\n(\s+hotword regex.*)\n",
    "\g<1> \\\n\g<2> \\\n\g<3> \\\n\g<4> \\\n\g<5> \\\n\g<6> \\\n\g<7> "
    "\\\n\g<8> \\\n\g<9> \\\n\g<10> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/storage_pb2.py",
    "(likelihood_adjustment:)\n",
    "\g<1> \\\n"
)

# Fix Docstrings in google/cloud/dlp_v2/proto/dlp_pb2.py
s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(max_findings_per_item:)\n(\s+Max number.*)\n(\s+scanned. When.*)\n"
    "(\s+maximum returned is 1000.*)\n(\s+When set within.*)\n",
    "\g<1> \\\n\g<2> \\\n\g<3> \\\n\g<4> \\\n\g<5> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(max_findings_per_request:)\n(\s+Max number of.*)\n(\s+When set .*)\n",
    "\g<1> \\\n\g<2> \\\n\g<3> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(max_findings_per_info_type:)\n",
    "\g<1> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(snapshot_inspect_template:)\n(\s+If run with an .*)\n",
    "\g<1> \\\n\g<2> \\\n"
)

to_replace = [
    "processed_bytes:", "total_estimated_bytes:", "info_type_stats:",
    "Statistics of how many instances of each info type were found",
    "requested_options:",
]

for replace in to_replace:
    s.replace(
        "google/cloud/dlp_v2/proto/dlp_pb2.py",
        f"({replace})\n",
        "\g<1> \\\n"
    )

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(sensitive_value_frequency_lower_bound:)\n(\s+Lower bound.*)\n",
    "\g<1> \\\n\g<2> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(sensitive_value_frequency_upper_bound:)\n(\s+Upper bound.*)\n",
    "\g<1> \\\n\g<2> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(bucket_size:)\n(\s+Total number of equivalence.*)\n",
    "\g<1> \\\n\g<2>\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(bucket_values:)\n(\s+Sample of equivalence.*)\n",
    "\g<1> \\\n\g<2> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(offset_minutes:)\n(\s+Set only.*)\n",
    "\g<1> \\\n\g<2> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(result:)\n(\s+A summary of the outcome of this inspect job.)",
    "\g<1> \\\n\g<2>"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(storage_config:)\n(\s+The data to scan.\n)",
    "\g<1> \\\n\g<2>"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(inspect_config:)\n(\s+How and what to scan for.\n)",
    "\g<1> \\\n\g<2>"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(inspect_template_name:)\n(\s+If provided, will be.*)\n"
    "(\s+InspectConfig.*)\n(\s+values persisted.*)\n(\s+actions:)\n"
    "(\s+Actions to.*)\n",
    "\g<1> \\\n\g<2> \\\n\g<3> \\\n\g<4> \\\n\g<5> \\\n\g<6> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "    (\s+Set of values defining the equivalence class.*)\n"
    "    (\s+quasi-identifier.*)\n"
    "    (\s+message. The order.*)\n",
    "\g<1> \\\n\g<2> \\\n\g<3>\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "    (\s+Size of the equivalence class, for example number of rows with)\n"
    "    (\s+the above set of values.)\n",
    "\g<1> \\\n\g<2>\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(equivalence_class_size_lower_bound:)\n(\s+Lower bound.*)\n",
    "\g<1> \\\n\g<2> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(equivalence_class_size_upper_bound:)\n(\s+Upper bound.*)\n",
    "\g<1> \\\n\g<2> \\\n"
)

s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(bucket_value_count:)\n(\s+Total number of distinct equivalence.*)\n",
    "\g<1> \\\n\g<2>\n"
)

# Docstrings from categorical histogram bucket
s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(value_frequency_lower_bound:)\n\s+(Lower bound.*)\n\s+(bucket.\n)"
    "(\s+value_frequency_upper.*)\n\s+(Upper.*)\n\s+(bucket.\n)"
    "(\s+bucket_size:)\n\s+(Total.*\n)"
    "(\s+bucket_values:)\n\s+(Sample of value.*)\n\s+(of values.*\n)"
    "(\s+bucket_value_count:)\n\s+(Total number.*\n)",

    "\g<1> \g<2> \g<3>\g<4> \g<5> \g<6>\g<7> \g<8>"
    "\g<9> \g<10> \g<11>\g<12> \g<13>"
)

# Fix docstrings tagged field indentation issues in dlp_pb2.py
s.replace(
    "google/cloud/dlp_v2/proto/dlp_pb2.py",
    "(DESCRIPTOR .*_TAGGEDFIELD,\n\s+__module__.*\n\s+,\n\s+__doc__.*\n)"
    "(\s+field:)\n(\s+Identifies .*)\n(\s+tag:)\n(\s+Semantic.*)\n"
    "(\s+determine.*)\n(\s+reidentifiability.*)\n(\s+info_type:)\n"
    "(\s+A column.*)\n(\s+public dataset.*)\n(\s+available.*)\n(\s+ages.*)\n"
    "(\s+supported Info.*)\n(\s+supported.*)\n(\s+custom_tag:)\n(\s+A col.*)\n"
    "(\s+user must.*)\n(\s+statist.*)\n(\s+\(below.*)\n(\s+inferred:)\n"
    "(\s+If no semantic.*)\n",
    "\g<1>\g<2> \\\n\g<3>\n\g<4> \\\n\g<5> \\\n\g<6> \\\n"
    "\g<7> \\\n\g<8> \\\n\g<9> \\\n\g<10> \\\n\g<11> \\\n\g<12> \\\n"
    "\g<13> \\\n\g<14>\n\g<15> \\\n\g<16> \\\n\g<17> \\\n\g<18> \\\n"
    "\g<19>\n\g<20> \\\n\g<21> \\\n"
)

s.replace(
        "google/cloud/dlp_v2/proto/dlp_pb2.py",
        "(////////.*)\n\s+(///////////////\n)",
        "\g<1> \g<2>"
)

# Fix Docstrings in google/cloud/dlp_v2/gapic/dlp_service_client.py
s.replace(
    "google/cloud/dlp_v2/gapic/dlp_service_client.py",
    "(- ``CryptoReplaceFfxFpeConfig``\n)(\s+If a dict is provided.*\n)"
    "(\s+message.*\n)",
    "\g<1>   \g<2>   \g<3>"
)

s.replace(
    "google/cloud/dlp_v2/gapic/dlp_service_client.py",
    "  ::\n  (\s+- `state`.*\n)  (\s+- `inspected_storage`.*\n)"
    "  (\s+- `trigger_name`.*\n)",
    "* Supported fields/values for inspect jobs:\n\g<1>\g<2>\g<3>"
)

s.replace(
    "google/cloud/dlp_v2/gapic/dlp_service_client.py",
    "  ::\n  (\s+- `state`.*\n)(\s+\* The operator must be)",
    "* Supported fields for risk analysis jobs:\n\g<1>\g<2>"
)
