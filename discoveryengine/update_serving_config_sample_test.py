# Copyright 2024 Google LLC
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
#

import os

from discoveryengine import update_serving_config_sample

project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
location = "global"
engine_id = "tuning-sample-app"


def test_update_serving_config():
    serving_config = update_serving_config_sample.update_serving_config_sample(
        project_id, location, engine_id
    )
    assert serving_config
    assert serving_config.custom_fine_tuning_spec.enable_search_adaptor
