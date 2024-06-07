.. py:module:: PKPIL.ImageSequence
.. py:currentmodule:: PKPIL.ImageSequence

:py:mod:`~PKPIL.ImageSequence` Module
===================================

The :py:mod:`~PKPIL.ImageSequence` module contains a wrapper class that lets you
iterate over the frames of an image sequence.

Extracting frames from an animation
-----------------------------------

::

    from PKPIL import Image, ImageSequence

    with Image.open("animation.fli") as im:
        index = 1
        for frame in ImageSequence.Iterator(im):
            frame.save(f"frame{index}.png")
            index += 1

The :py:class:`~PKPIL.ImageSequence.Iterator` class
-------------------------------------------------

.. autoclass:: PKPIL.ImageSequence.Iterator
    :members:

Functions
---------

.. autofunction:: PKPIL.ImageSequence.all_frames
