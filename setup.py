"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-13 17:20:35
 * @modify date 2020-08-13 17:26:18
 * @desc [
    Setup for AlexaUtils PyPi
 ]
 */
"""

##########
# Imports
##########

from setuptools import setup, find_packages


##########
# Setup variabless
##########

name = "pywrangle"
version = "0.3.03"
description = "Auxiliary functions to clean pandas data frames"
author = "Jai Miles"
author_email = "jaimiles23@gmail.com"
keywords = ['clean', 'wrangle', 'pandas', 'dataframe', 'mangle', 'data', 'numpy', 'text', 'missing']
url = 'https://github.com/jaimiles23/pywrangle'
download_url = ''


##########
# Read files
##########

with open('README.md') as readme_file:
    README = readme_file.read()

try:
    with open('HISTORY.md') as history_file:
        HISTORY = history_file.read()
        
except FileNotFoundError:
    print("HISTORY.md not found.")
    HISTORY = "---"


##########
# SetUp args
##########

setup_args = dict(
    name = name,
    version = version,
    description = description,
    long_description_content_type = "text/markdown",
    long_description = README + '\n\n' + HISTORY,
    license = 'MIT',
    packages = find_packages(),
    author = author,
    author_email = author_email,
    keywords = keywords,
    url = url,
    download_url = download_url,
    python_requires='>=3.6',
)


##########
# Requirements
##########

install_requires = [
    'pandas >= 1.0.3',
    'numpy >= 1.14.4',
    'fuzzywuzzy == 0.18.0',
    'python-levenshtein == 0.12.0',
    'metaphone == 0.6'
]


##########
# Setup
##########

if __name__ == '__main__':
    setup(**setup_args, install_requires = install_requires)