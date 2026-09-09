Troubleshooting
===============

Start with the visible symptom, then check application logs, browser developer
tools, service health, configuration, and permissions. Preserve relevant logs
without copying sensitive data into public tickets.

I cannot sign in
----------------

* Confirm the exact server URL and that all services are running.
* Check username/email spelling and keyboard layout.
* Ask an administrator whether the account is active and has a usable platform
  role.
* Check server time and reverse-proxy behavior if sessions expire immediately.

Self-service password recovery is temporarily disabled. Ask an Administrator to
issue a temporary password through User Management, then change it immediately
at the next login.

I can sign in but cannot see a study
------------------------------------

The account needs study-level **View** access unless it owns the study or is an
administrator. Ask the owner to inspect the access grant and any scope
restrictions.

I cannot enter data
-------------------

Confirm all of the following:

* the study is published;
* the account has **Add data** permission;
* the subject belongs to the expected group;
* the form section is assigned to that visit and group in the protocol matrix;
* the link, if used, has not expired or reached its use limit; and
* another active lock or conflict is not blocking the entry.

A dropped subject is intentionally read-only. Check the dropout badge/status
filter and use the audit event to confirm when and why entry was closed.

Save is blocked by validation
-----------------------------

Review the first reported field and check required state, number bounds, text
pattern, date/time range, choice coding, table cells, and files. If a value is
legitimately unavailable, use the supported skip workflow only when allowed by
the protocol.

My changes conflict with another edit
--------------------------------------

Another user saved a newer revision. Compare the field and table differences,
select the correct values, and save the resolved entry. Do not refresh blindly;
that may discard the information needed to resolve the conflict.

A shared link does not work
---------------------------

Check expiry, maximum uses, revocation state, subject/visit scope, section scope,
and capability. Test the exact URL in a private browser window. If replacing the
link, revoke the old one before distributing the new one.

An import row shows Warning or Error
------------------------------------

Recheck column mapping, identifiers, dates, decimals, units, required fields,
choice values, and subject/visit/group references. Commit only validated rows,
then reconcile the result against the source file.

An export looks incomplete
---------------------------

Review selected filters, study permissions, protocol assignments, version,
group anonymization, and pagination in the source view. Compare subject and
visit counts before and after export. Remember that analytical exports may omit
storage-level content included in a full archive.

For a combined-version ZIP, unchanged fields appear once using the latest
available value; changed fields receive version suffixes. Repeating-table
versions are snapshots rather than matched historical rows. Confirm the chosen
version mode and package-content options before reporting a missing column.

A file will not upload
----------------------

Check the field's permitted format, configured size, single/multiple setting,
browser connection, server request limit, storage capacity, and backend logs.
Client-side acceptance alone does not prove that server storage succeeded.

If case-e says the data was saved but a removed file could not be deleted, the
form update is already stored and the deletion remains queued. Keep the file
removed in the form and save the entry again, then verify the uploaded-files
browser.

The local service will not start
--------------------------------

* Confirm the documented Python and Node runtimes are installed.
* Check whether the configured ports are already occupied.
* Verify environment variables and database paths.
* Run the frontend and backend commands from their documented directories.
* Inspect the first error in the logs rather than subsequent cascade failures.

Requesting support
------------------

Include the application version, deployment type, affected workflow, time of
failure, exact error text, and sanitized reproduction steps. Never attach real
participant data, active shared links, credentials, or secret environment files
to a public issue.
