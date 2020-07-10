#  Copyright 2020 Varun Kruthiventi
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import Any

from fastapi import APIRouter

from krypton.backend.models.schema.health_check import HealthCheckResponse
from krypton.core.constants import KRYPTON_VERSION

router = APIRouter()


@router.get("/health", response_model=HealthCheckResponse)
def health() -> Any:
    """Simple Health Check Endpoint."""
    return {"status": "Healthy", "version": KRYPTON_VERSION}
