.. py:module:: PKPIL.ImageQt
.. py:currentmodule:: PKPIL.ImageQt

:py:mod:`~PKPIL.ImageQt` Module
=============================

The :py:mod:`~PKPIL.ImageQt` module contains support for creating PyQt6, PySide6, PyQt5
or PySide2 QImage objects from PKPIL images.

`Qt 5 reached end-of-life <https://www.qt.io/blog/qt-5.15-released>`_ on 2020-12-08 for
open-source users (and will reach EOL on 2023-12-08 for commercial licence holders).

Support for PyQt5 and PySide2 has been deprecated from ``ImageQt`` and will be removed
in PKPillow 10 (2023-07-01). Upgrade to
`PyQt6 <https://www.riverbankcomputing.com/static/Docs/PyQt6/>`_ or
`PySide6 <https://doc.qt.io/qtforpython/>`_ instead.

.. versionadded:: 1.1.6

.. py:class:: ImageQt(image)

    Creates an :py:class:`~PKPIL.ImageQt.ImageQt` object from a PKPIL
    :py:class:`~PKPIL.Image.Image` object. This class is a subclass of
    QtGui.QImage, which means that you can pass the resulting objects directly
    to PyQt6/PySide6/PyQt5/PySide2 API functions and methods.

    This operation is currently supported for mode 1, L, P, RGB, and RGBA
    images. To handle other modes, you need to convert the image first.
