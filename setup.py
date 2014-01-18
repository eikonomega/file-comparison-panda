from setuptools import setup, find_packages

import file_comparison_panda

with open('requirements.txt') as requirements_doc:
    requirements = requirements_doc.read()

setup(
    name="file-comparison-panda",
    packages=find_packages(),
    version=file_comparison_panda.__version__,
    author="Mike Dunn",
    author_email="mike@eikonomega.com",
    url="https://github.com/eikonomega/file-comparison-panda",
    description="The file-comparison-panda library provides easy "
                "comparisons of csv file contents.",
    long_description=file_comparison_panda.__doc__,

    install_requires=requirements,
    #include_package_data=True,
    package_data={
        '': ['requirements.txt']
    }
)
