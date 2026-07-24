Field settings and constraints
==============================

Every field has a **Field Settings & Constraints** dialog with **Basic** and
**Advanced** tabs. In the form builder, locate the field and select its settings
button. Save the dialog, then save the form or draft before leaving the builder.

Basic settings shared by most fields
------------------------------------

Required
   Prevents a normal save until a value is entered or the supported
   skip-required workflow is used.

Readonly
   Displays the field without permitting manual entry. Calculated and
   value-assignment target fields are also made read-only by their logic.

Placeholder
   Hint displayed inside an empty compatible control. Checkboxes, tables,
   file fields, dates, and slider mode use more appropriate controls instead.

Help text
   Guidance displayed under the control. Use it for definitions, units, and
   entry instructions rather than embedding long instructions in the label.

Default value
   Initial value for a new entry. The control is adapted to the field type:
   typed text/number, choice list, multiple-choice chips, time input, or a
   checked/unchecked checkbox. Dates have their own formatted default control.

Change a field type
-------------------

The Basic tab can convert a non-table field to another supported type. The
dialog shows a conversion warning when incompatible settings or values may be
lost. For a lossy conversion, enable **I understand and want to continue**
before saving.

Visibility and popup configuration are preserved during the conversion preview,
but type-specific values and options can require correction. If choice options
are removed, case-e identifies dependent visibility and assignment rules. Review
the option-remapping dialog and every dependent rule after the conversion.

Text and text-area settings
---------------------------

* **Min length** and **Max length** constrain character count.
* **Regex pattern** applies a regular-expression format check, for example
  ``^[A-Za-z]+$``.
* **Transform** can preserve the input, convert to uppercase or lowercase, or
  capitalize it.

Patterns validate format; they should not be used to encode a complex clinical
decision. Test empty, minimum, maximum, invalid, Unicode, and pasted values.

Number settings
---------------

* **Min value** and **Max value** define inclusive bounds.
* **Step** defines permitted increments where enforced by the control and
  validator.
* **Integer only** rejects fractional values.
* **Min digits** and **Max digits** apply to the integer part when integer-only
  validation is used.

Use a text field with a pattern for identifiers that require leading zeroes.
Use a number field only when arithmetic meaning is intended.

Date settings
-------------

Choose the stored/displayed **Date format**, then optionally set **Min date**,
**Max date**, and **Default date**. The configured format is reused by
visibility logic and value assignments when dates are compared. A default must
also satisfy the configured range.

Time settings
-------------

Choose a **24-hour** or **12-hour (AM/PM)** display, and optionally configure
**Min time**, **Max time**, and a default. Runtime comparisons convert valid
times to seconds, so equality, ordering, and between rules use chronological
order.

Choice settings
---------------

Radio and dropdown fields provide an option editor with:

* number of options;
* add and remove controls;
* ascending/descending sorting; and
* direct editing of each option label.

A radio field can enable **Allow multiple selections**, in which case defaults
are edited as chips and stored as a list. Dropdowns are single-select in the
current builder. Removing or renaming an option may affect defaults,
visibility rules, popup rules, value assignments, and calculation scoring.

Checkbox settings
-----------------

A checkbox supports required, read-only, help text, and checked-by-default.
It has no placeholder. Conditions and assignments represent its value as
checked/unchecked; calculation scoring maps both states to numbers.

File settings
-------------

Allowed formats
   Comma-separated extensions or MIME patterns such as ``.pdf``, ``.csv``,
   ``image/*``, or ``application/zip``.

Max size (MB)
   Client-side maximum accepted by the control. Production hosting must also
   enforce an appropriate server and reverse-proxy limit.

Storage behavior
   **Local storage (upload)** presents a file picker. **Link via URL** stores a
   reference instead.

Allow multiple files
   Changes the entry value between one file and a collection of files.

Modalities (BIDS)
   Select built-in modalities or add a custom modality. This metadata helps
   organize and name supported files in BIDS output.

Slider settings
---------------

Choose **Slider** or **Likert scale** as the control type.

Slider mode supports minimum, maximum, step, percentage mode (1–100), and
optional labels at selected step values. Labels do not change snapping; the
track jumps to the nearest configured step. A slider intentionally has no
default selection.

Likert mode supports minimum, maximum, and left/right endpoint labels. It shows
only endpoints and limits the number of displayed points to avoid an unusable
control.

Table settings and copying
--------------------------

Tables define repeating rows and typed columns. Table field controls support
adding, editing, copying, and deleting rows during data entry. In the builder,
the complete-copy option preserves all columns, column types, options, advanced
settings, and show/hide logic. Basic copy preserves only basic field settings;
columns and advanced settings are intentionally not copied.

Advanced tab
------------

The Advanced tab contains two independent features:

Conditional visibility
   Show or hide the current field according to one or more other fields. See
   :ref:`conditional-visibility-detailed`.

Popup reminder
   Display a message when the current field matches a rule, optionally beneath
   another selected target field too. See :ref:`popup-reminders-detailed`.

Clearing and saving
-------------------

**Save** applies the dialog state. **Clear** resets the settings to their
initial/default configuration. **Cancel** closes without applying the current
dialog edits. Saving the dialog does not replace saving the overall study draft.
