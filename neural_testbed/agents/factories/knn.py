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
"""Factory methods for K-nearest neighbors baseline agent."""

import dataclasses
from typing import Sequence

from enn import base as enn_base
from neural_testbed import base as testbed_base
from neural_testbed.agents.factories import base as factories_base
import numpy as np
from sklearn import neighbors


@dataclasses.dataclass
class KnnConfig:
  num_neighbors: int = 3  # Number of nearest-neighbors
  weighting: str = 'uniform'  # Weighting type to use ('distance', 'uniform')


def make_agent(config: KnnConfig) -> testbed_base.TestbedAgent:
  """Factory method to create a K-nearst neighbors agent."""

  def knn_agent(
      data: testbed_base.Data,
      prior: testbed_base.PriorKnowledge,
  ) -> testbed_base.EpistemicSampler:
    # sklearn cannot handle instances with no samples of that class
    # so we add a fake sample for every class here as a hack
    new_x = np.zeros((prior.num_classes, data.x.shape[1]))
    new_y = np.expand_dims(np.arange(prior.num_classes), axis=1)
    data = testbed_base.Data(
        np.concatenate((data.x, new_x), axis=0),
        np.concatenate((data.y, new_y), axis=0))
    knn = neighbors.KNeighborsClassifier(
        n_neighbors=min(data.x.shape[0], config.num_neighbors),
        weights=config.weighting)
    knn.fit(data.x, np.ravel(data.y))

    # Ensure that the number of classes is correct
    # (this will fail if the fake data isn't added above)
    assert len(knn.classes_) == prior.num_classes

    def enn_sampler(x: enn_base.Array, seed: int = 0) -> enn_base.Array:
      del seed  # seed does not affect the knn agent.
      probs = knn.predict_proba(x)
      # threshold the probabilities, otherwise get nans in the KL calculation
      probs = np.minimum(np.maximum(probs, 0.01), 0.99)
      return np.log(probs)  # return logits

    return enn_sampler

  return knn_agent


def knn_sweep() -> Sequence[KnnConfig]:
  sweep = []
  for num_neighbors in [1, 5, 10, 30, 50, 100]:
    for weighting in ['uniform', 'distance']:
      sweep.append(KnnConfig(num_neighbors, weighting))
  return tuple(sweep)


def paper_agent() -> factories_base.PaperAgent:
  return factories_base.PaperAgent(
      default=KnnConfig(),
      ctor=make_agent,
      sweep=knn_sweep,
  )
