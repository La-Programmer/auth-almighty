from typing import Any, Optional
from httpx import Response
from pydantic import BaseModel, ValidationError


class ResponseHelper:
    @staticmethod
    def process_incoming_network_response(
        response: Response, response_class: Optional[BaseModel] = None
    ) -> dict[str, Any] | Any:
        try:
            json_data = response.json()
        except ValueError:
            raise RuntimeError("Response was not valid JSON.")

        if response_class:
            try:
                model_instance = response_class(**json_data)
                return model_instance.model_dump(exclude_none=True)
            except ValidationError as ve:
                # Log or handle validation errors
                raise RuntimeError(f"Validation failed: {ve}")
        else:
            # Return raw if no class provided
            return json_data
