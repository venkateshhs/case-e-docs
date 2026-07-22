Forms, sections, and custom fields
==================================

The form builder creates reusable case-report forms from sections and fields.
Forms may be built from scratch, loaded from a saved template, or assembled
using specialized clinical fields and supported ontology terms.

Design hierarchy
----------------

Study
   Contains visits, groups, subjects, users, and forms.

Form
   A named CRF such as Demographics or Adverse Events.

Section
   A logical block within a form. Protocol assignments are made at section
   level, allowing the same form to vary by visit or group.

Field
   A single response, upload, calculation, choice, or table.

Supported field types
---------------------

Text
   Single-line text with length, pattern, transformation, default, help text,
   required, and read-only options.

Text area
   Multi-line narrative text with the relevant text constraints.

Number
   Numeric value with minimum, maximum, step, integer-only, and decimal-digit
   controls.

Checkbox
   Boolean or multi-choice selection, depending on field configuration.

Radio buttons
   Exactly one value from a visible list of choices.

Dropdown / select
   One value from a compact option list.

Date and time
   Date or time input with display format and supported lower/upper bounds.

File
   Upload or URL reference with permitted formats, size guidance, multiple-file
   behavior, and optional BIDS modality metadata.

Slider / Likert
   Bounded numeric or ordinal scale with marks and endpoint labels.

Table
   Repeating row data with defined columns, validation, and row-level editing.

Common field settings
---------------------

Most fields support a label, internal identifier, help text, required state,
read-only state, and default value. Internal identifiers should be stable,
machine-friendly, and unique within their scope. Treat them as export schema:
renaming an identifier after collection starts may break downstream scripts.

Choice fields
-------------

For radio, checkbox, and dropdown fields, define stable stored values and clear
display labels. Keep values unique and avoid changing their meaning later. If an
option is retired, consider preserving it for historical interpretation rather
than silently reusing its code.

File fields
-----------

File configuration can restrict expected formats and maximum size, allow one or
multiple files, and choose upload or URL-style collection. BIDS-related modality
metadata supports structured imaging or research datasets.

Browser-side extension and size checks improve usability; they are not a full
malware or content-security control. Production deployments need server-side
limits, safe content handling, access controls, and backup policies.

Conditional visibility
----------------------

A field or section can be shown according to answers elsewhere in the form.
Combine conditions with **AND** when all must match, or **OR** when any may match.
Test the false-to-true and true-to-false transitions, especially when a hidden
field already contains data.

Calculations and assignments
----------------------------

Calculated fields derive a value from other fields. Value assignments set a
target based on configured rules; when several rules could match, the first
matching assignment wins. The builder checks for circular dependencies, but the
designer must still test missing values, decimals, and conditional inputs.

Popup reminders
---------------

Popup rules can show instructions or safety reminders in response to entered
values. Write messages that tell the user what to verify or do next. A popup is
decision support, not a substitute for protocol training or clinical judgment.

Tables
------

Use a table for naturally repeating records such as medications or adverse
events. Define column types and validation before collection. Confirm that
adding, editing, copying, and removing rows works on both desktop and the
smallest supported screen.

Templates and section saving
----------------------------

The builder can save a complete form or selected sections as a reusable design
template. This is what **section saving** means: preserving form design for reuse
in another form or study. It does not mean partially saving only one section of
an in-progress participant data entry; entry saving applies to the form slot.

When loading a template, review identifiers, conditional references,
calculations, protocol assignments, and controlled terminology. A template is a
starting point, not automatic protocol validation.

Form design checklist
---------------------

* Keep one concept per field.
* Use coded choices instead of free text where the protocol defines a list.
* Add units to labels and exports.
* Use required fields only where missingness is truly unacceptable.
* Provide help text for ambiguous definitions.
* Test constraints at both valid and invalid boundaries.
* Avoid calculations that depend on a conditionally hidden value.
* Preview the form in every assigned visit and group.
