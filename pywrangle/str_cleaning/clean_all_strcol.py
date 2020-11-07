# Clean all string columns in a DataFrame.


##########
# Imports 
##########

from typing import Union

import numpy as np
import pandas as pd

from ..print_tbl.table_class import TableInfo
from .clean_strcol import clean_strcol
from .constants import CASE_TO_CLEAN


##########
# Clean all string columns
##########

def clean_all_strcols(
    df: "DataFrame", 
    columns: Union[list, tuple, None] = None, 
    col_cases: Union[ list, tuple, None] = None, 
    trim: bool = True,
    clean_case: str = 'l'
    ) -> "DataFrame":
    """Cleans string columns in DataFrame.

    Args:
        df (DataFrame): DataFrame to clean.
        col_cases (Union[ list, tuple, None]): Names of the columns to clean.
            If not specified, will attempt to clean all columns.
        columns (Union[list, tuple, None], optional): col_cases to use with the columns. 
            If not specified, will default to optional clean_case parameter.
        trim (bool, optional): If should trim the string data in columns. Defaults to True.
        clean_case (str): Sentence case to default string column cleaning. Defaults to 'l', or lowercase.
    
    Returns:
        DataFrame: Returns DataFrame with cleaned string columns.
    
    Notes:
    
    - Available sentence cases include: 'l', 'u', and 't', for lower, upper and title respectively.
    """
    ## Check columns
    if columns is None:
        columns = df.columns
    elif not isinstance(columns, (list, tuple)):
        raise Exception("Must pass list or tuple for columns!")
    
    ## Check case
    if col_cases is None:
        col_cases = [clean_case for c in columns]
    elif not isinstance(col_cases, (list, tuple)):
        raise Exception("Must pass list or tuple for case!")

    if len(columns) != len(col_cases):
        raise Exception("Number of columns must match number of cases provided!")
    
    ## Info table to print
    tbl_strcleaning_keys = ('Column', 'Is Str Col', 'Clean Method')
    tbl_strcleaning = TableInfo(tbl_strcleaning_keys)

    ## Iterate through columns.
    for info in zip(columns, col_cases):
        name, case = info

        if name not in df.columns:
            raise Exception(
        f"{name} not in DataFrame colnames!" + 
        "".join(["\n - " + str(col) for col in df.columns]))

        if (is_str_col := df[name].dtype == (object)):
            df = clean_strcol(df, name, case, trim = trim)
            clean = CASE_TO_CLEAN[case].__name__
        else:
            clean = None
        
        entry = (name, is_str_col, clean)
        tbl_strcleaning.add_entry(entry)
    
    tbl_strcleaning.print_info()
    return df
