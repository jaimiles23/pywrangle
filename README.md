
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

## PyWrangler class

Per convention of Python data analysis modules, PyWrangle can be imported as follows:
```
>>> from pywrangle import PyWrangler as pw
```

PyWrangler contains the following auxiliary functions:
1. print_nulls_per_col(df: DataFrame object) -> None.
   1. prints the number of null values in each df column.
2. clean_str_columns( df, col_strcase_tuple: tuple) -> df:
   1. Cleans dataframe's string columns based on col_strcase_tuple. Ordinal case structure determines which string cleaning method to use.
3. 



## TODO:
TODO lists available in pywrangle functions.

1. Add testing documenation.
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

