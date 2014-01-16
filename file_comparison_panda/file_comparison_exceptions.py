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


class FileDoesNotExist(FileComparisonPandaError):
    """
    Error to raise when an attempt is made to operate on
    a nonexistent file.

    """
    pass


class PermissionDeniedOnFile(FileComparisonPandaError):
    """
    Error to raise when an attempt is made to operate on
    an file user doesn't have access to.

    """
    pass