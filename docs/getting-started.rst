Getting started
===============

Five-minute quickstart
----------------------

1. Get the source and create a Python environment.

   .. code-block:: console

      git clone https://github.com/venkateshhs/eCRF.git
      cd eCRF
      python3 -m venv .venv
      source .venv/bin/activate
      pip install -r requirements.txt

2. Build the Vue frontend.

   .. code-block:: console

      cd eCRF_frontend
      npm ci
      npm run build
      cd ..

3. Start the local launcher.

   .. code-block:: console

      python server.py

4. Visit ``http://127.0.0.1:8000/login`` if the browser does not open
   automatically.

   .. figure:: _static/screenshots/local-login.jpg
      :alt: case-e local login page in a 1280 by 720 browser window
      :width: 100%

      The local case-e sign-in page. Select **Create account** for a new user or
      enter an existing username and password. Branding can vary by deployment.

5. For a new local data folder, sign in as ``admin`` with ``Admin123!``, then
   immediately change that password from **User Management → Change Password**.

6. Open **Study Management → Create Study**, complete the setup wizard, publish
   the study, and use **Add Data** to enter the first subject/visit record.

.. warning::

   Local defaults are for evaluation on one workstation. Do not expose the
   local launcher to a network and do not retain the default administrator
   password.

Run locally from source
-----------------------

Prerequisites
~~~~~~~~~~~~~

* Python 3.11 or a compatible recent Python 3 release
* Node.js and npm for the frontend build
* Git to obtain the source

The local launcher performs the following automatically:

* selects the ``local`` runtime profile;
* binds only to ``127.0.0.1:8000``;
* stores application records in SQLite;
* stores canonical study JSON and uploaded files on the local filesystem;
* disables DataLad and git-annex;
* creates a bootstrap administrator when the database is new; and
* opens the browser unless ``ECRF_OPEN_BROWSER=0`` is set.

On macOS and Windows, the first launch asks for a data folder. If no folder is
chosen, case-e uses ``ecrf_data`` beside the launcher and records the choice in
``ecrf_config.json``.

Local storage layout
~~~~~~~~~~~~~~~~~~~~

===================== =====================================
Item                  Default location
===================== =====================================
SQLite database       ``<data-dir>/ecrf.db``
Study and file root   ``<data-dir>/bids_datasets``
Launcher config       ``<application-dir>/ecrf_config.json``
Runtime profile       ``ECRF_PROFILE=local``
===================== =====================================

Set ``ECRF_DATA_DIR`` to choose the data folder without the selection dialog.
Set ``ECRF_LOCAL_STUDY_ROOT`` when the canonical study folders should live in a
different location from the SQLite database.

Build the desktop application
-----------------------------

The repository includes a PyInstaller specification. Build the frontend first,
install the build dependencies, and then create the application bundle.

.. code-block:: console

   source .venv/bin/activate
   pip install -r requirements-build.txt
   cd eCRF_frontend
   npm ci
   npm run build
   cd ..
   pyinstaller -y ecrf.spec

The result is written beneath ``dist/``. Move the complete generated bundle;
do not extract individual internal files. The packaged application uses the
same local profile, folder selection, SQLite database, and bootstrap behavior
as ``python server.py``.

Move an existing local installation
-----------------------------------

1. Stop case-e completely.
2. Copy the complete selected data directory, including ``ecrf.db`` and
   ``bids_datasets``.
3. Set ``ECRF_DATA_DIR`` to the copied directory or update the launcher config.
4. Start case-e and verify subjects, files, and exports before deleting the old
   copy.
