Conditional logic, assignments, and calculations
================================================

case-e has four related but distinct automation mechanisms. Select the one that
matches the intended behavior.

====================== ================================================
Feature                Purpose
====================== ================================================
Conditional visibility Show or hide a field
Popup reminder         Display guidance when a field value matches
Value assignment       Set another field to a configured value
Calculation            Derive a numeric result from one or more fields
====================== ================================================

.. _conditional-visibility-detailed:

Conditional visibility
----------------------

Open the target field's settings and select **Advanced**. The field being
edited is the field that will be shown or hidden.

#. Under **When conditions match**, choose **Show this field** or **Hide this
   field**.
#. Choose **All conditions must match (AND)** or **Any one condition may match
   (OR)**.
#. For each condition, choose the source section and source field.
#. Choose the operator and enter the comparison value. **Is empty** and **Is
   not empty** do not need a comparison value; **Between** needs From and To.
#. Add more conditions if necessary and read the generated rule summary.
#. Save the field settings, preview the form, and test both matching and
   non-matching states.

The action is important. With **Show**, the target is hidden until the rule
matches. With **Hide**, it is normally visible and disappears when the rule
matches. When a source field is itself hidden, dependent behavior should be
tested carefully with the value it previously held.

Visibility operators
~~~~~~~~~~~~~~~~~~~~

===================== =================================================
Source type           Operators
===================== =================================================
All supported types   Equals, does not equal, is empty, is not empty
Number, slider        Greater/greater-or-equal, less/less-or-equal, between
Date, time            Greater/greater-or-equal, less/less-or-equal, between
Text, text area       Contains, does not contain, starts with, ends with
Choice                Equals/does not equal; configured selection matching
Checkbox              Checked/unchecked equality
===================== =================================================

Choice dependencies are tied to option values. When an option is deleted, the
builder can remove affected visibility rules and asks the designer to review and
recreate logic if required.

.. _popup-reminders-detailed:

Popup reminders
---------------

Popup logic belongs to its current field; that field is always the source.

#. Open the source field's settings and select **Advanced**.
#. Enable **Enable pop-up message**.
#. Select the operator and comparison value. The controls adapt for number,
   date, time, single choice, multiple choice, checkbox, and between ranges.
#. Enter the reminder message.
#. Optionally enable **Do you want the message to be shown in target field
   too?**, then select the target section and target field.
#. Review the generated summary and save.

When the rule matches during data entry, the reminder is available below the
source field. With the target option enabled, the same reminder is also shown
below the selected target field. If the source field is hidden, its reminders
are not shown. Use reminders for instructions—not to perform data mutation.

Value assignments
-----------------

From the form builder, select **Value Assignments**. An assignment sets a target
field to a literal value when its conditions match.

#. Enter a descriptive **Rule name**.
#. Select the **Target field** and the value to assign. Choice, checkbox, date,
   time, number, and text-compatible targets receive an appropriate editor.
#. Decide whether to enable **Overwrite existing values**.
#. If overwrite is enabled, decide whether to **Clear the target when no rule
   matches**.
#. Under **Conditions**, choose AND (**All**) or OR (**Any**).
#. Add each source field, operator, comparison value, and optional upper bound.
#. Select **Add Assignment**, then inspect the saved rule summary.

Assignment target behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~

Assignment targets are read-only during data entry.

* Without overwrite, a matching rule fills the target only while it is empty.
* With overwrite, the matched result replaces the current target value.
* With clear-when-no-match, the target returns to the type-appropriate empty
  value when no rule for that target matches.
* Rules are grouped by target and evaluated in priority/order. The first
  matching rule for a target wins.
* The runtime repeats evaluation so that one assignment can feed another. It
  limits passes and reports a warning when a circular dependency may exist.

Assignment operators
~~~~~~~~~~~~~~~~~~~~

All types support equals, does-not-equal, empty, and not-empty. Number, slider,
date, and time add greater-than, greater-or-equal, less-than, less-or-equal, and
between. Text and text area add contains, does-not-contain, starts-with, and
ends-with. Dates use the source field's configured date format; times are
compared chronologically.

The source field cannot be the same field as the target. Output is coerced to
the target type. Invalid target choices or invalid numbers generate a warning
instead of silently storing an incompatible value.

Calculations
------------

From the form builder, select **Logic & Calculations**. The calculation screen
is divided into inputs, expression, and result/scoring.

#. Search or browse the form fields and select each input to insert its symbol.
#. Build the expression with the toolbar or type directly.
#. Use **Format** and **Validate** and resolve undefined symbols or syntax
   issues.
#. Choose an existing result field or **Create new field**.
#. When creating a field, select its section, name it, and set 0–10 decimals.
   case-e creates a read-only calculated number field.
#. For radio/select inputs, map every option to a numeric score. For checkboxes,
   map checked and unchecked states.
#. Choose the blank-input policy.
#. Review warnings and save the calculation.

Expression syntax
~~~~~~~~~~~~~~~~~

The toolbar supports ``+``, ``-``, ``*``, ``/``, exponent ``^``, remainder
``%``, parentheses, commas, constants 0/1/100, and ``pi``. Supported functions
include:

``mean()``
   Average of supplied values.

``min()`` and ``max()``
   Smallest or largest supplied value.

``round()``, ``ceil()``, and ``floor()``
   Numeric rounding functions.

``abs()``, ``sqrt()``, ``pow()``, and ``mod()``
   Absolute value, square root, power, and remainder operations.

``ifElse(condition, a, b)``
   Selects ``a`` or ``b`` according to a calculated condition.

``nz(value, fallback)``
   Replaces a blank value with the fallback, which defaults to zero.

Calculation blank policies
~~~~~~~~~~~~~~~~~~~~~~~~~~

Strict
   A missing numeric or scored input produces no calculated result.

Zero
   A missing numeric or scored input is evaluated as zero.

The final numeric result is rounded to the configured decimal count. The result
field must not also be an input. An existing target controlled by a value
assignment cannot be selected for a calculation; the editor reports the
conflict.

Safe design and testing
-----------------------

* Give every field a stable identifier before creating logic.
* Prefer one responsibility per target: visibility, assignment, or calculation.
* Test boundaries, blanks, every choice, AND/OR combinations, and hidden-source
  states.
* Test assignment rule order when several rules share a target.
* Test calculation scoring for every stored option.
* Re-test logic after renaming fields, changing types, or editing options.
* Preview every visit/group combination because protocol assignment determines
  whether source and target fields are present together.
