Review, audit, and export
=========================

Use **View data** to review collected records before analysis or handoff. Export
is a snapshot; it does not replace the live entry history or the study's backup.

View data
---------

The data table presents one row for a subject/visit record and groups columns by
form structure. Depending on the view, you can:

* select a saved version;
* sort and filter rows;
* choose 50 or 100 rows per page;
* use **View all** for datasets up to the supported 1,000-row limit;
* download permitted file attachments; and
* distinguish unavailable assignments and skipped required values.

Cells shown in gray indicate that the form or field is not assigned in that
subject/visit context. Skipped required values are shown in red. Interpret these
states separately from an ordinary empty value.

Versions and audit information
------------------------------

Version selection allows an earlier saved state to be inspected. Audit
information helps establish who changed data and when. The exact records
required for a regulated audit trail depend on deployment policy and validation;
confirm that the installed configuration meets the organization's requirements
before production use.

Export formats
--------------

CSV
   A plain tabular export suitable for analysis tools and scripted pipelines.

Excel-compatible XLS
   A spreadsheet-oriented export for convenient review. It is
   Excel-compatible output and should not be assumed to be a native XLSX
   workbook.

JSON template
   A machine-readable study definition. Export the whole definition or a
   selected subset when the interface allows it. Use this for controlled study
   design transfer, not as the only participant-data backup.

ZIP archive
   A fuller packaged export available in owner/administrator workflows. Merge or
   archive options may be available depending on storage mode.

BIDS folder
   An owner/administrator local-mode workflow for supported BIDS-oriented files
   and metadata.

Export data
-----------

#. Open the study and select **Export**.
#. Choose the required subjects, visits, groups, forms, or sections if filtering
   is available.
#. Select the output format.
#. Enable group-based anonymization only after reviewing its transformation
   rules.
#. Generate and download the export.
#. Verify record counts, columns, coding, missing-value representation, dates,
   units, and attachments.
#. Store the file in an approved location and record the export date and purpose.

Anonymization
-------------

Group anonymization can reduce direct identification in an export, but it does
not automatically make a dataset anonymous. Free text, dates, rare diagnoses,
file metadata, URLs, images, and small groups can remain identifying. Perform a
formal disclosure-risk review for any external release.

Reproducible handoff
--------------------

For analysis, keep together:

* the exported data;
* the corresponding JSON study definition;
* export filters and anonymization settings;
* application version and export time;
* a checksum when required; and
* the analysis code or data dictionary that interprets field identifiers.

Backup versus export
--------------------

CSV and spreadsheet exports are analytical extracts. A recovery backup must also
cover the database, uploads or dataset storage, server configuration, and the
keys or credentials required to restore service. Test restoration instead of
assuming that copied files are usable.
