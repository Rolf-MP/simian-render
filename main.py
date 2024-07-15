from typing import Optional
# Use back-end type `python_fastapi` in the portal configuration.
from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
import logging
import traceback

from simian.entrypoint import entry_point

app = FastAPI()
@app.get('/health', response_class=JSONResponse)
async def status():
    return dict(status="OK")

@app.post('/', response_class=JSONResponse)
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
