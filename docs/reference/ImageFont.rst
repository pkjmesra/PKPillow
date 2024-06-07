.. py:module:: PKPIL.ImageFont
.. py:currentmodule:: PKPIL.ImageFont

:py:mod:`~PKPIL.ImageFont` Module
===============================

The :py:mod:`~PKPIL.ImageFont` module defines a class with the same name. Instances of
this class store bitmap fonts, and are used with the
:py:meth:`PKPIL.ImageDraw.ImageDraw.text` method.

PKPIL uses its own font file format to store bitmap fonts, limited to 256 characters. You can use
`pilfont.py <https://github.com/python-pillow/pillow-scripts/blob/main/Scripts/pilfont.py>`_
from `pillow-scripts <https://pypi.org/project/pillow-scripts/>`_ to convert BDF and
PCF font descriptors (X window font formats) to this format.

Starting with version 1.1.4, PKPIL can be configured to support TrueType and
OpenType fonts (as well as other font formats supported by the FreeType
library). For earlier versions, TrueType support is only available as part of
the imToolkit package.

Example
-------

::

    from PKPIL import ImageFont, ImageDraw

    draw = ImageDraw.Draw(image)

    # use a bitmap font
    font = ImageFont.load("arial.pil")

    draw.text((10, 10), "hello", font=font)

    # use a truetype font
    font = ImageFont.truetype("arial.ttf", 15)

    draw.text((10, 25), "world", font=font)

Functions
---------

.. autofunction:: PKPIL.ImageFont.load
.. autofunction:: PKPIL.ImageFont.load_path
.. autofunction:: PKPIL.ImageFont.truetype
.. autofunction:: PKPIL.ImageFont.load_default

Methods
-------

.. autoclass:: PKPIL.ImageFont.ImageFont
    :members:

.. autoclass:: PKPIL.ImageFont.FreeTypeFont
    :members:

.. autoclass:: PKPIL.ImageFont.TransposedFont
    :members:
    :undoc-members:

Constants
---------

.. data:: PKPIL.ImageFont.Layout.BASIC

    Use basic text layout for TrueType font.
    Advanced features such as text direction are not supported.

.. data:: PKPIL.ImageFont.Layout.RAQM

    Use Raqm text layout for TrueType font.
    Advanced features are supported.

    Requires Raqm, you can check support using
    :py:func:`PKPIL.features.check_feature` with ``feature="raqm"``.
