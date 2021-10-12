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
"""Code for generating a full set of results using multiprocessing."""

from concurrent import futures
import multiprocessing
from typing import Callable, Optional, Sequence

import termcolor
import tqdm

ProblemId = str


def map_mpi(
    run_fn: Callable[[ProblemId], ProblemId],
    problem_ids: Sequence[ProblemId],
    num_processes: Optional[int] = None,
):
  """Maps `run_fn` over `problem_ids`, using `num_processes` in parallel."""

  num_processes = num_processes or multiprocessing.cpu_count()
  num_experiments = len(problem_ids)

  message = """
    Experiment info
    ---------------
    Num experiments: {num_experiments}
    Num worker processes: {num_processes}
    """.format(
        num_processes=num_processes, num_experiments=num_experiments)
  termcolor.cprint(message, color='blue', attrs=['bold'])

  # Create a pool of processes, dispatch the experiments to them, show progress.
  pool = futures.ProcessPoolExecutor(num_processes)
  progress_bar = tqdm.tqdm(total=num_experiments)

  for problem_id in pool.map(run_fn, problem_ids):
    description = '[Last finished: {}]'.format(problem_id)
    progress_bar.set_description(termcolor.colored(description, color='green'))
    progress_bar.update()
