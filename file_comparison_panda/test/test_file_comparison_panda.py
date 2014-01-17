import os
from unittest import TestCase
import pytest

from ..file_comparison_panda import FileComparisonPanda
from ..file_comparison_exceptions import (
    UnsupportedFileType, FileDoesNotExist, PermissionDeniedOnFile)


class TestFileComparison(TestCase):
    test_files_path = os.path.dirname(__file__)

    def test_constructor_with_invalid_file_types(self):
        """
        Prove the FileComparisonPanda.__init__() throws
        UnsupportFileType when passed a file paths that refers to
        a non-supported file types.

        """
        with pytest.raises(UnsupportedFileType):
            FileComparisonPanda(
                self.test_files_path + '/unsupported_file_1.usp',
                self.test_files_path + '/unsupported_file_2.usp')

    def test_constructor_with_inaccessible_file(self):
        """
        Prove the FileComparisonPanda.__init__() throws
        PermissionDeniedOnFile when passed a file path that refers
        to an inaccessible file.

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
        Prove the FileComparisonPanda.__init__() throws
        FileDoesNotExist when passed a file path that refers
        to a nonexistent file.
        """
        with pytest.raises(FileDoesNotExist):
            FileComparisonPanda(
                self.test_files_path + '/nonexistent_file_1.csv',
                self.test_files_path + '/new_file.csv')

    def test_matching_records_getter(self):
        file_comparison = FileComparisonPanda(
            self.test_files_path + '/new_file.csv',
            self.test_files_path + '/old_file.csv'
        )

        assert file_comparison.matching_records == [
            ('UserId', 'Last Name', 'First Name',
             'Email', 'Password', 'User Type', 'Internal ID'),
            ('mmouse', 'Mouse', 'Mickey',
             'mickey.mouse@disney.com', '', 'maintain', '')]

    def test_unique_records_getter(self):
        """
        Prove that FileComparisonPanda.unique_records property
        returns the unique records for file_one and file_two.

        """

        file_comparison = FileComparisonPanda(
            self.test_files_path + '/new_file.csv',
            self.test_files_path + '/old_file.csv'
        )

        assert file_comparison.unique_records['file_one'] == [
            ('dduck', 'Duck', 'Donald',
             'donald.duck@disney.com', '', 'registered', ''),
            ('mmouse1', 'Mouse', 'Minnie',
             'minnie.mouse@disney.com', '', 'registered', '')]

        assert file_comparison.unique_records['file_two'] == [
            ('goofy', 'Goofy', 'N/A',
             'goofy@disney.com', '', 'maintain', ''),
            ('dduck', 'Duck', 'Donald',
             'donald.duck@disney.com', '', 'maintain', '')]

    def test_switching_comparison_file(self):
        file_comparison = FileComparisonPanda(
            self.test_files_path + '/new_file.csv',
            self.test_files_path + '/old_file.csv'
        )

        file_comparison.file_two = self.test_files_path + '/test_file_three.csv'

