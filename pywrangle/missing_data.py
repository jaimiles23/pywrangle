"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-20 16:08:16
 * @modify date 2020-08-20 23:16:16
 * @desc [
    Contains auxiliary functions for cleaning missing data.
 ]
 */
"""


##########
# Imports
##########

from typing import (
    List,
    Tuple,
)


import numpy as np
import seaborn as sns
import pandas as pd


try:
    import printing
except:
    from pywrangle import printing


##########
# Print Nulls per column
##########

def show_col_nulls(
    df,
    show_null_heatmap: bool = True,
) -> None:
    """
    Calculates number of null values in each column and prints result.
    
    Calls auxiliary functions:
    - _count_column_nulls

    ## Tests
    >>> df_winereviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv")
    >>> show_col_nulls(df_winereviews)
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


    def _count_column_nulls(df) -> List[ Tuple[ int, str]]:
        """
        Returns list of tuples (str, int) each column and its number of nulls.
        """
        col_nulls: List[ Tuple[int, str]] = []

        ## Create tuples of number of nulls in respective column.
        for col in df.columns:
            num_null = df[col].isna().sum()
            col_nulls.append( (col, num_null))

        col_nulls.sort(key = lambda x: x[1], reverse = True)
        return col_nulls
    
    
    ## Print Nulls per column
    column_nulls = _count_column_nulls(df)
    max_colname_length = printing.get_max_colname_length(df, "Null")
    printing._print_headers_colname_singleattr(
        df= df, 
        singleattr_header= "Null",
        max_colname_length= max_colname_length,
    )
    printing._print_tuple_with_spacing(
        column_nulls, max_colname_length= max_colname_length)

    ## Null heatmap
    if show_null_heatmap:
        sns.heatmap( df.isnull(), cbar = False)
    return

