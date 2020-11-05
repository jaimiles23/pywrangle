"""Function to changes values in a dataframe column.
"""

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
    """Returns dataframe with all values in column changed to value at index.

    Args:
        df (DataFrame): DataFrame to change
        column (str): Column Name
        values (list): Values to change
        val_index (int): Index of value to change others.
    """
    correct_val = values[val_index]
    del values[val_index]

    matching_rows = df[column].isin(values)    
    df.loc[matching_rows, column] = correct_val

    return df
    