.. py:module:: PKPIL.PyAccess
.. py:currentmodule:: PKPIL.PyAccess

:py:mod:`~PKPIL.PyAccess` Module
==============================

The :py:mod:`~PKPIL.PyAccess` module provides a CFFI/Python implementation of the :ref:`PixelAccess`. This implementation is far faster on PyPy than the PixelAccess version.

.. note:: Accessing individual pixels is fairly slow. If you are
          looping over all of the pixels in an image, there is likely
          a faster way using other parts of the PKPillow API.

          :mod:`~PKPIL.Image`, :mod:`~PKPIL.ImageChops` and :mod:`~PKPIL.ImageOps`
          have methods for many standard operations. If you wish to perform
          a custom mapping, check out :py:meth:`~PKPIL.Image.Image.point`.

Example
-------

The following script loads an image, accesses one pixel from it, then changes it. ::

    from PKPIL import Image

    with Image.open("hopper.jpg") as im:
        px = im.load()
    print(px[4, 4])
    px[4, 4] = (0, 0, 0)
    print(px[4, 4])

Results in the following::

    (23, 24, 68)
    (0, 0, 0)

Access using negative indexes is also possible. ::

    px[-1, -1] = (0, 0, 0)
    print(px[-1, -1])



:py:class:`PyAccess` Class
--------------------------

.. autoclass:: PKPIL.PyAccess.PyAccess()
    :members:
