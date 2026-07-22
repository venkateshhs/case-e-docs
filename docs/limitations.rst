Known boundaries and validation notes
=====================================

This page distinguishes supported workflows from assumptions that should not be
made during deployment or protocol validation.

Current product boundaries
--------------------------

* There is no separate Viewer platform role. Use a study-level **View** grant for
  read-only access.
* Draft studies are not intended for routine data collection.
* The subject identifier pattern locks after publication.
* **Study Configurations** is a placeholder area in the current interface.
* **Study Settings** should be treated as not fully implemented until the
  installed version is verified.
* **View all** is intended for data views up to 1,000 rows; use export for larger
  analysis workflows.
* Spreadsheet export is Excel-compatible ``.xls`` output and is not necessarily
  a native ``.xlsx`` workbook.
* Section-template saving reuses form design; it is not a partial participant
  entry save.
* A local development setup is not a secure multi-user production deployment.
* Browser file checks do not replace server-side security controls.

Clinical and regulatory validation
----------------------------------

case-e functionality must be evaluated in the context of the installed version,
hosting controls, protocol, jurisdiction, and intended use. Documentation alone
does not establish compliance with GCP, GDPR, HIPAA, 21 CFR Part 11, or another
standard.

Before production use, the responsible organization should define requirements,
perform risk assessment, qualify infrastructure, validate configured workflows,
test audit and recovery behavior, train users, and control changes.

Design changes after publication
--------------------------------

Although revision workflows exist, changing fields, choices, calculations,
visits, or assignments after collection starts can alter interpretation and
exports. Preserve the approved definition and test all changes against historical
records.

Data anonymization
------------------

Export anonymization features reduce selected identifiers but cannot guarantee
anonymous output. Free text, timestamps, images, URLs, rare combinations, and
file metadata can identify a participant. Apply a separate disclosure-control
process before sharing data outside the approved team.

Documentation versioning
------------------------

Host these docs from a branch or tag that corresponds to the deployed case-e
version. When behavior differs, the installed application and its validated
release notes take precedence over documentation for another version.
