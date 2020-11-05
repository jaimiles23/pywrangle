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

def change_val(
    df: "DataFrame",
    column: str,
    current_val: Any,
    desired_val: Any
    ):
    """Returns DataFrame with values changed in column.

    Args:
        df (DataFrame): DataFrame to change.
        column (str): Column name to change.
        current_val (Any): Value to replace
        desired_val (Any): Value to change to.
    """
    

    ## Get matching rows
    df[column] = df[column].replace(current_val, desired_val)
    print(df)

    rows_with_matches = df[column].isin(list(current_val))
    print(rows_with_matches)

    

    ## Replace row values

