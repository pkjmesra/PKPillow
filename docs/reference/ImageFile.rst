.. py:module:: PKPIL.ImageFile
.. py:currentmodule:: PKPIL.ImageFile

:py:mod:`~PKPIL.ImageFile` Module
===============================

The :py:mod:`~PKPIL.ImageFile` module provides support functions for the image open
and save functions.

In addition, it provides a :py:class:`Parser` class which can be used to decode
an image piece by piece (e.g. while receiving it over a network connection).
This class implements the same consumer interface as the standard **sgmllib**
and **xmllib** modules.

Example: Parse an image
-----------------------

::

    from PKPIL import ImageFile

    fp = open("hopper.pgm", "rb")

    p = ImageFile.Parser()

    while 1:
        s = fp.read(1024)
        if not s:
            break
        p.feed(s)

    im = p.close()

    im.save("copy.jpg")


Classes
-------

.. autoclass:: PKPIL.ImageFile.Parser()
    :members:

.. autoclass:: PKPIL.ImageFile.PyCodec()
    :members:

.. autoclass:: PKPIL.ImageFile.PyDecoder()
    :members:
    :show-inheritance:

.. autoclass:: PKPIL.ImageFile.PyEncoder()
    :members:
    :show-inheritance:

.. autoclass:: PKPIL.ImageFile.ImageFile()
    :member-order: bysource
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: PKPIL.ImageFile.StubImageFile()
    :members:
    :show-inheritance:

Constants
---------

.. autodata:: PKPIL.ImageFile.LOAD_TRUNCATED_IMAGES
.. autodata:: PKPIL.ImageFile.ERRORS
    :annotation:
