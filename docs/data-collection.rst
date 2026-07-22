Subjects, visits, and data collection
=====================================

Routine data collection starts from the subject-by-visit matrix. Each available
cell represents a form slot for one subject and one visit, subject to the
protocol matrix, group assignment, and the user's permissions.

Open a data-entry form
----------------------

#. Open a published study.
#. Go to **Data entry**.
#. Search for or select a subject.
#. Select the required visit and form slot.
#. Confirm the subject, visit, group, and form shown in the header.
#. Enter data and resolve validation messages.
#. Select **Save Data**.

The save action writes the whole available entry. It is not an independent save
for only the currently visible section. If you leave with unsaved changes, the
application warns before navigation; do not rely on that warning as a substitute
for saving.

Validation and missing data
---------------------------

Required fields and configured constraints are checked before a normal save.
Where the workflow permits it, a required value can be explicitly skipped. A
skipped required field is different from a value that has never been reviewed
and is highlighted accordingly in data views.

Use the skip mechanism only under the protocol's missing-data rules. If a reason
must be recorded, provide it in the designated field or operational workflow.

Repeating tables
----------------

For table fields, add one row for each repeating event or item. Validate every
column before saving. Row operations are part of the same form entry, so save the
entry after adding, copying, editing, or deleting rows.

Files
-----

For an upload field, select a permitted file and wait for the interface to show
that it is attached before saving. For URL mode, enter the approved location.
Multiple-file fields may accept several objects. Never upload directly
identifying material unless the protocol, permissions, and hosting environment
explicitly allow it.

Import from a previous visit
----------------------------

When the same information is collected repeatedly, **Import previous visit** can
copy supported values into the current entry, including supported table rows.
Always review the imported values before saving; the previous answer may no
longer be true.

Clear an entry
--------------

**Clear** removes entered values from the current form. Confirm the subject,
visit, and form before using it. If records must be retained for audit or
regulatory reasons, follow the approved correction workflow rather than clearing
data simply to hide an error.

Bulk import
-----------

case-e supports tabular import from CSV, XLSX, and XLS files.

#. Start the import from the relevant study.
#. Upload the source file.
#. Map source columns to study fields.
#. Review the preview status for every row:

   * **Ready** — the row passed the current checks;
   * **Warning** — the row can require attention but may still be usable;
   * **Error** — the row cannot be committed as shown.

#. Correct mapping or source problems.
#. Commit only the validated rows.
#. Reconcile imported record counts and inspect a sample in the normal data
   view.

An import preview does not prove semantic correctness. Verify units, date
formats, choice coding, subject identifiers, group/visit mapping, and decimal
conventions before committing.

Concurrent editing
------------------

Entries use revision information to detect edits based on an older version. If
another user saved first, case-e can present field or table conflicts for review.
Choose values deliberately rather than overwriting the newer record. Editing
locks reduce collisions but do not replace communication between data-entry
staff.

Completion workflow
-------------------

Use the matrix indicators to identify expected, incomplete, or completed slots.
Before marking a visit operationally complete:

* confirm every expected form is available;
* resolve validation errors and unexplained skipped fields;
* check repeating rows and uploads;
* save all modified entries; and
* review the corresponding row in **View data**.
