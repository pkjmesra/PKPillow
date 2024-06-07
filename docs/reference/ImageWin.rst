.. py:module:: PKPIL.ImageWin
.. py:currentmodule:: PKPIL.ImageWin

:py:mod:`~PKPIL.ImageWin` Module (Windows-only)
=============================================

The :py:mod:`~PKPIL.ImageWin` module contains support to create and display images on
Windows.

ImageWin can be used with PythonWin and other user interface toolkits that
provide access to Windows device contexts or window handles. For example,
Tkinter makes the window handle available via the winfo_id method::

    from PKPIL import ImageWin

    dib = ImageWin.Dib(...)

    hwnd = ImageWin.HWND(widget.winfo_id())
    dib.draw(hwnd, xy)


.. autoclass:: PKPIL.ImageWin.Dib
    :members:

.. autoclass:: PKPIL.ImageWin.HDC
    :members:

.. autoclass:: PKPIL.ImageWin.HWND
    :members:
