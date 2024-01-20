=====================
Programming Interface
=====================

| **Base URL**
|   Development server: http://localhost:8000/
|   Hosted on Render: https://oc-lettings-f53h.onrender.com/

Endpoints:

==============================  ================================
             URL                          Description
==============================  ================================
``/``                           Home
``/lettings/``                  Lettings list
``/lettings/<letting_id>/``     Letting detail
``/profiles/``                  Profiles list
``/profiles/<user_username>/``  Profile detail
``/admin/``                     Django admin site
``/sentry-debug/``              Test Sentry by raising 500 error
==============================  ================================
