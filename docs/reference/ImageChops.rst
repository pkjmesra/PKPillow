.. py:module:: PKPIL.ImageChops
.. py:currentmodule:: PKPIL.ImageChops

:py:mod:`~PKPIL.ImageChops` ("Channel Operations") Module
=======================================================

The :py:mod:`~PKPIL.ImageChops` module contains a number of arithmetical image
operations, called channel operations (“chops”). These can be used for various
purposes, including special effects, image compositions, algorithmic painting,
and more.

For more pre-made operations, see :py:mod:`~PKPIL.ImageOps`.

At this time, most channel operations are only implemented for 8-bit images
(e.g. “L” and “RGB”).

Functions
---------

Most channel operations take one or two image arguments and returns a new
image. Unless otherwise noted, the result of a channel operation is always
clipped to the range 0 to MAX (which is 255 for all modes supported by the
operations in this module).

.. autofunction:: PKPIL.ImageChops.add
.. autofunction:: PKPIL.ImageChops.add_modulo
.. autofunction:: PKPIL.ImageChops.blend
.. autofunction:: PKPIL.ImageChops.composite
.. autofunction:: PKPIL.ImageChops.constant
.. autofunction:: PKPIL.ImageChops.darker
.. autofunction:: PKPIL.ImageChops.difference
.. autofunction:: PKPIL.ImageChops.duplicate
.. autofunction:: PKPIL.ImageChops.invert
.. autofunction:: PKPIL.ImageChops.lighter
.. autofunction:: PKPIL.ImageChops.logical_and
.. autofunction:: PKPIL.ImageChops.logical_or
.. autofunction:: PKPIL.ImageChops.logical_xor
.. autofunction:: PKPIL.ImageChops.multiply
.. autofunction:: PKPIL.ImageChops.soft_light
.. autofunction:: PKPIL.ImageChops.hard_light
.. autofunction:: PKPIL.ImageChops.overlay
.. autofunction:: PKPIL.ImageChops.offset
.. autofunction:: PKPIL.ImageChops.screen
.. autofunction:: PKPIL.ImageChops.subtract
.. autofunction:: PKPIL.ImageChops.subtract_modulo
