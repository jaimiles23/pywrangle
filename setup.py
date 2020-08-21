"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-13 17:20:35
 * @modify date 2020-08-13 17:26:18
 * @desc [
    Setup for AlexaUtils PyPi

Steps When uploading changes:
    - update verison
    - cmd, navigate to dir:
        - python setup.py sdist
        - twine upload dist/*
            - username: __token__
            - pw in API_token.txt

NOTE:
    - If run into HTTPError: 403 Forbidden, may need to delete old version in dist to avoid duplicate uploads.  
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
version = "0.2.1"
description = "Auxiliary functions to clean pandas data frames"
author = "Jai Miles"
author_email = "jaimiles23@gmail.com"
keywords = ['clean', 'wrangle', 'pandas', 'dataframe', 'mangle',]
url = 'https://github.com/jaimiles23/pywrangle'
download_url = ''


##########
# Read files
##########

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()


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
)


##########
# Requirements
##########

install_requires = [
    'pandas == 1.1.0',
    
]


##########
# Setup
##########

if __name__ == '__main__':
    setup(**setup_args, install_requires = install_requires)