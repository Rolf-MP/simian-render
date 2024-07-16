from typing import Optional
# Use back-end type `python_fastapi` in the portal configuration.
from fastapi import Body, FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader
import logging
import traceback

from simian.entrypoint import entry_point

api_keys = [
    "akljnv13bvi2vfo0b0bw"
]  # This is encrypted in the database

app = FastAPI()

header_scheme = APIKeyHeader(name="x-key")

def api_key_auth(api_key: str = Depends(header_scheme)):
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )


@app.get('/health', response_class=JSONResponse)
async def status():
    return dict(status="OK")

@app.post('/', response_class=JSONResponse, dependencies=[Depends(api_key_auth)])
def route_app_requests(request_data: list = Body()) -> dict:
    """Route requests to ballthrower GUI and return the response."""
    # Set the namespace that contains the GUI definition.
    request_data[1].update({"namespace": "helloworld"})

    try:
        # Route the post to the entrypoint method.
        payload_out = entry_point(
            request_data[0],
            request_data[1],
            request_data[2],
        )

        # Defer loading the utils until the entry_point has checked that the
        # framework can be used.
        from simian.gui import utils

        # Return the payload_out as a json string.
        response = {"returnValue": utils.payloadToString(payload_out)}

    except Exception as exc:
        logging.error('Error caught by entrypoint wrapper: %r', exc)
        response = {
            "error": {
                "message": str(exc),
                "stacktrace": traceback.format_tb(exc.__traceback__)  # Optional
            }
        }

    return response
