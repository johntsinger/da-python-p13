.. _deploy:

======
Deploy
======

This app use Render as host, Sentry to track error, GitHub for the versioning,
GitHub Actions for the CI, and DockerHub to save the image.

**REQUIREMENTS:**

- GitHub account
- Sentry account
- DockerHub account
- Render account

A CI/CD pipeline is set to run 3 jobs:

- **build and test** - to lint the code, run test and check coverage (must be over 80%)
- **docker** - to buid the Docker image and push it to DockerHub
- **deploy** - to deploy the Docker container on Render

The pipeline run every job when pushed onto the master branch,
or only the Build-and-test job when pushed onto another branch.

If one job fails, the others are skiped.


Set GitHub enviroment variables
-------------------------------

If you don't have a GitHub account yet, create one.

#. On your respository go to settings

#. Select Secrets and variables and click on Actions

#. Click on New repository secrets

#. Enter secret name

#. Enter the secret

#. Repeat 3. 4. and 5. for all secrets to be set

Secrets to be set:

========================  =============================
Name                      Secret                       
========================  =============================
``DOCKERHUB_USERNAME``    ``<your_dockerhub_username>``
``DOCKERHUB_TOKEN``       ``<your_dockerhub_token>``
``MY_RENDER_API_KEY``     ``<your_render_api_key>``
``MY_RENDER_SERVICE_ID``  ``<your_render_service_id>``
========================  =============================

See below to know how to get it.


Get the DockerHub access token
------------------------------

If you don't have a DockerHub account yet, create one.

On your DockerHub account:

#. Click your profile

#. Then on My Account

#. Select Security

#. And create a new token by clicking New Access Token

#. Add the token to your GitHub secrets with name ``DOCKERHUB_TOKEN``

.. warning::

    The DockerHub Access Token can be view only one time at the creation !
    If you loose it you need to generate a new one.


Configure Sentry
----------------

If you don't have a Sentry account yet, create one.

On your dashboard

#. Select Projects

#. Click on Create project

#. Configure the project

#. Get the DSN


Configure Render
----------------

If you don't have a Render account yet, create one.

On your render dashbord:

#. Click on New + and select Web Service

#. Select option Build and deploy from a Git repository

#. Connect yout GitHub account

#. Configure your service by setting:

    * Name: Choose a name
    * Region: Choose your region
    * Runtime: set Docker
    * Set environment variables:

        * ``DJANGO_SECRET_KEY``: ``<your_django_secret_key>`` 

          .. warning::

             | Django can **NOT** start without a secret key.
             | If the secret key is missing it will raise
             | ``ImproperlyConfigured: The SECRET_KEY setting must not be empty.``

        * ``SENTRY_DSN``: ``<your_sentry_dsn>``

          .. note::

             To get your Sentry DSN see `Where to Find Your DSN <https://docs.sentry.io/product/sentry-basics/concepts/dsn-explainer/#where-to-find-your-dsn>`_

    * Click on Advanced:

        * Set Dockerfile Path to: ``Dockerfile``
        * Set Auto-Deploy to: ``No``

    * Click Create Web Service

#. Get the api key:

    * On your profile select Account Settings

    * Under API Keys select Create API key

    * Add the API key to your GitHub secrets with the name ``MY_RENDER_API_KEY``

    .. warning::

        The Render API key can be view only one time at the creation !
        If you loose it you need to generate a new one.

#. Get the service id:

    * On your dashboard select your service

    * When viewing a service in the Render dashboard grab this value from the URL - it will start with ``srv-``

    * Add the service id to your GitHub secrets with the name ``MY_RENDER_SERVICE_ID``
