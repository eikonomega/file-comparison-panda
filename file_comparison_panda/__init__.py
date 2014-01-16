"""
**ZenFileComparison provides easy comparisons of file contents.**

Usage
-----
Assuming you have two files, test_file_one.csv & test_file_two.csv with
the following content:

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


>>> my_file_comparison = FileComparisonPanda(
        '/path/to/test_file_one.csv', '/path/to/test_file_two.csv')
>>> my_file_comparison.compare_files()
>>> my_file_comparison.matching_records
[
    ('UserId', 'Last Name', 'First Name', 'Email', 'Password', 'User Type', 'Internal ID'),
    ('mmouse', 'Mouse', 'Mickey', 'mickey.mouse@disney.com', '', 'maintain', '')
]

>>> my_file_comparison.unique_records
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

"""

from file_comparison_panda import FileComparisonPanda

__version__ = '0.1.0'