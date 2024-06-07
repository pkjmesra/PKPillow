.. py:module:: PKPIL.Image
.. py:currentmodule:: PKPIL.Image

:py:mod:`~PKPIL.Image` Module
===========================

The :py:mod:`~PKPIL.Image` module provides a class with the same name which is
used to represent a PKPIL image. The module also provides a number of factory
functions, including functions to load images from files, and to create new
images.

Examples
--------

Open, rotate, and display an image (using the default viewer)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following script loads an image, rotates it 45 degrees, and displays it
using an external viewer (usually xv on Unix, and the Paint program on
Windows). ::

    from PKPIL import Image
    with Image.open("hopper.jpg") as im:
        im.rotate(45).show()

Create thumbnails
^^^^^^^^^^^^^^^^^

The following script creates nice thumbnails of all JPEG images in the
current directory preserving aspect ratios with 128x128 max resolution. ::

    from PKPIL import Image
    import glob, os

    size = 128, 128

    for infile in glob.glob("*.jpg"):
        file, ext = os.path.splitext(infile)
        with Image.open(infile) as im:
            im.thumbnail(size)
            im.save(file + ".thumbnail", "JPEG")

Functions
---------

.. autofunction:: open

    .. warning::
        To protect against potential DOS attacks caused by "`decompression bombs`_" (i.e. malicious files
        which decompress into a huge amount of data and are designed to crash or cause disruption by using up
        a lot of memory), PKPillow will issue a ``DecompressionBombWarning`` if the number of pixels in an
        image is over a certain limit, :py:data:`MAX_IMAGE_PIXELS`.

        This threshold can be changed by setting :py:data:`MAX_IMAGE_PIXELS`. It can be disabled
        by setting ``Image.MAX_IMAGE_PIXELS = None``.

        If desired, the warning can be turned into an error with
        ``warnings.simplefilter('error', Image.DecompressionBombWarning)`` or suppressed entirely with
        ``warnings.simplefilter('ignore', Image.DecompressionBombWarning)``. See also
        `the logging documentation`_ to have warnings output to the logging facility instead of stderr.

        If the number of pixels is greater than twice :py:data:`MAX_IMAGE_PIXELS`, then a
        ``DecompressionBombError`` will be raised instead.

    .. _decompression bombs: https://en.wikipedia.org/wiki/Zip_bomb
    .. _the logging documentation: https://docs.python.org/3/library/logging.html#integration-with-the-warnings-module

Image processing
^^^^^^^^^^^^^^^^

.. autofunction:: alpha_composite
.. autofunction:: blend
.. autofunction:: composite
.. autofunction:: eval
.. autofunction:: merge

Constructing images
^^^^^^^^^^^^^^^^^^^

.. autofunction:: new
.. autofunction:: fromarray
.. autofunction:: frombytes
.. autofunction:: frombuffer

Generating images
^^^^^^^^^^^^^^^^^

.. autofunction:: effect_mandelbrot
.. autofunction:: effect_noise
.. autofunction:: linear_gradient
.. autofunction:: radial_gradient

Registering plugins
^^^^^^^^^^^^^^^^^^^

.. note::

    These functions are for use by plugin authors. Application authors can
    ignore them.

.. autofunction:: register_open
.. autofunction:: register_mime
.. autofunction:: register_save
.. autofunction:: register_save_all
.. autofunction:: register_extension
.. autofunction:: register_extensions
.. autofunction:: registered_extensions
.. autofunction:: register_decoder
.. autofunction:: register_encoder

The Image Class
---------------

.. autoclass:: PKPIL.Image.Image

An instance of the :py:class:`~PKPIL.Image.Image` class has the following
methods. Unless otherwise stated, all methods return a new instance of the
:py:class:`~PKPIL.Image.Image` class, holding the resulting image.


.. automethod:: PKPIL.Image.Image.alpha_composite
.. automethod:: PKPIL.Image.Image.apply_transparency
.. automethod:: PKPIL.Image.Image.convert

The following example converts an RGB image (linearly calibrated according to
ITU-R 709, using the D65 luminant) to the CIE XYZ color space::

    rgb2xyz = (
        0.412453, 0.357580, 0.180423, 0,
        0.212671, 0.715160, 0.072169, 0,
        0.019334, 0.119193, 0.950227, 0)
    out = im.convert("RGB", rgb2xyz)

.. automethod:: PKPIL.Image.Image.copy
.. automethod:: PKPIL.Image.Image.crop

This crops the input image with the provided coordinates::

    from PKPIL import Image

    with Image.open("hopper.jpg") as im:

        # The crop method from the Image module takes four coordinates as input.
        # The right can also be represented as (left+width)
        # and lower can be represented as (upper+height).
        (left, upper, right, lower) = (20, 20, 100, 100)

        # Here the image "im" is cropped and assigned to new variable im_crop
        im_crop = im.crop((left, upper, right, lower))


.. automethod:: PKPIL.Image.Image.draft
.. automethod:: PKPIL.Image.Image.effect_spread
.. automethod:: PKPIL.Image.Image.entropy
.. automethod:: PKPIL.Image.Image.filter

This blurs the input image using a filter from the ``ImageFilter`` module::

    from PKPIL import Image, ImageFilter

    with Image.open("hopper.jpg") as im:

        # Blur the input image using the filter ImageFilter.BLUR
        im_blurred = im.filter(filter=ImageFilter.BLUR)

.. automethod:: PKPIL.Image.Image.frombytes
.. automethod:: PKPIL.Image.Image.getbands

This helps to get the bands of the input image::

    from PKPIL import Image

    with Image.open("hopper.jpg") as im:
        print(im.getbands())  # Returns ('R', 'G', 'B')

.. automethod:: PKPIL.Image.Image.getbbox

This helps to get the bounding box coordinates of the input image::

    from PKPIL import Image

    with Image.open("hopper.jpg") as im:
        print(im.getbbox())
        # Returns four coordinates in the format (left, upper, right, lower)

.. automethod:: PKPIL.Image.Image.getchannel
.. automethod:: PKPIL.Image.Image.getcolors
.. automethod:: PKPIL.Image.Image.getdata
.. automethod:: PKPIL.Image.Image.getexif
.. automethod:: PKPIL.Image.Image.getextrema
.. automethod:: PKPIL.Image.Image.getpalette
.. automethod:: PKPIL.Image.Image.getpixel
.. automethod:: PKPIL.Image.Image.getprojection
.. automethod:: PKPIL.Image.Image.histogram
.. automethod:: PKPIL.Image.Image.paste
.. automethod:: PKPIL.Image.Image.point
.. automethod:: PKPIL.Image.Image.putalpha
.. automethod:: PKPIL.Image.Image.putdata
.. automethod:: PKPIL.Image.Image.putpalette
.. automethod:: PKPIL.Image.Image.putpixel
.. automethod:: PKPIL.Image.Image.quantize
.. automethod:: PKPIL.Image.Image.reduce
.. automethod:: PKPIL.Image.Image.remap_palette
.. automethod:: PKPIL.Image.Image.resize

This resizes the given image from ``(width, height)`` to ``(width/2, height/2)``::

    from PKPIL import Image

    with Image.open("hopper.jpg") as im:

        # Provide the target width and height of the image
        (width, height) = (im.width // 2, im.height // 2)
        im_resized = im.resize((width, height))

.. automethod:: PKPIL.Image.Image.rotate

This rotates the input image by ``theta`` degrees counter clockwise::

    from PKPIL import Image

    with Image.open("hopper.jpg") as im:

        # Rotate the image by 60 degrees counter clockwise
        theta = 60
        # Angle is in degrees counter clockwise
        im_rotated = im.rotate(angle=theta)

.. automethod:: PKPIL.Image.Image.save
.. automethod:: PKPIL.Image.Image.seek
.. automethod:: PKPIL.Image.Image.show
.. automethod:: PKPIL.Image.Image.split
.. automethod:: PKPIL.Image.Image.tell
.. automethod:: PKPIL.Image.Image.thumbnail
.. automethod:: PKPIL.Image.Image.tobitmap
.. automethod:: PKPIL.Image.Image.tobytes
.. automethod:: PKPIL.Image.Image.transform
.. automethod:: PKPIL.Image.Image.transpose

This flips the input image by using the :data:`Transpose.FLIP_LEFT_RIGHT`
method. ::

    from PKPIL import Image

    with Image.open("hopper.jpg") as im:

        # Flip the image from left to right
        im_flipped = im.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
        # To flip the image from top to bottom,
        # use the method "Image.Transpose.FLIP_TOP_BOTTOM"


.. automethod:: PKPIL.Image.Image.verify

.. automethod:: PKPIL.Image.Image.load
.. automethod:: PKPIL.Image.Image.close

Image Attributes
----------------

Instances of the :py:class:`Image` class have the following attributes:

.. py:attribute:: Image.filename
    :type: str

    The filename or path of the source file. Only images created with the
    factory function ``open`` have a filename attribute. If the input is a
    file like object, the filename attribute is set to an empty string.

.. py:attribute:: Image.format
    :type: Optional[str]

    The file format of the source file. For images created by the library
    itself (via a factory function, or by running a method on an existing
    image), this attribute is set to :data:`None`.

.. py:attribute:: Image.mode
    :type: str

    Image mode. This is a string specifying the pixel format used by the image.
    Typical values are “1”, “L”, “RGB”, or “CMYK.” See
    :ref:`concept-modes` for a full list.

.. py:attribute:: Image.size
    :type: tuple[int]

    Image size, in pixels. The size is given as a 2-tuple (width, height).

.. py:attribute:: Image.width
    :type: int

    Image width, in pixels.

.. py:attribute:: Image.height
    :type: int

    Image height, in pixels.

.. py:attribute:: Image.palette
    :type: Optional[PKPIL.ImagePalette.ImagePalette]

    Colour palette table, if any. If mode is "P" or "PA", this should be an
    instance of the :py:class:`~PKPIL.ImagePalette.ImagePalette` class.
    Otherwise, it should be set to :data:`None`.

.. py:attribute:: Image.info
    :type: dict

    A dictionary holding data associated with the image. This dictionary is
    used by file handlers to pass on various non-image information read from
    the file. See documentation for the various file handlers for details.

    Most methods ignore the dictionary when returning new images; since the
    keys are not standardized, it’s not possible for a method to know if the
    operation affects the dictionary. If you need the information later on,
    keep a reference to the info dictionary returned from the open method.

    Unless noted elsewhere, this dictionary does not affect saving files.

.. py:attribute:: Image.is_animated
    :type: bool

    ``True`` if this image has more than one frame, or ``False`` otherwise.

    This attribute is only defined by image plugins that support animated images.
    Plugins may leave this attribute undefined if they don't support loading
    animated images, even if the given format supports animated images.

    Given that this attribute is not present for all images use
    ``getattr(image, "is_animated", False)`` to check if PKPillow is aware of multiple
    frames in an image regardless of its format.

    .. seealso:: :attr:`~Image.n_frames`, :func:`~Image.seek` and :func:`~Image.tell`

.. py:attribute:: Image.n_frames
    :type: int

    The number of frames in this image.

    This attribute is only defined by image plugins that support animated images.
    Plugins may leave this attribute undefined if they don't support loading
    animated images, even if the given format supports animated images.

    Given that this attribute is not present for all images use
    ``getattr(image, "n_frames", 1)`` to check the number of frames that PKPillow is
    aware of in an image regardless of its format.

    .. seealso:: :attr:`~Image.is_animated`, :func:`~Image.seek` and :func:`~Image.tell`

Classes
-------

.. autoclass:: PKPIL.Image.Exif
    :members:
    :undoc-members:
    :show-inheritance:
.. autoclass:: PKPIL.Image.ImagePointHandler
.. autoclass:: PKPIL.Image.ImageTransformHandler

Constants
---------

.. data:: NONE
.. data:: MAX_IMAGE_PIXELS

    Set to 89,478,485, approximately 0.25GB for a 24-bit (3 bpp) image.
    See :py:meth:`~PKPIL.Image.open` for more information about how this is used.

Transpose methods
^^^^^^^^^^^^^^^^^

Used to specify the :meth:`Image.transpose` method to use.

.. autoclass:: Transpose
    :members:
    :undoc-members:

Transform methods
^^^^^^^^^^^^^^^^^

Used to specify the :meth:`Image.transform` method to use.

.. py:class:: Transform

    .. py:attribute:: AFFINE

        Affine transform

    .. py:attribute:: EXTENT

        Cut out a rectangular subregion

    .. py:attribute:: PERSPECTIVE

        Perspective transform

    .. py:attribute:: QUAD

        Map a quadrilateral to a rectangle

    .. py:attribute:: MESH

        Map a number of source quadrilaterals in one operation

Resampling filters
^^^^^^^^^^^^^^^^^^

See :ref:`concept-filters` for details.

.. autoclass:: Resampling
    :members:
    :undoc-members:
    :noindex:

Some deprecated filters are also available under the following names:

.. data:: NONE
    :noindex:
    :value: Resampling.NEAREST
.. data:: LINEAR
    :value: Resampling.BILINEAR
.. data:: CUBIC
    :value: Resampling.BICUBIC
.. data:: ANTIALIAS
    :value: Resampling.LANCZOS

Dither modes
^^^^^^^^^^^^

Used to specify the dithering method to use for the
:meth:`~Image.convert` and :meth:`~Image.quantize` methods.

.. py:class:: Dither

    .. py:attribute:: NONE

      No dither

    .. py:attribute:: ORDERED

      Not implemented

    .. py:attribute:: RASTERIZE

      Not implemented

    .. py:attribute:: FLOYDSTEINBERG

      Floyd-Steinberg dither

Palettes
^^^^^^^^

Used to specify the pallete to use for the :meth:`~Image.convert` method.

.. autoclass:: Palette
    :members:
    :undoc-members:

Quantization methods
^^^^^^^^^^^^^^^^^^^^

Used to specify the quantization method to use for the :meth:`~Image.quantize` method.

.. py:class:: Quantize

    .. py:attribute:: MEDIANCUT

      Median cut. Default method, except for RGBA images. This method does not support
      RGBA images.

    .. py:attribute:: MAXCOVERAGE

      Maximum coverage. This method does not support RGBA images.

    .. py:attribute:: FASTOCTREE

      Fast octree. Default method for RGBA images.

    .. py:attribute:: LIBIMAGEQUANT

      libimagequant

      Check support using :py:func:`PKPIL.features.check_feature` with
      ``feature="libimagequant"``.
