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
    import aux_functions
except (ModuleNotFoundError):
    from pywrangle import printing
    from pywrangle import aux_functions


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
    
    
    ## Null values
    column_nulls = _count_column_nulls(df)

    ## Columns length
    max_colname_length = aux_functions.get_max_colname_length(df, "Null")

    ## Print headers
    printing._print_headers_colname_oneattr(
        df= df, 
        attr_header= "Null",
        max_colname_length= max_colname_length,
    )
    printing._print_tuple_with_colname_spacing(
        column_nulls, max_colname_length= max_colname_length)

    ## Null heatmap
    if show_null_heatmap:
        sns.heatmap( df.isnull(), cbar = False)
    return

