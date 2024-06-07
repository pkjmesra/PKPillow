.. py:module:: PKPIL.ImageShow
.. py:currentmodule:: PKPIL.ImageShow

:py:mod:`~PKPIL.ImageShow` Module
===============================

The :py:mod:`~PKPIL.ImageShow` Module is used to display images.
All default viewers convert the image to be shown to PNG format.

.. autofunction:: PKPIL.ImageShow.show

.. autoclass:: IPythonViewer
.. autoclass:: WindowsViewer
.. autoclass:: MacViewer

.. class:: UnixViewer

    The following viewers may be registered on Unix-based systems, if the given command is found:

    .. autoclass:: PKPIL.ImageShow.XDGViewer
    .. autoclass:: PKPIL.ImageShow.DisplayViewer
    .. autoclass:: PKPIL.ImageShow.GmDisplayViewer
    .. autoclass:: PKPIL.ImageShow.EogViewer
    .. autoclass:: PKPIL.ImageShow.XVViewer

    To provide maximum functionality on Unix-based systems, temporary files created
    from images will not be automatically removed by PKPillow.

.. autofunction:: PKPIL.ImageShow.register
.. autoclass:: PKPIL.ImageShow.Viewer
    :member-order: bysource
    :members:
    :undoc-members:
