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

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from krypton.backend.models.schema.health_check import HealthCheckResponse
from krypton.backend.models.store.repository import model_repository

router = APIRouter()


@router.get("/models")
def list_models() -> Any:
    try:
        models = model_repository.get_models()
        return JSONResponse(status_code=status.HTTP_200_OK, content={
            'success': True,
            'data': models
        })
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={
            'success': False,
            'message': f"Unable to handle the request. Please try again.",
            'details': str(e)
        })


@router.post("/models/{model_name}/predict")
async def serve_model(model_name: str, request: Request) -> Any:
    """Simple Health Check Endpoint."""
    try:
        model = model_repository.get_model(model_name)
        if not model:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={
                'success': False,
                'message': f"Model with name: {model_name} not found in the Krypton Model Repository."
            })
        # Pass FastAPI Request object to
        response = await model.predict(request)
        # Krypton expects the response to be a valid response object that can be handled by FastAPI
        return response

    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={
            'success': False,
            'message': f"Unable to handle the request. Please try again.",
            'details': str(e)
        })
