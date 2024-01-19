===========
Quick Start
===========

**REQUIREMENTS:**

*The following are not required for development, but since a CI/CD pipeline is set,
it's highly recommended to have it otherwise the pipeline will fail when you push your code to your GitHub repository.*

* GitHub account
* Sentry account
* DockerHub account
* Render account


After following the installation instructions (see :ref:`install`) you can run the django server locally.

#. Activate virtual environment if not already activated (see :ref:`virtual_env`).

#. Create a file named ``.env`` at the root folder to store environment varibales.

#. Add environment variables into the ``.env`` file::

    DJANGO_SECRET_KEY=<your_secret_key> (required)
    SENTRY_DSN=<your_sentry_dsn> (optional)
    RENDER='' (optional use it to set DEBUG to False)

#. Run the local server:

   .. code-block:: console

       $ python manage.py runserver

#. Go to http://127.0.0.1:8000/

.. note::
    When running local server, ``DEBUG`` is set to ``True`` by default.
    If you want to set it to False you can:

        - add ``RENDER=''`` in ``.env`` file.
          (since the site uses Render for deployment)

    Then run ``$ python manage.py runserver --insecure``
    to load static files locally.

Testing
-------

To run tests:

.. code-block:: console

    $ pytest

To update coverage:

.. code-block:: console

    $ coverage run -m pytest

To get coverage html:

.. code-block:: console

    $ coverage html

Linting
-------

To run linting:

.. code-block:: console

    $ flake8

Docker
------

There are two ways to run a Docker container locally.

**Manually:**

#. Build the image with the Dockerfile locally (optional):

   .. code-block:: console

       $ docker build -t <image_name> .

#. Run it:

   * Set environment variable at run time:

     With ``DEBUG`` set to ``True``:

     .. code-block:: console

         $ docker run -e DJANGO_SECRET_KEY=<your_secret_key> -e SENTRY_DSN=<your_sentry_dsn> -d -p 8000:8000 <image_name>

     To set ``DEBUG`` to ``False`` add ``RENDER`` environment variable like this:

     .. code-block:: console

         $ docker run -e DJANGO_SECRET_KEY=<your_secret_key> -e SENTRY_DSN=<your_sentry_dsn> -e RENDER='' -d -p 8000:8000 <image_name>

   * Or using ``.env`` file:

     Create a ``.env`` file at the root folder with::

       DJANGO_SECRET_KEY=<your_secret_key> (required)
       SENTRY_DSN=<your_sentry_dsn> (optional)
       RENDER='' (optional use it to set DEBUG to False)

     Then run:

     .. code-block:: console

         $ docker run --env-file .env -d -p 8000:8000 <image_name>

Got to http://127.0.0.1:8000/

**By getting the existing image from the DockerHub:**

    Execute command from step 2. (Run it) using ``johnsinger/oc_lettings`` as ``<image_name>``

    This download the latest image of the application deployed on the host (Render see :ref:`deploy`).