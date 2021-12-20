# file __init__.py
import os
import os.path

from traitlets.config import Config
from nbconvert.exporters.html import HTMLExporter

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------

class TocExporter(HTMLExporter):
    """
    Custom exporter to link nbconvert to custom JS code for interactive
    table of contents (TOC)
    """

    # If this custom exporter should add an entry to the
    # "File -> Download as" menu in the notebook, give it a name here in the
    # `export_from_notebook` class member
    export_from_notebook = "HTML (w/ TOC)"

    def _file_extension_default(self):
        return '.html'

    @property
    def template_paths(self):
        """
        We want to inherit from HTML template, and have template under
        ``./templates/`` so append it to the search path. (see next section)

        Note: nbconvert 6.0 changed ``template_path`` to ``template_paths``
        """
        # return super().template_paths+[os.path.join(os.path.dirname(__file__), "templates")]
        return super()._template_paths() + [os.path.join(os.path.dirname(__file__), "templates")]

    def _template_file_default(self):
        """
        We want to use the new template we ship with our library.
        """
        return 'html_toc' # full