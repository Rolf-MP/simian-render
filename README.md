# Deploy your Simian Web App

After developing and testing your Simian Web App locally, deployment to the web. This involves two main steps:
1. Publishing the app to your audience on Simian Portal
2. Deploying your Simian Web App Python code as a web service on a(ny) backend

For evaluation purposes, a shared Simian Portal is readily available.  
For deployment, [Render](https://render.com) offers convenient and free hosting Python code as a web service - directly from GitHub.

## Simian Portal
1. Sign up at [Simian Evaluation Portal](https://evaluate.simiansuite.com/).
2. From your Render deployment (per steps below), take note of:
  - The `subdomain` of your backend deployment on `.onrender.com`
  - The API Key (if configured per instructions in [main.py](main.py)).
5. In Simian Evaluation Portal, configure and publish app [here](https://evaluate.simiansuite.com/configure_my_app/) by setting the onrender.com subdomain, and the (optional) API Key.
6. Start your app via the [Simian Evaluation Portal](https://evaluate.simiansuite.com/) and bookmark the app link for direct access.

Notes:  
- Simian Portal supports app sharing and access management, but app access on the Evaluation Portal is restricted to yourself only and solely serves evaluation purposes.
- Simian Portal works with a range of backend platforms. For evaluation purposes render.com has been chosen because of its convenient deployment path from GitHub, its free offering, and the fact that deployed mode lives under your (versus us) control.

## Render FastAPI web service as Simian Web App backend
Render provides a free option to deploy Python code as a FastAPI web service, making it perfect for testing the deployment of your Simian Web App.

# Deploy to FastAPI web service on Render

Use this repo as a Simian Web App template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) web service on Render.

- Render build information is provided in `render.yaml`.
- Python package installation instructions are provided through `requirements.txt`.
- FastAPI routing,  API key configuration and Simian Web app module configuration is done in `main.py`.
- A simple Simian Web App example is provided in `helloworld.py`

Note:
If you fork this repository, you should modify the github project url in this `readme.md` to point to your organization and your repository.

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
