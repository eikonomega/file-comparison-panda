import os
from unittest import TestCase
import pytest

from ..file_comparison_panda import FileComparisonPanda
from ..file_comparison_exceptions import (
    UnsupportedFileType, FileDoesNotExist, PermissionDeniedOnFile)


class TestFileComparison(TestCase):
    def setUp(self):
        self.test_files_path = os.path.dirname(__file__)

    def test_constructor_with_invalid_file_types(self):
        """
        Prove the FileComparisonPanda().__init__() throws a NotImplementedError
        exception when passed file paths that refer to non-supported
        file types.

        """
        with pytest.raises(UnsupportedFileType):
            FileComparisonPanda(
                self.test_files_path + '/unsupported_file_1.usp',
                self.test_files_path + '/unsupported_file_2.usp')

    def test_constructor_with_inaccessible_file(self):
        """
        Prove the FileComparisonPanda().__init__() throws an OSError
        exception when passed file paths that refer to inaccessible
        or non-existent files.

        """
        os.chmod(
            self.test_files_path + '/inaccessible_file_1.csv', int('000', 8))

        with pytest.raises(PermissionDeniedOnFile):
            FileComparisonPanda(
                self.test_files_path + '/inaccessible_file_1.csv',
                self.test_files_path + '/new_file.csv')

        os.chmod(
            self.test_files_path + '/inaccessible_file_1.csv', int('777', 8))

    def test_constructor_with_nonexistent_file(self):
        """
        Prove the FileComparisonPanda().__init__() throws IOError
        when given a path pointing to a non-existent file.
        """
        with pytest.raises(FileDoesNotExist):
            FileComparisonPanda(
                self.test_files_path + '/nonexistent_file_1.csv',
                self.test_files_path + '/new_file.csv')

    def test_compare_files(self):

        file_comparison = FileComparisonPanda(
            self.test_files_path + '/new_file.csv',
            self.test_files_path + '/old_file.csv'
        )

        self.assertListEqual(
            [
                ('dduck', 'Duck', 'Donald',
                 'donald.duck@disney.com', '', 'registered', ''),
                ('mmouse1', 'Mouse', 'Minnie',
                 'minnie.mouse@disney.com', '', 'registered', '')
            ],
            file_comparison.unique_records['file_one']
        )

        self.assertListEqual(
            [
                ('goofy', 'Goofy', 'N/A',
                 'goofy@disney.com', '', 'maintain', ''),
                ('dduck', 'Duck', 'Donald',
                 'donald.duck@disney.com', '', 'maintain', ''),
            ],
            file_comparison.unique_records['file_two']
        )

        self.assertListEqual(
            [
                ('UserId', 'Last Name', 'First Name',
                 'Email', 'Password', 'User Type', 'Internal ID'),
                ('mmouse', 'Mouse', 'Mickey',
                 'mickey.mouse@disney.com', '', 'maintain', '')
            ],
            file_comparison.matching_records
        )
