Create and manage a study
=========================

A study contains the protocol structure, user assignments, subjects, visits,
forms, and collected data. Build and test the design while it is in **Draft**,
then publish it before routine data collection.

Study lifecycle
---------------

Draft
   The design can change freely. Draft studies are not available for normal
   data collection.

Published
   The study is active for data collection. Structural changes must be made
   deliberately because existing records may depend on the design.

Revised
   A published study has been updated. Validate revisions against existing
   entries and communicate them to the study team.

The subject identifier pattern is locked after publication. Choose and test it
before publishing. Study deletion is permanent; export and verify a backup
before deleting a study.

Create a study
--------------

#. Select **Create study** from the study dashboard.
#. Enter a clear title, short identifier, description, owner, and protocol
   details.
#. Define study groups, such as treatment arms, sites, or cohorts.
#. Configure the subject identifier pattern and starting sequence.
#. Add visits in protocol order.
#. Create or import forms and arrange their sections.
#. Use the protocol matrix to assign form sections to visits and groups.
#. Add users and grant the minimum study permissions.
#. Test the complete workflow with non-production subjects.
#. Publish the study when the design is approved.

Groups
------

Groups can represent arms, cohorts, sites, or another protocol-defined
partition. A subject is assigned according to the study design. Groups also
control which form sections appear in the protocol matrix and can be used in
scoped exports or anonymization workflows.

Do not use a group name as the only record of a real-world treatment. Preserve
the protocol definition and coding rules in the study documentation.

Subjects
--------

The subject identifier pattern creates consistent, non-identifying record IDs.
Before publication:

* choose a prefix or format that does not reveal personal information;
* verify uniqueness and sequence behavior;
* confirm that sites or cohorts can be distinguished only if the protocol
  requires it; and
* document how screening failures, withdrawals, and replacements are handled.

After subjects exist, use the subject-by-visit matrix to see expected forms and
completion progress. Search is available for large subject lists.

Visits
------

Create visits in the order used by the protocol—for example Screening,
Baseline, Week 4, and Close-out. A visit is a collection point, not a form.
Assign the relevant form sections to each visit through the protocol matrix.

When revising visits after data collection has started, check whether entries
already exist for the affected subject/visit slots. Never rename a visit merely
to change the meaning of historical data.

Protocol matrix
---------------

The protocol matrix maps three dimensions:

* form section;
* visit; and
* study group.

An enabled matrix cell means that the section is expected for that group at that
visit. Review the matrix horizontally by visit and vertically by form section.
Missing assignments can make a form unavailable to data-entry users; excessive
assignments can create forms that the protocol does not require.

Publish safely
--------------

Before selecting **Publish**:

* create test subjects in every group;
* enter valid, invalid, missing, and boundary values;
* test conditional fields, calculations, tables, and file fields;
* verify every matrix assignment;
* test each role with a representative user;
* preview exports and shared links; and
* archive the approved study definition.

Revisions
---------

For a published study, make the smallest possible revision. Record the reason,
test it with existing data, and check export column stability. Removing or
changing a field can make previous values difficult to interpret even if the
database still retains history.
