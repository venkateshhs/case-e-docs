case-e documentation
====================

.. raw:: html

   <div class="hero-copy">
     <strong>Clinical data collection, documented end to end.</strong><br>
     Build studies, design forms, collect and review data, collaborate securely,
     and run case-e locally or on your own server.
   </div>
   <div class="workflow-grid">
     <div><span>01</span><b>Create</b><small>Study · groups · visits</small></div>
     <div><span>02</span><b>Design</b><small>Sections · fields · logic</small></div>
     <div><span>03</span><b>Collect</b><small>Subjects · forms · files</small></div>
     <div><span>04</span><b>Review</b><small>Dashboard · audit · export</small></div>
   </div>
   <div class="casee-link-bar">
     <a href="getting-started.html">Run case-e locally</a>
     <a href="deployment.html">Host case-e on a server</a>
     <a href="https://venkateshhs.github.io/case-e-docs/">Hosted documentation</a>
     <a href="https://github.com/venkateshhs/eCRF">Application source</a>
   </div>

case-e is a web-based electronic case report form system for defining clinical
studies and collecting structured participant data. It combines study design,
versioned form templates, role-based access, field validation, file handling,
audit history, dashboards, and portable exports in one application.

What case-e supports
--------------------

Study setup
   Draft and published studies; metadata; groups; generated subject IDs;
   manual, random, or sequential assignment; visits; protocol matrices;
   independent editing steps; template versioning; and deletion.

Form design
   Text, textarea, number, checkbox, radio, dropdown, date, time, file,
   slider/Likert, and table fields; OBI terminology search; specialized clinical
   fields; reusable complete-form and selected-section templates.

Data quality
   Required and read-only fields, defaults, ranges, patterns, lengths, dates,
   times, choices, file constraints, conditional visibility, pop-up reminders,
   calculations, value assignments, and explicit required-value skipping.

Data collection
   Subject-by-visit selection matrix, completion status and percentages,
   spreadsheet import, previous-visit copying, repeating tables, file upload,
   conflict resolution, and unsaved-change protection.

Collaboration
   Study-specific View, Add data, and Edit study grants; view-only or add-data
   shared links; section-restricted and bulk links; expiry and use limits;
   revocation; and CSV link export.

Review and export
   Version-aware data tables, filters, sorting, pagination, audit history and
   diffs, CSV/Excel data export, JSON template export, and ZIP transfer or
   archive bundles.

Deployment
   Local SQLite/filesystem use, packaged desktop builds, Docker Compose, or a
   Linux systemd/Apache installation backed by PostgreSQL and DataLad/RIA.

.. note::

   This guide follows the current case-e frontend, backend routes, environment
   templates, and deployment scripts. Screens marked as unfinished by the
   application are identified in :doc:`limitations`.

Start here
----------

New users should begin with :doc:`getting-started`, then follow
:doc:`studies` and :doc:`form-design`. Administrators should also read
:doc:`administration`, :doc:`deployment`, and :doc:`operations` before a
shared or production installation.

.. toctree::
   :maxdepth: 2
   :caption: Get started

   getting-started
   deployment

.. toctree::
   :maxdepth: 2
   :caption: Administration

   administration

.. toctree::
   :maxdepth: 2
   :caption: Use case-e

   studies
   form-design
   field-settings
   form-logic
   data-collection
   collaboration
   review-export

.. toctree::
   :maxdepth: 2
   :caption: Complete reference

   application-reference
   feature-index

.. toctree::
   :maxdepth: 2
   :caption: Operate case-e

   operations
   troubleshooting
   limitations
   glossary
