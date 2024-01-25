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

#. Add environment variables into the ``.env`` file:

    .. parsed-literal::

        DJANGO_SECRET_KEY=<your_secret_key> (**Required**)
        SENTRY_DSN=<your_sentry_dsn> (Optional see :ref:`sentry`)
        DEBUG=False (Optional use it to set DEBUG to False)

    .. note::
        When running local server, ``DEBUG`` is set to ``True`` by default.
        If you want to set it to ``False`` you can add ``DEBUG=False`` in ``.env`` file.

        Value allowed are ``False``, ``false``, ``FALSE`` or ``0``, each other value or not adding ``DEBUG`` in the ``.env`` file
        is equivalent to ``DEBUG=True``.

        Then run ``$ python manage.py runserver --insecure``
        to load static files locally.

#. Run the local server:

   .. code-block:: console

       $ python manage.py runserver

#. Go to http://localhost:8000/


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

.. _sentry:

Sentry
------

You can enable Sentry to track errors. To do that you need to have a Sentry account and a project configured.

.. note::

    Sentry is NOT activated when ``DEBUG`` is set to ``True`` (during development).

To activate it during development, do the following :

#. Get your Sentry DSN (see `Where to Find Your DSN <https://docs.sentry.io/product/sentry-basics/concepts/dsn-explainer/#where-to-find-your-dsn>`_).

#. Add ``SENTRY_DSN=<your_sentry_dsn>`` to the ``.env`` file.

#. Add ``DEBUG=False`` in the ``.env`` file to set ``DEBUG`` to ``False``.

#. Run Django local server with ``python manage.py runserver --insecure``

#. Test sending an error by going to http://localhost:8000/sentry-debug/

#. You can find the report on your Sentry Issues.

Docker
------

There are two ways to run a Docker container locally.

**Manually:**

#. Build the image with the Dockerfile locally (optional):

   .. code-block:: console

       $ docker build -t <image_name> .

#. Run it:

   * Set environment variables:

     With ``DEBUG`` set to ``True`` and **NOT** using Sentry:

     .. code-block:: console

         $ docker run -e DJANGO_SECRET_KEY=<your_secret_key> -d -p 8000:8000 <image_name>

     To set ``DEBUG`` to ``False`` and **ACTIVATE** Sentry, add ``SENTRY_DSN`` and ``DEBUG`` environment variables as follows:

     .. code-block:: console

         $ docker run -e DJANGO_SECRET_KEY=<your_secret_key> -e SENTRY_DSN=<your_sentry_dsn> -e DEBUG=False -d -p 8000:8000 <image_name>

   * Or read environment variables from a file:

     Create a ``.env`` file at the root folder with:

     .. parsed-literal::

           DJANGO_SECRET_KEY=<your_secret_key> (**Required**)
           SENTRY_DSN=<your_sentry_dsn> (Optional see :ref:`sentry`)
           DEBUG=False (Optional use it to set DEBUG to False)

     Then run:

     .. code-block:: console

         $ docker run --env-file .env -d -p 8000:8000 <image_name>

Got to http://localhost:8000/

**By getting the existing image from the DockerHub:**

    Execute command from step 2. (Run it) using ``johnsinger/oc_lettings`` as ``<image_name>``

    This download the latest image of the application deployed on the host (Render see :ref:`deploy`).