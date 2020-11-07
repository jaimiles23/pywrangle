# Pywrangle
- [Pywrangle](#pywrangle)
- [About](#about)
- [Install](#install)
  - [Requirements](#requirements)
  - [Pip Install](#pip-install)
- [Import](#import)
- [Contributing](#contributing)
- [Documentation](#documentation)
- [TODO](#todo)

---

# About
PyWrangle is an open-source Python library for data wrangling. Wikipedia defines [data wrangling](https://en.wikipedia.org/wiki/Data_wrangling) as follows:
> is the process of transforming and mapping data from one "raw" data form into another format with the intent of making it more appropriate and valuable for a variety of downstream purposes such as analytics

PyWrangle currently supports:
- cleaning strings
- tracking dataframe changes
- Identifying data entry errors


PyWrangle is available on PyPI [here](https://pypi.org/project/pywrangle/)


# Install

## Requirements
- Python >= 3.8+
- numpy >= 1.14.4
- pandas >= 1.0.3
- fuzzywuzzy >= 0.18.0
- python-levenshtein >= 0.12.0
- metaphone >= 0.6

## Pip Install
To install pywrangle, use pip:

```
pip install pywrangle
```

# Import

Per convention with Python Analysis modules, import pywrangle as follows:
```
>>> import pywrangle as pw
```

# Contributing
Like all developers, I _love_ open source. Please reference the contributing guidelines [here](https://github.com/jaimiles23/pywrangle/blob/master/CONTRIBUTING.md)
<!-- TODO: ADD LINK TO CONTRIbuTING GUIDELINES> -->

# Documentation
Documentation on how to use PyWrangle is available [here](https://pywrangle.readthedocs.io/en/latest/)

# TODO
- [ ] Documentation
  - [x] Create documentation with Sphinx
  - [x] Host the documentation on Read the Docs
  - [ ] Requirements currently stored in `setup.py` - investigate reading from a `requirements.txt` file
- [ ] Data entry cleaning
  - [ ] Re-think output method for matches strings that may be due to data entry errors
  - [ ] Create method for users to automatically clean those strings via either 
    - [ ] (a) threshold similarity parameter or 
      - [ ] (b) manual list of items - can print 'families' of words above a threshold and allow user to manually pick which one to select, e.g., provide index in that list when passing it to function.
  - [ ] Investigate using jaro winkler distance. This places heavier emphasis on the beginning of the word and thus is more efficient at identifying different tenses & plural/singular companion forms.