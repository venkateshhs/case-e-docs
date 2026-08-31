Administration and user management
==================================

This chapter is for platform administrators and study owners. It explains the
account model, platform roles, study-level permissions, and the checks to make
before granting access to clinical data.

User roles
----------

Every account has one platform role:

Administrator
   Full platform access. Administrators can manage users, inspect all studies,
   change study access, and perform owner-level export and maintenance tasks.

Principal Investigator
   Can create and own studies and can be granted access to other studies.

Investigator
   Works only in studies explicitly shared with the account.

No Access
   The account can authenticate but cannot work with study data until an
   administrator changes the role or a study owner grants appropriate access.

There is no separate ``Viewer`` platform role. Read-only access is created by
granting **View** permission on a particular study without granting **Add data**
or **Edit study**.

Create and manage users
-----------------------

#. Sign in as an Administrator.
#. Open **Administration** and then **Users**.
#. Create an account with the person's name, email or username, and platform
   role.
#. Communicate initial credentials through an approved secure channel.
#. Confirm the user can sign in and sees only the intended studies.

Administrators can set a generated temporary password for another account. The
password is displayed for secure handoff and the account is required to change
it at next login. An Administrator cannot use that operation for their own
account; use **Change Password** instead. Users marked for a required password
change are routed directly to that screen after login.

When a person changes responsibilities, update both the platform role and every
study access grant. Disabling or downgrading a platform account does not replace
a review of study-specific access.

Study-level permissions
-----------------------

Study access is additive. A study owner or administrator can grant one or more
of the following permissions:

View
   Open the study, browse subjects and visits, and inspect entered data.

Add data
   Create or update case-report-form entries in the assigned study scope.

Edit study
   Change study design, forms, visits, groups, assignments, and sharing
   configuration. Grant this only to trained study designers.

The study owner and platform administrators retain full control. Sensitive
operations such as complete study archives, storage-level dataset actions, and
access management are restricted to owner or administrator workflows.

Study documents use a narrower set of checks in the current application:

* an owner, Administrator, or user with **Add data** can upload, describe, edit
  descriptions, and delete study-level attachments; and
* download is available to the owner/Administrator, or to a granted user only
  when **View**, **Add data**, and **Edit study** are all enabled.

Review these rules when assigning document-management duties; **View** alone is
not sufficient to download a study document.

Grant access to a study
-----------------------

#. Open the study.
#. Open **Access** or **User access**.
#. Select an existing user.
#. Enable the minimum required permissions.
#. If the interface offers group, visit, or subject scope, narrow the grant to
   the person's actual assignment.
#. Save, then verify the result using a test account with the same role.

Access review checklist
-----------------------

Perform an access review at study activation, at regular intervals, and when a
team member joins or leaves.

* Remove accounts that no longer require access.
* Avoid granting **Edit study** to routine data-entry staff.
* Confirm shared links have an expiry and use limit.
* Review group assignments before exporting anonymized data.
* Keep at least two current administrators to avoid an administrative lockout.
* Record access changes in the study's operational documentation.

.. _password-recovery-admin:

Password recovery
-----------------

When hosted password recovery is enabled, the login page offers **Forgot
password?**:

#. The user enters their username.
#. case-e returns only a masked email address and asks the user to confirm it.
#. After confirmation, case-e emails a one-time reset link.
#. The user enters and confirms a new password of at least eight characters,
   including a number and one of ``!@#$%^&*``.
#. A successful reset clears the temporary-password requirement, consumes all
   outstanding reset tokens for the account, revokes the account's existing
   sessions, and writes a system audit event.

The default emailed reset link expires after 20 minutes and the username/email
confirmation after 10 minutes. By default, case-e permits three reset emails per
user per hour and ten username lookups per requesting IP per hour. A newer reset
request invalidates unused earlier reset links. Accounts without a stored email
cannot use self-service recovery and must contact an Administrator.

The feature is disabled until the operator configures SMTP and the public
frontend URL. Do not enable it with example values. See
:ref:`hosted-password-reset` for deployment settings.

Security responsibilities
-------------------------

case-e provides application permissions and audit information, but the hosting
organization remains responsible for identity lifecycle, passwords, TLS,
backups, host security, retention, and compliance validation. Do not treat a
development server or an unencrypted local database as a production clinical
deployment.
