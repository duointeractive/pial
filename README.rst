=========================================
pial - Python Imaging Abstraction Library
=========================================

An overview
===========

pial is a re-packaging and adaption of sorl-thumbnails image manipulation
internals. The idea is to make the flexibility of sorl's engines available
to other projects in a simple, compact form.

Status
======

pial is currently in a state of flex while we develop and test. Using the
PILEngine should be pretty safe, but the others are currently in need of work.

Documentation
=============

Forthcoming. For now, check out the ``tests/pil_tests.py`` for examples of
how this module works.

Requirements
============

* Python 2.6+
* PIL or pgMagick or conver

Credit where it's due
=====================

Most of the hard work in putting this project together was done by the authors
of sorl-thumbnails. We just pulled it from their repo, dusted it off, and
re-packaged it as a separate project.

License
=======

The project is licensed under the `BSD License`_. The license for pial
remains the same as sorl-thumbnail's.

.. _BSD License: https://github.com/duointeractive/pial/blob/master/LICENSE