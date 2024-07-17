from os import getenv
import logging
import traceback

from fastapi import Body, FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader

from simian.entrypoint import entry_point

# Hello world example of deployment of a Simian Web App using fastapi
# In Simian Portal configure back-end type `python_fastapi`.

# SIMIAN_APP_NAMESPACE contains the implicit namespace where gui_init() and gui_event() are defined
# In this case "helloworld.py" next to this file. 
# If helloworld.py is in a subfolder "demo" set SIMIAN_APP_NAMESPACE to "demo.helloworld"
SIMIAN_APP_NAMESPACE = "helloworld"

# Basic API Key based authentication to prevent anonymous access.
# API Key to be configured in Simian Portal and on Backend Server (where the Python code is deployed)
# SIMIAN Portal: configure API Key header name and value in Simian Portal under cURL options:
# Add CURLOPT_HTTPHEADER of type array and add name:value. E.g. x-key:abcdefg
API_KEY_HEADER_NAME = "x-key"
# Backend Server: Configure API Key environment variable. On many  platforms this can be done as "secret".
API_KEY_ENV_VAR_NAME = "X_KEY"

# Basic security by requiring an api-key to be set in header of request
header_scheme = APIKeyHeader(name=API_KEY_HEADER_NAME)
def api_key_auth(api_key: str = Depends(header_scheme)):
    if not api_key == getenv(API_KEY_ENV_VAR_NAME):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )

app = FastAPI()

# The app is served on the root ("/") of the server
@app.post('/', response_class=JSONResponse, dependencies=[Depends(api_key_auth)])
def route_app_requests(request_data: list = Body()) -> dict:
    """Route requests to the simain app code and return the response."""
    # Set the namespace that contains the GUI definition.
    request_data[1].update({"namespace": SIMIAN_APP_NAMESPACE})

    try:
        # Route the post to the entrypoint method.
        payload_out = entry_point(
            request_data[0],
            request_data[1],
            request_data[2],
        )

        # Defer loading the utils until the entry_point has checked that the
        # framework can be used.
#        from simian.gui import utils

        # Return the payload_out as a json string.
#        response = {"returnValue": utils.payloadToString(payload_out)}
        response = {"returnValue": payload_out}

    except Exception as exc:
        logging.error('Error caught by entrypoint wrapper: %r', exc)
        response = {
            "error": {
                "message": str(exc),
                "stacktrace": traceback.format_tb(exc.__traceback__)  # Optional
            }
        }

    return response
