# Deploy your Simian Web App

After developing and testing your Simian Web App locally, the next step is deployment to the web. This involves two components:
1. Simian Portal configured to host your App
2. A(ny) backend where your Simian Web App Python code is running as a web service

For evaluation purposes a shared Simian Portal is available. [Render](https://render.com) allows for free deployment of Python code as a web service - directly from GitHub.

## Simian Portal
1. Complete registration at [Simian Demo Portal](https://demo02.simiansuite.com/).
2. From your Render deployment, per steps below, take note of the `subdomain` of your backend deployment on `.onrender.com`
3. Take note of the API Key (if configured in [main.py](main.py)).
5. Configure your app with Renderer as backend [here](https://demo02.simiansuite.com/configure_my_app/) by setting the onrender.com subdomain, and optionally the API Key.
6. Start your Simian Web App via the [Simian Portal](https://demo02.simiansuite.com/) (you can bookmark the app link for direct access).

Note: Simian Portal is intended to share apps with others and features app access management. On the evaluation Simian Portal access to your app is restricted to yourself.

## Render FastAPI web service as Simian Web App backend
Render provides a free option to deploy Python code as a FastAPI web service. This is ideal for testing the deployment of your Simian Web App.

This repo contains all that is needed to deploy a working Simian Web App.

# Deploy to FastAPI web service on Render

Use this repo as a Simian Web App template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) web service on Render.

- Render build information is provided in `render.yaml`.
- Python package installation instructions are provided through `requirements.txt`.
- FastAPI routing,  API key configuration and Simian Web app module configuration is done in `main.py`.
- A simple Simian Web App example is provided in `helloworld.py`

Note: If you fork this repository, you should modify the github project url in this `readme.md` to point to your organization and your repository.

## Manual Steps
See https://render.com/docs/deploy-fastapi or follow the steps below:

1. You may use this repository directly or [create your own repository from this template](https://github.com/Rolf-MP/simian-render/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

Or simply click:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=(https://github.com/Rolf-MP/simian-render/))

## Thanks
Forked from [Render Examples - FastAPI](https://github.com/render-examples/fastapi) who thanks [Harish](https://harishgarg.com) for the [inspiration to create a FastAPI quickstart for Render](https://twitter.com/harishkgarg/status/1435084018677010434) and for some sample code!
