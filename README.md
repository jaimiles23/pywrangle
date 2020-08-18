# Pywrangle
Library with auxiliary functions to clean pandas data frames. Available on PyPI [here](https://pypi.org/project/pywrangle/)

## Install
- Python 3.6+
- numpy
- pandas

To install pywrangle, use pip:
```
pip install pywrangle
```


## Contents

### Missing Data

### String cleaning

## TODO:
TODO lists available in pywrangle functions.

1. Missing data functions
   1. show correlation between NULL values in different columns. e.g., if state is missing, likely region is missing too
   2. barchart with number of NULL per num columns
      1. show number of rows with NULL in only 1 column, 2 columns, 3 columns etc.
      2. May like to include optional parameters to show correlation b/w NULL values in different columns?
   3. Print number of rows with NULL in X columns - optional param for desc sort by num NULL?
2. Create wrapper that prints changes in the data frame size.
   1. Helpful when dropping is_na rows.
   2. Can create optional param to assert that dropped_rows = num_na before


