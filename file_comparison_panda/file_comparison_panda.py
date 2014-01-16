"""
The file_comparison module exists to easily compare the contents of two
files.  The functionality of this module is currently limited to CSV files.

"""

import csv

from file_comparison_exceptions import UnsupportedFileType, FileDoesNotExist, PermissionDeniedOnFile


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

        try:
            self._file_one = open(file_path_1, 'rU')
            self._file_two = open(file_path_2, 'rU')
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

        if not self._verify_acceptable_file_extensions(
                [file_path_1, file_path_2], ['csv']):
            raise UnsupportedFileType

    def unique_records(self):
        """
        Returns:
            A dict containing two elements ['_file_one', '_file_two'] each of
            which are lists of unique records found during compare_files().

        Raises:
            AttributeError: When the method is called prior to compare_files().

        """
        if set(self._unique_records.keys()).difference(
                ['file_one', 'file_two']):
            raise AttributeError(
                "The internal structure of self._matching_results is "
                "not correct.  Run compare_files() first.")
        return self._unique_records

    def matching_records(self):
        """
        A list of records that were found in both files.

        """
        return self._matching_records

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

            if filename_parts[2] in list_of_extensions:
                return True
            else:
                return False

    def compare_files(self):
        """
        Identify unique and matching records from self._file_one and
        self._file_two using various set operations.

        """

        # Obtain in-memory lists of file contents.
        file_one_records = set(self._load_file_into_memory(self._file_one))
        file_two_records = set(self._load_file_into_memory(self._file_two))

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