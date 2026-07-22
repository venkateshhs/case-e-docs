Hosted deployment
=================

case-e automatically selects the server profile when ``ECRF_ENV=production``,
a PostgreSQL database URL, or a RIA URL is present. Set ``ECRF_PROFILE=server``
explicitly in production so the intended behavior is unambiguous.

Docker Compose
--------------

The supplied stack starts PostgreSQL 16, case-e, an Apache reverse proxy,
persistent runtime storage, and a file-based DataLad RIA store.

1. Create production settings.

   .. code-block:: console

      cd deploy/docker
      cp .env.example .env
      chmod 600 .env

2. Replace every placeholder in ``.env``. Use a long random secret and a unique
   administrator password.

3. Replace ``casee_password`` in both the PostgreSQL service and
   ``ECRF_DATABASE_URL`` in ``docker-compose.yml``. Prefer Docker secrets or an
   external secret manager for a durable deployment.

4. Build and start the stack.

   .. code-block:: console

      docker compose up -d --build
      docker compose ps
      ./scripts/smoke-test.sh http://localhost:8080

5. Put an HTTPS reverse proxy in front of the service, use the correct forwarded
   protocol headers, set ``ECRF_CORS_ALLOW_ORIGINS`` to the exact final HTTPS
   origin, and do not publish PostgreSQL port 5432 to the public internet.

Persistent volumes
~~~~~~~~~~~~~~~~~~

======================== ===============================================
Volume                   Contents
======================== ===============================================
``casee_postgres_data``   Users, sessions, metadata, entries, and grants
``casee_runtime_data``    Canonical study datasets and uploaded files
``casee_ria_store``       DataLad RIA history and annexed content
======================== ===============================================

.. warning::

   Back up all three volumes as a consistent set. A database-only backup cannot
   restore uploaded files or the complete study history.

Linux server with systemd and Apache
------------------------------------

The manual path targets Debian or Ubuntu and runs case-e from ``/opt/casee`` as
the ``casee`` service user.

1. Copy the repository to ``/opt/casee`` and build the frontend.
2. Copy ``.env.example`` to ``/opt/casee/.env`` and configure PostgreSQL,
   secrets, CORS, data folders, and RIA access.
3. Run the installer.

   .. code-block:: console

      sudo ./deploy/install_hosted.sh /opt/casee casee casee
      sudo systemctl status casee
      curl -fsS http://127.0.0.1:8000/health

4. Edit ``deploy/docker/apache/casee-ssl.conf`` for the real hostname and
   certificate paths, install it into Apache, enable SSL, headers, and proxy
   modules, and redirect HTTP to HTTPS.

The systemd service reads ``/opt/casee/.env``, runs preflight checks, and starts
``uvicorn eCRF_backend.datalad_main:app``. It restarts automatically and its
filesystem hardening permits writes only beneath ``/opt/casee`` and
``/srv/casee``.

Configuration reference
-----------------------

============================================ ===============================
Variable                                     Purpose / hosted recommendation
============================================ ===============================
``ECRF_ENV``                                 ``production``
``ECRF_PROFILE``                             ``server``
``ECRF_DATABASE_URL``                        PostgreSQL SQLAlchemy URL
``ECRF_SECRET_KEY``                          Long, unique token-signing secret
``ECRF_CORS_ALLOW_ORIGINS``                  Exact comma-separated HTTPS origins
``ECRF_BIND_HOST``                           ``0.0.0.0`` behind the proxy
``ECRF_PORT``                                Application port, normally ``8000``
``ECRF_DATA_DIR``                            Runtime root, e.g. ``/srv/casee``
``BIDS_ROOT``                                Canonical dataset root
``ECRF_TEMPLATES_DIR``                       Backend template JSON directory
``ECRF_DB_AUTO_CREATE``                      ``1`` for provisioning, then ``0``
``ECRF_BOOTSTRAP_ADMIN``                     ``1`` once, then ``0``
``ECRF_ADMIN_*``                             Initial administrator identity
``ECRF_DATALAD_MODE``                        ``primary``
``ECRF_DATALAD_RIA_URL``                     ``ria+ssh://`` or ``ria+file://`` URL
``ECRF_DATALAD_PUSH_ON_SAVE``                ``1``
``ECRF_DATALAD_REQUIRE_RIA_FOR_WRITES``      ``1`` for protected hosted writes
``ECRF_DATALAD_LOCK_TIMEOUT_SECONDS``        Normally ``120``
============================================ ===============================

Production validation rejects a missing database URL, SQLite unless explicitly
allowed, the known default secret, missing CORS configuration, or bootstrap
administration without an explicit password.

Verification
------------

.. code-block:: console

   python -m eCRF_backend.preflight
   curl -fsS http://127.0.0.1:8000/health
   sudo journalctl -u casee -n 200 --no-pager

Preflight checks database configuration, writable data directories, template
availability, Git and git-annex, the DataLad Python import, Git identity, and RIA
reachability when required.
