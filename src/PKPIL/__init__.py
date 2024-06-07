"""PKPillow (Fork of the Python Imaging Library)

PKPillow is the friendly PKPIL fork by Jeffrey A. Clark (Alex) and contributors.
    https://github.com/python-pillow/PKPillow/

PKPillow is forked from PKPIL 1.1.7.

PKPIL is the Python Imaging Library by Fredrik Lundh and contributors.
Copyright (c) 1999 by Secret Labs AB.

Use PKPIL.__version__ for this PKPillow version.

;-)
"""

from . import _version

# VERSION was removed in PKPillow 6.0.0.
# PKPILLOW_VERSION was removed in PKPillow 9.0.0.
# Use __version__ instead.
__version__ = _version.__version__
del _version


_plugins = [
    "BlpImagePlugin",
    "BmpImagePlugin",
    "BufrStubImagePlugin",
    "CurImagePlugin",
    "DcxImagePlugin",
    "DdsImagePlugin",
    "EpsImagePlugin",
    "FitsImagePlugin",
    "FitsStubImagePlugin",
    "FliImagePlugin",
    "FpxImagePlugin",
    "FtexImagePlugin",
    "GbrImagePlugin",
    "GifImagePlugin",
    "GribStubImagePlugin",
    "Hdf5StubImagePlugin",
    "IcnsImagePlugin",
    "IcoImagePlugin",
    "ImImagePlugin",
    "ImtImagePlugin",
    "IptcImagePlugin",
    "JpegImagePlugin",
    "Jpeg2KImagePlugin",
    "McIdasImagePlugin",
    "MicImagePlugin",
    "MpegImagePlugin",
    "MpoImagePlugin",
    "MspImagePlugin",
    "PalmImagePlugin",
    "PcdImagePlugin",
    "PcxImagePlugin",
    "PdfImagePlugin",
    "PixarImagePlugin",
    "PngImagePlugin",
    "PpmImagePlugin",
    "PsdImagePlugin",
    "QoiImagePlugin",
    "SgiImagePlugin",
    "SpiderImagePlugin",
    "SunImagePlugin",
    "TgaImagePlugin",
    "TiffImagePlugin",
    "WebPImagePlugin",
    "WmfImagePlugin",
    "XbmImagePlugin",
    "XpmImagePlugin",
    "XVThumbImagePlugin",
]


class UnidentifiedImageError(OSError):
    """
    Raised in :py:meth:`PKPIL.Image.open` if an image cannot be opened and identified.

    If a PNG image raises this error, setting :data:`.ImageFile.LOAD_TRUNCATED_IMAGES`
    to true may allow the image to be opened after all. The setting will ignore missing
    data and checksum failures.
    """

    pass
