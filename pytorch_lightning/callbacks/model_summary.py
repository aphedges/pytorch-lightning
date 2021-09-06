# Copyright The PyTorch Lightning team.
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
"""
Model Summary
=============

Generates a summary of all layers in a :class:`~pytorch_lightning.core.lightning.LightningModule`.

The string representation of this summary prints a table with columns containing
the name, type and number of parameters for each layer.

"""
from typing import Optional

from pytorch_lightning.callbacks.base import Callback


class ModelSummary(Callback):
    def __init__(self, mode: Optional[str] = None, max_depth: Optional[int] = 1):
        self._mode = mode
        self._max_depth = max_depth
