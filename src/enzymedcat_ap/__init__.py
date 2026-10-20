"""EnzymeDCAT-AP.

This is an extension of the DCAT-AP Plus LinkML schema to provide biocatalytic specific metadata for a dataset.
"""

try:
    from enzymedcat_ap._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
