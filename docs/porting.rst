Porting
=======

**Porting existing PKPIL-based code to PKPillow**

PKPillow is a functional drop-in replacement for the Python Imaging Library.

PKPIL is Python 2 only. PKPillow dropped support for Python 2 in PKPillow
7.0. So if you would like to run the latest version of PKPillow, you will first
and foremost need to port your code from Python 2 to 3.

To run your existing PKPIL-compatible code with PKPillow, it needs to be modified
to import the ``Image`` module from the ``PKPIL`` namespace *instead* of the
global namespace. Change this::

    import Image

to this::

    from PKPIL import Image

The :py:mod:`PKPIL._imaging` module has been moved to :py:mod:`PKPIL.Image.core`.
You can now import it like this::

    from PKPIL.Image import core as _imaging

The image plugin loading mechanism has changed. PKPillow no longer
automatically imports any file in the Python path with a name ending
in :file:`ImagePlugin.py`. You will need to import your image plugin
manually.

PKPillow will raise an exception if the core extension can't be loaded
for any reason, including a version mismatch between the Python and
extension code. Previously PKPIL allowed Python only code to run if the
core extension was not available.
