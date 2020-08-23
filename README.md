# Pywrangle
Library for Python data wrangling to streamline string cleaning, identifying missing data, and tracking dataframe changes. Available on PyPI [here](https://pypi.org/project/pywrangle/)


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

### String cleaning
> def clean_str_columns(df: object, col_strcase_tuple: tuple) -> df:

Master function to clean string columns using col_strcase_tuple key.

### Missing Data
> print_nulls_per_col(df) -> None:

Calculates number of null values in each column and prints result.

### Dataframe changes




