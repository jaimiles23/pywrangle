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

## Import

Per convention with Python Analysis modules, import pywrangle as follows:
```
>>> import pywrangle as pw
```

### Missing Data
print_nulls_per_col(df) -> None:
    Calculates number of null values in each column and prints result.
    

### String cleaning
def clean_str_columns(df: object, col_strcase_tuple: tuple) -> df:
    Master function to clean string columns using col_strcase_tuple key.


## TODO:
TODO lists available in pywrangle functions.


1. Add testing documenation.
   1. [Follow](https://python-packaging.readthedocs.io/en/latest/minimal.html)
2. Missing data functions
   1. show correlation between NULL values in different columns. e.g., if state is missing, likely region is missing too
   2. barchart with number of NULL per num columns
      1. show number of rows with NULL in only 1 column, 2 columns, 3 columns etc.
      2. May like to include optional parameters to show correlation b/w NULL values in different columns?
   3. Print number of rows with NULL in X columns - optional param for desc sort by num NULL?
3. Create wrapper that prints changes in the data frame size.
   1. Helpful when dropping is_na rows.
   2. Can create optional param to assert that dropped_rows = num_na before
4. Create pywrangle documentation website?