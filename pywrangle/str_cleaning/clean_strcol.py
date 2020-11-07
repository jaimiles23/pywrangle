# Clean String Column


##########
# Imports 
##########

from typing import Union

import numpy as np
import pandas as pd

from .constants import CASE_TO_CLEAN


##########
# Clean string column
##########

def clean_strcol(
    df: "DataFrame",
    colname: str,
    case: Union['l', 't', 'u'] = 'l',
    trim: bool = True
) -> "DataFrame":
    """Cleans column in DataFrame based on case and trim args.

    Args:
        df (DataFrame): DataFrame to clean.
        colname (str): Column to clean.
        case (Union['l', 't', 'u']): Case to standardize column, available in constants.py module. Defaults to 'l' for lowercase.
        trim (bool, optional): If should trim white spaces from column. Defaults to True.

    Returns:
        DataFrame: Returns DataFrame with cleaned strings in specified column.
    
    **Example**

    .. code-block:: python

        >>> df1.animals = pw.clean_strcol(df1, 'animals', CASE_LIST[i])
    """
    if colname not in df.columns:
        Exception(
            f"{colname} not found in column names:" + 
            "".join(["\n - " + str(col) for col in df.columns])
        )
    elif df[colname].dtype != np.object:
        Exception(f"{colname} is not a numpy object!")

    if trim:
        df[colname] = df[colname].str.strip()
    
    case_keys = list(CASE_TO_CLEAN.keys())
    if case in case_keys[0]:
        df[colname] = df[colname].str.lower()
    elif case in case_keys[1]:
        df[colname] = df[colname].str.title()
    elif case in case_keys[2]:
        df[colname] = df[colname].str.upper()
    
    return df
