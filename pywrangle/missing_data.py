"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-20 16:08:16
 * @modify date 2020-08-20 16:08:16
 * @desc [
    Contains auxiliary functions for cleaning missing data.
 ]
 */
"""


##########
# Imports
##########

## functools for wrappers
import numpy as np
import pandas as pd



##########
# Print Nulls per column
##########

def print_nulls_per_col(df) -> None:
    """
    Calculates number of null values in each column and prints result.
    
    Calls 2 auxiliary functions:
    - _count_column_nulls
    - _print_column_nulls

    ## Tests
    >>> df_winereviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv")
    >>> print_nulls_per_col(df_winereviews)
        89977	region_2
        45735	designation
        25060	region_1
        13695	price
        5	    country
        5	    province
        0	    description
        0	    points
        0	    variety
        0	    winery
    https://www.kaggle.com/jaimiles23/wine-tasting

    TODO:
        - Refactor lambda expression for clarity
        - Create auxiliary function to count total chars in data frame names.
        - Use aux func & switch num_nulls & col name columns
        - Update testing documentation to be compliant with pytests
    """


    def _count_column_nulls(df) -> list:
        """
        Returns list of tuples (int, str) indicating number of nulls per column.
        """
        ## Column null values
        col_nulls = []

        ## Create tuples of number of nulls in respective column.
        for col in df.columns:
            num_null = df[col].isna().sum()
            col_nulls.append( (num_null, col))

        col_nulls.sort(key = lambda x: x[0], reverse = True)
        return col_nulls


    def _print_column_nulls(null_per_columns: list) -> None:
        """
        Prints null values and column name in tuple.

        Pass list returned from _count_column_nulls.
        """
        print("NULLS\tColumn_name")
        for val, name in null_per_columns:
            print(val, name, sep = "\t")
    
    
    ## Call auxiliary functions.
    null_per_column = _count_column_nulls(df)
    _print_column_nulls(null_per_column)