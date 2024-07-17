from os import getenv
import logging
import traceback

from fastapi import Body, FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader

from simian.entrypoint import entry_point
from simian.gui import utils

# Hello world example of deployment of a Simian Web App using fastapi, with API Key authentication 
# between Simian Portal and BAckend Server where the Python runs as FastAPI web service.
# In Simian Portal configure back-end type `python_fastapi`.

# SIMIAN_APP_NAMESPACE contains the implicit namespace where gui_init() and gui_event() are defined
# In this case "helloworld.py" next to this file. 
# If helloworld.py is in a subfolder "demo" set SIMIAN_APP_NAMESPACE to "demo.helloworld"
SIMIAN_APP_NAMESPACE = "helloworld"
# The route on which the Simian App is served on backend server.
SIMIAN_APP_ROUTE = "/"

# Enable basic API Key based authentication to prevent anonymous access.
API_KEY_AUTH_ENABLED = True
# When API Key Authentication is enabled, it must be configured in Simian Portal and on the 
# Backend Server (where the Python code is deployed).
# SIMIAN Portal: configure API Key header name and value in Simian Portal under cURL options:
# Add CURLOPT_HTTPHEADER of type array and add name:value. E.g. x-key:abcdefg
API_KEY_HEADER_NAME = "x-key"
# Backend Server: Configure API Key environment variable, on many platforms labeled "secret".
API_KEY_ENV_VAR_NAME = "X_KEY"

app = FastAPI()

# If API Key authentication is enabled add dependency
if API_KEY_AUTH_ENABLED:
    # Basic security by requiring an api-key to be set in header of request
    header_scheme = APIKeyHeader(name=API_KEY_HEADER_NAME)
    def api_key_auth(api_key: str = Depends(header_scheme)):
        if not api_key == getenv(API_KEY_ENV_VAR_NAME):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Forbidden"
            )
    dependencies = [Depends(api_key_auth)]
else:
    dependencies = []

# The app is served on the SIMIAN_APP_SLUG path on backend server
@app.post(SIMIAN_APP_ROUTE, response_class=JSONResponse, dependencies=dependencies)
def route_app_requests(request_data: list = Body()) -> dict:
    """Route requests to the Simian App code and return the response."""
    # Set the Python namespace of the Simian App.
    request_data[1].update({"namespace": SIMIAN_APP_NAMESPACE})

    try:
        # Route the post to the entrypoint method.
        payload_out = entry_point(
            request_data[0],
            request_data[1],
            request_data[2],
        )

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
