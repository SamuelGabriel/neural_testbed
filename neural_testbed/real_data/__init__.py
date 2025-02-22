# python3
# pylint: disable=g-bad-file-header
# Copyright 2021 DeepMind Technologies Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or  implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

"""Exposing the public methods of real data."""
from neural_testbed.real_data.data_sampler import RealDataSampler
from neural_testbed.real_data.datasets import CLASSIFICATION_DATASETS
from neural_testbed.real_data.datasets import DatasetInfo
from neural_testbed.real_data.datasets import DATASETS
from neural_testbed.real_data.datasets import DATASETS_SETTINGS
from neural_testbed.real_data.datasets import IMAGE_DATASETS
from neural_testbed.real_data.datasets import ORIGINAL_CLASSIFICATION_DATASETS
from neural_testbed.real_data.datasets import ORIGINAL_IMAGE_DATASETS
from neural_testbed.real_data.datasets import ORIGINAL_STRUCTURED_DATASETS
from neural_testbed.real_data.datasets import REGRESSION_DATASETS
from neural_testbed.real_data.datasets import STRUCTURED_DATASETS
from neural_testbed.real_data.load import problem_from_id
from neural_testbed.real_data.load_classification import load as load_classification
from neural_testbed.real_data.load_regression import load as load_regression
