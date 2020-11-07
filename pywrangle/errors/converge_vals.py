# Converge all values in a Column to a single value.


##########
# Imports
##########

from typing import Any
import pandas as pd 
import numpy as np


##########
# Dataframe
##########

def converge_vals(
    df          :   'DataFrame',
    column      :   str,
    values      :   list,
    val_index   :   int,
    ) -> "DataFrame":
    """Returns DataFrame with all values in column changed to value at val_index.

    This function will have all 'values' converge on the value at the specified index.

    Args:
        df (DataFrame): DataFrame to change.
        column (str): Column name.
        values (list): Values to change
        val_index (int): Index of value in values to converge on.
    """
    correct_val = values[val_index]
    del values[val_index]

    matching_rows = df[column].isin(values)    
    df.loc[matching_rows, column] = correct_val

    return df
    