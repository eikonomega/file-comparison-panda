"""
**file-comparison-panda provides easy comparisons of csv file contents.**

Usage
-----
**Assuming you have the following three files:**

test_file_one.csv::

    "UserId","Last Name","First Name","Email","Password","User Type","Internal ID"
    "dduck","Duck","Donald","donald.duck@disney.com","","registered",""
    "mmouse1","Mouse","Minnie","minnie.mouse@disney.com","","registered",""
    "mmouse","Mouse","Mickey","mickey.mouse@disney.com","","maintain",""

test_file_two.csv::

    "UserId","Last Name","First Name","Email","Password","User Type","Internal ID"
    "mmouse","Mouse","Mickey","mickey.mouse@disney.com","","maintain",""
    "goofy","Goofy","N/A","goofy@disney.com","","maintain",""
    "dduck","Duck","Donald","donald.duck@disney.com","","maintain",""

test_file_three.csv::

    "UserId","Last Name","First Name","Email","Password","User Type","Internal ID"
    "dduck","Duck","Donald","donald.duck@disney.com","","registered",""
    "iman","Man","Iron","ironman@disney.com","","maintain",""
    "camerica","America","Captain","captain.america@disney.com","","maintain",""

**You could compare the files like so: **

>>> file_comparison_panda = FileComparisonPanda(
        '/path/to/test_file_one.csv', '/path/to/test_file_two.csv')
>>> file_comparison_panda.matching_records
[
    ('UserId', 'Last Name', 'First Name', 'Email', 'Password', 'User Type', 'Internal ID'),
    ('mmouse', 'Mouse', 'Mickey', 'mickey.mouse@disney.com', '', 'maintain', '')
]
>>> file_comparison_panda.unique_records
{
    'file_two': [
        ('goofy', 'Goofy', 'N/A', 'goofy@disney.com', '', 'maintain', ''),
        ('dduck', 'Duck', 'Donald', 'donald.duck@disney.com', '', 'maintain', '')
    ],
    'file_one': [
        ('dduck', 'Duck', 'Donald', 'donald.duck@disney.com', '', 'registered', ''),
        ('mmouse1', 'Mouse', 'Minnie', 'minnie.mouse@disney.com', '', 'registered', '')
    ]
}
>>> file_comparison_panda.file_one = '/path/to/test_file_three.csv'
>>> file_comparison_panda.matching_records
[
    ('dduck', 'Duck', 'Donald', 'donald.duck@disney.com', '', 'registered', ''),
    ('UserId', 'Last Name', 'First Name', 'Email', 'Password', 'User Type', 'Internal ID')
]
>>> file_comparison_panda.unique_records
{
    'file_two': [
        ('camerica', 'America', 'Captain', 'captain.america@disney.com', '', 'maintain', ''),
        ('iman', 'Man', 'Iron', 'ironman@disney.com', '', 'maintain', '')
    ],
    'file_one': [
        ('mmouse1', 'Mouse', 'Minnie', 'minnie.mouse@disney.com', '', 'registered', ''),
        ('mmouse', 'Mouse', 'Mickey', 'mickey.mouse@disney.com', '', 'maintain', '')
    ]
}


"""

from file_comparison_panda import FileComparisonPanda
from file_comparison_exceptions import (
    FileDoesNotExist, PermissionDeniedOnFile, UnsupportedFileType)

__version__ = '0.4.0'
