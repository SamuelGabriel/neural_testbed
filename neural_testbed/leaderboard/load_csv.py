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

"""Load a problem_id from sweep with CSV logging."""

from neural_testbed import base as testbed_base
from neural_testbed import logging
from neural_testbed.leaderboard import load


def problem_from_id(problem_id: str,
                    results_dir: str = '/tmp/neural_testbed',
                    overwrite: bool = False) -> testbed_base.TestbedProblem:
  """Factory method to load problem from problem_id and wrap it with a csv logger."""
  problem = load.problem_from_id(problem_id)
  return logging.wrap_problem_csv(problem, problem_id, results_dir, overwrite)
