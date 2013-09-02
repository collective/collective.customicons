Installation
============
- If you want to use this addon together with archetypes depend your buildout
  on ``collectice.customicons[archetypes]``

- If you want to use this addon together with dexterity depend your buildout
  on ``collectice.customicons[dexterity]``

- ZCML is loaded automagically with z3c.autoinclude.
  Install it as an addon in the Plone control-panel or portal_setup.
  This package is written for Plone 4.3 or later.

Archetypes
----------

- By default the schemaextender is activated for folder and link content types.

- If you want to activate it on other types you need to add some lines to your
  integration addons configure.zcml like so::
  
    <class class="Products.ATContentTypes.content.document.ATDocument">
        <implements interface="collective.customicons.interfaces.ICustomIcon" />
    </class> 

Dexterity
---------

- To make this product work with dx, you need to enable the behavior for i.e.
  folders via the dexterity-types admin controlpanel. Click on the Folder type
  and under the behaviors-tab you'll find the custom icon behavior.
  Activate it and you're ready to go.


Usage
=====

- With this product installed, you can specify an imagepool-folder via
  the admin controlpanel. Inside this folder you put the images you want.
  When you edit a folder you can either choose a customicon from the imagepool-
  folder, or browse on your local machine for an image.

- When there is an imagepool-image and an uploaded image simultaneously
  specified for a folder, the the uploaded image will be taken and the
  pool-image will be ignored.


Source Code and Contributions
=============================

If you want to help with the development (improvement, update, bug-fixing, ...)
of ``collective.customicons`` this is a great idea!

The code is located in the
`github collective <https://github.com/collective/collective.customicons`_.

You can clone it or `get access to the github-collective
<http://collective.github.com/>`_ and work directly on the project.

Maintainer is Benjamin Stefaner and the BlueDynamics Alliance developer team. We
appreciate any contribution and if a release is needed to be done on pypi,
please just contact one of us
`dev@bluedynamics dot com <mailto:dev@bluedynamics.com>`_

Contributors
============

- Jens W. Klein <jens@bluedynamics.com>
- Benjamin Stefaner <bs@kleinundpartner.at>

