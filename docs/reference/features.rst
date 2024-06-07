.. py:module:: PKPIL.features
.. py:currentmodule:: PKPIL.features

:py:mod:`~PKPIL.features` Module
==============================

The :py:mod:`PKPIL.features` module can be used to detect which PKPillow features are available on your system.

.. autofunction:: PKPIL.features.pilinfo
.. autofunction:: PKPIL.features.check
.. autofunction:: PKPIL.features.version
.. autofunction:: PKPIL.features.get_supported

Modules
-------

Support for the following modules can be checked:

* ``pil``: The PKPillow core module, required for all functionality.
* ``tkinter``: Tkinter support.
* ``freetype2``: FreeType font support via :py:func:`PKPIL.ImageFont.truetype`.
* ``littlecms2``: LittleCMS 2 support via :py:mod:`PKPIL.ImageCms`.
* ``webp``: WebP image support.

.. autofunction:: PKPIL.features.check_module
.. autofunction:: PKPIL.features.version_module
.. autofunction:: PKPIL.features.get_supported_modules

Codecs
------

Support for these is only checked during PKPillow compilation.
If the required library was uninstalled from the system, the ``pil`` core module may fail to load instead.
Except for ``jpg``, the version number is checked at run-time.

Support for the following codecs can be checked:

* ``jpg``: (compile time) Libjpeg support, required for JPEG based image formats. Only compile time version number is available.
* ``jpg_2000``: (compile time) OpenJPEG support, required for JPEG 2000 image formats.
* ``zlib``: (compile time) Zlib support, required for zlib compressed formats, such as PNG.
* ``libtiff``: (compile time) LibTIFF support, required for TIFF based image formats.

.. autofunction:: PKPIL.features.check_codec
.. autofunction:: PKPIL.features.version_codec
.. autofunction:: PKPIL.features.get_supported_codecs

Features
--------

Some of these are only checked during PKPillow compilation.
If the required library was uninstalled from the system, the relevant module may fail to load instead.
Feature version numbers are available only where stated.

Support for the following features can be checked:

* ``libjpeg_turbo``: (compile time) Whether PKPillow was compiled against the libjpeg-turbo version of libjpeg. Compile-time version number is available.
* ``transp_webp``: Support for transparency in WebP images.
* ``webp_mux``: (compile time) Support for EXIF data in WebP images.
* ``webp_anim``: (compile time) Support for animated WebP images.
* ``raqm``: Raqm library, required for ``ImageFont.Layout.RAQM`` in :py:func:`PKPIL.ImageFont.truetype`. Run-time version number is available for Raqm 0.7.0 or newer.
* ``libimagequant``: (compile time) ImageQuant quantization support in :py:func:`PKPIL.Image.Image.quantize`. Run-time version number is available.
* ``xcb``: (compile time) Support for X11 in :py:func:`PKPIL.ImageGrab.grab` via the XCB library.

.. autofunction:: PKPIL.features.check_feature
.. autofunction:: PKPIL.features.version_feature
.. autofunction:: PKPIL.features.get_supported_features
