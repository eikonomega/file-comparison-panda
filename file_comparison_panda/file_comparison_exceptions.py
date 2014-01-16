"""
Custom exceptions for file_comparison_panda module.

"""


class FileComparisonPandaError(Exception):
    """
    Base exception class for FileComparisonPandaError Errors.
    """
    pass


class UnsupportedFileType(FileComparisonPandaError):
    """
    Error to raise when an attempt is made to operate on
    an unsupported file-type.

    """
    pass