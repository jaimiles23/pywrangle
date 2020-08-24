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

col_strcase_tuple is a tuple of tuples representing the column names to be cleaned
and an ordinal number for the pandas str cleaning method to use.
Ordinal case control structure to determine case:
0 : lower_case
1 : title_case
2 : upper_case

```python
df_winereviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv")
col_strcase_tuple = (
        ("country", 2),
        ("description", 0)
        ("province", 1),
    )
df_winereviews = clean_str_columns( df_winereviews, col_strcase_tuple)
    column name:		str.clean_method
    country     		upper
    description 		lower
    province    		title
```

### Missing Data
> print_nulls_per_col(df) -> None:

Calculates number of null values in each column and prints result.

### Dataframe changes
The dataframe change functions `record_df_info` and `print_df_changes` are used in conjunction.
```python
>>> old_df = pw.df_info(df)
>>> ... # some change to df
>>> pw.print_df_changes(df, old_df)
```


> record_df_info(df, _name: str = "before") -> None:

Records information about the dataframe.
    
Information includes:
    - name (state of the dict, before or after)
    - number of rows
    - number of columns
    - size of df

recorded dataframe information is passed to compare_dfs()
to check differences between dataframes.

> print_df_changes(
        df,
        dict_recorded_info: dict,
        show_col_names: bool = False
    ) -> None:

Prints differences between dataframe and previously recorded information.


