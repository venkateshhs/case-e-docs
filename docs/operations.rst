Storage, backup, and operations
===============================

case-e supports a lightweight local workflow and a server-hosted workflow. The
correct choice depends on the number of users, data sensitivity, availability
needs, and the organization's operating controls.

Local mode
----------

Local mode uses SQLite and filesystem-backed data. It is appropriate for
development, demonstrations, evaluation, and controlled single-machine work.

* Keep the database and upload directories outside ephemeral build folders.
* Do not expose the development server directly to a network.
* Stop writes before taking a simple file-level copy, or use a database-safe
  backup method.
* Protect the workstation with encryption, access control, updates, and backups.

Hosted mode
-----------

A hosted deployment uses server components such as PostgreSQL and the configured
DataLad/RIA-backed dataset storage. Place the application behind TLS, use durable
volumes, manage secrets outside source control, and monitor all services.

Production hosting requires more than starting containers. Define ownership for
patching, certificates, database maintenance, storage capacity, incident
response, recovery, and user support.

What to back up
---------------

A complete recovery set includes:

* the PostgreSQL database or local SQLite database;
* uploaded files and DataLad/RIA storage, where configured;
* application configuration and environment variables;
* reverse-proxy and TLS configuration;
* deployment manifests and the exact application version; and
* any encryption keys or credentials needed to read the backup.

Keep credentials in the backup system's secret store, not in the same plaintext
archive as the data.

Restore testing
---------------

#. Restore into an isolated environment.
#. Start the database and storage services.
#. Start the application using the restored configuration.
#. Sign in with a recovery test account.
#. Open representative studies, entries, versions, and attachments.
#. Generate and compare a test export.
#. Record recovery time and any manual steps.

Monitoring
----------

Monitor service health, HTTP errors, login failures, database connections,
volume capacity, backup completion, certificate expiry, and application logs.
Avoid logging participant data or secrets. Define alert recipients before
production launch.

Upgrades
--------

#. Read release and migration notes.
#. Take and verify a recovery point.
#. Rehearse the upgrade with a copy of representative data.
#. Deploy during an approved maintenance window.
#. Run smoke tests for login, study view, entry save, file access, sharing, and
   every required export.
#. Keep a documented rollback decision and procedure.

Close-out and retention
-----------------------

At study close-out, revoke shared links, review accounts, create the approved
final exports and archive, verify restoration, and apply the retention schedule.
Deletion must follow institutional policy and should never be used as an
informal substitute for controlled archival.
