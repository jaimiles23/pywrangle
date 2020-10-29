"""
Function used to clean column
"""

##########
# Imports 
##########

from typing import Union

import numpy as np
import pandas as pd

from constants import CASE_TO_CLEAN


##########
# Clean column function 
##########

def clean_col(
    df: "dataframe", 
    colname: str, 
    case: Union[str, int] = 'l', 
    trim: bool = True
) -> 'DataFrame':
    """Cleans column in dataframe based on case and trim args.

    Args:
        df (dataframe): Dataframe to clean
        colname (str): Column to clean
        case (Union[str, int]): Case to standardize column, available in constants.py module. Defaults to 'l'.
        trim (bool, optional): If should trim white spaces from column. Defaults to True.

    Returns:
        DataFrame: Returns dataframe with cleaned colname.
    """
    if colname not in df.columns:
        Exception(
            f"{colname} not found in column names:" + 
            "".join(["\n - " + str(col) for col in df.columns])
        )
    elif df[colname].dtype != np.object:
        Exception(f"{colname} is not a numpy object!")

    
    ## Trim
    if trim:
        df[colname] = df[colname].str.strip()
    
    if case in CASE_TO_CLEAN.keys()[0]:
        df[colname] = df[colname].str.lower()
    elif case in CASE_TO_CLEAN.keys()[1]:
        df[colname] = df[colname].str.title()
    elif case in CASE_TO_CLEAN.keys()[2]:
        df[colname] = df[colname].str.upper()
    
    return df
