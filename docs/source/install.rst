.. _install:

==================
Installation guide
==================

1. Get the project
------------------

Clone repository with Git:

.. code-block:: console

    $ git clone https://github.com/johntsinger/da-python-p13.git

or

Download the repository:

    * On the `project page <https://github.com/johntsinger/da-python-p13>`_
    * Click on green Code button
    * Click on download ZIP
    * Extract the file.

And go to the project folder:

.. code-block:: console

    $ cd /path/to/da-python-p13

2. Install Python
-----------------

**Requires python 3.6 or higher**

If you don't have Python 3, please visit : https://www.python.org/downloads/ to download it !

.. _virtual_env:

3. Virtual Environment
----------------------

Create a virtual environment in the project root:

.. code-block:: console

    $ python -m venv env

Activate a virtual environment :

* windows:

  .. code-block:: console

      $ env/Scripts/activate

* linux/mac:

  .. code-block:: console

      $ source env/bin/activate

4. Install dependencies
-----------------------

.. code-block:: console

    $ pip install -r requirements.txt
