"""
The file_comparison module exists to easily compare the contents of two
files.  The functionality of this module is currently limited to CSV files.

"""

import csv

from file_comparison_exceptions import (
    UnsupportedFileType, FileDoesNotExist, PermissionDeniedOnFile)


SUPPORTED_FILE_TYPES = ['csv']


class FileComparisonPanda(object):
    """
    Compares the data in two files and provides matching and unique
    records.

    """

    def __init__(
            self, file_path_1, file_path_2):
        """
        Verify that constructor arguments are actually files and
        of supported types.  Perform routine object
        initialization tasks.

        Args:
            file_path_1 (str): Filepath of first file for comparison.
            file_path_2 (str): Filepath of second file for comparison.

        Raises:
            IOError: When one of the files identified by the parameters
                doesn't exist or is inaccessible.

            NotImplementedError: When one of the files being compared has
                a non-supported file extension.

        """
        self._unique_records = dict()
        self._matching_records = list()

        self.file_one = file_path_1
        self.file_two = file_path_2

    @property
    def file_one(self):
        return self._file_one

    @file_one.setter
    def file_one(self, file_path):
        FileComparisonPanda._verify_acceptable_file_extensions(
                [file_path], SUPPORTED_FILE_TYPES)
        self._file_one = FileComparisonPanda._file(file_path)
        self._reset_file_comparison_data()

    @property
    def file_two(self):
        return self._file_two

    @file_two.setter
    def file_two(self, file_path):
        FileComparisonPanda._verify_acceptable_file_extensions(
                [file_path], SUPPORTED_FILE_TYPES)
        self._file_two = FileComparisonPanda._file(file_path)
        self._reset_file_comparison_data()

    @staticmethod
    def _verify_acceptable_file_extensions(
            list_of_filenames, list_of_extensions):
        """
        Determine if every file in list_of_files has one of the extensions
        in list_of_extensions.  If so, return True.  Otherwise, return False.

        Caller is responsible to provide valid filenames.

        """
        for filename in list_of_filenames:
            filename_parts = filename.partition('.')

            if filename_parts[2] not in list_of_extensions:
                raise UnsupportedFileType(
                    "One of the file paths provided to FileComparisonPanda() "
                    "references an unsupported file type.  The following "
                    "file types are supported: {}".format(SUPPORTED_FILE_TYPES))

    @staticmethod
    def _file(file_path):
        try:
            open_file = open(file_path, 'rU')
        except IOError as error:
            if error.errno == 2:
                raise FileDoesNotExist(
                    "One of the file paths provided to FileComparisonPanda() "
                    "is invalid.  Verify that '{}' exists".format(
                        error.filename))
            elif error.errno == 13:
                raise PermissionDeniedOnFile(
                    "One of the file paths provided to FileComparisonPanda() "
                    "is not accessible.  Verify that '{}' is readable "
                    "by the user running the program".format(
                        error.filename))
            raise
        else:
            return open_file

    def _reset_file_comparison_data(self):
        self._unique_records = dict()
        self._matching_records = list()

    def _compare_files(self):
        """
        Identify unique and matching records from self._file_one and
        self.file_two using various set operations.

        """

        file_one_records = set(
            FileComparisonPanda._load_file_into_memory(self._file_one))
        file_two_records = set(
            FileComparisonPanda._load_file_into_memory(self._file_two))

        self._matching_records.extend(
            file_one_records.intersection(file_two_records))

        self._unique_records['file_one'] = list(
            file_one_records.difference(file_two_records))

        self._unique_records['file_two'] = list(
            file_two_records.difference(file_one_records))

    @staticmethod
    def _load_file_into_memory(file_object):
        """
        Load the contents of a CSV file into memory for faster
        performance.

        IMPORTANT: This creates the potential for the program
        to bomb out when it encounters memory limits.

        """
        csv_reader = csv.reader(file_object)
        records = [tuple(record) for record in csv_reader]
        return records

    @property
    def unique_records(self):
        """
        Returns:
            A dict containing two elements ['_file_one', 'file_two'] each of
            which are lists of unique records found during _compare_files().

        Raises:
            AttributeError: When the method is called prior to _compare_files().

        """
        if not self._unique_records:
            self._compare_files()
        return self._unique_records

    @property
    def matching_records(self):
        """
        A list of records that were found in both files.

        """
        if not self._matching_records:
            self._compare_files()
        return self._matching_records