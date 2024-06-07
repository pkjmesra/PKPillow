.. py:module:: PKPIL.ImageFilter
.. py:currentmodule:: PKPIL.ImageFilter

:py:mod:`~PKPIL.ImageFilter` Module
=================================

The :py:mod:`~PKPIL.ImageFilter` module contains definitions for a pre-defined set of
filters, which can be be used with the :py:meth:`Image.filter()
<PKPIL.Image.Image.filter>` method.

Example: Filter an image
------------------------

::

    from PKPIL import ImageFilter

    im1 = im.filter(ImageFilter.BLUR)

    im2 = im.filter(ImageFilter.MinFilter(3))
    im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)

Filters
-------

The current version of the library provides the following set of predefined
image enhancement filters:

* **BLUR**
* **CONTOUR**
* **DETAIL**
* **EDGE_ENHANCE**
* **EDGE_ENHANCE_MORE**
* **EMBOSS**
* **FIND_EDGES**
* **SHARPEN**
* **SMOOTH**
* **SMOOTH_MORE**

.. autoclass:: PKPIL.ImageFilter.Color3DLUT
    :members:

.. autoclass:: PKPIL.ImageFilter.BoxBlur
    :members:

.. autoclass:: PKPIL.ImageFilter.GaussianBlur
    :members:

.. autoclass:: PKPIL.ImageFilter.UnsharpMask
    :members:

.. autoclass:: PKPIL.ImageFilter.Kernel
    :members:

.. autoclass:: PKPIL.ImageFilter.RankFilter
    :members:

.. autoclass:: PKPIL.ImageFilter.MedianFilter
    :members:

.. autoclass:: PKPIL.ImageFilter.MinFilter
    :members:

.. autoclass:: PKPIL.ImageFilter.MaxFilter
    :members:

.. autoclass:: PKPIL.ImageFilter.ModeFilter
    :members:

.. class:: Filter

    An abstract mixin used for filtering images
    (for use with :py:meth:`~PKPIL.Image.Image.filter`).

    Implementors must provide the following method:

    .. method:: filter(self, image)

        Applies a filter to a single-band image, or a single band of an image.

        :returns: A filtered copy of the image.

.. class:: MultibandFilter

    An abstract mixin used for filtering multi-band images
    (for use with :py:meth:`~PKPIL.Image.Image.filter`).

    Implementors must provide the following method:

    .. method:: filter(self, image)

        Applies a filter to a multi-band image.

        :returns: A filtered copy of the image.
