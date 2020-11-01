"""Function to clean all string columns in data frame.
"""

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
    df: "dataframe", 
    columns: Union[list, tuple, None] = None, 
    col_cases: Union[ list, tuple, None] = None, 
    trim: bool = True,
    clean_case: str = 'l'
    ) -> 'dataframe':
    """Cleans string columns in dataframe.

    Args:
        df (dataframe): Dataframe to clean
        col_cases (Union[ list, tuple, None]): Names of the columns to clean. Defaults to None.
        columns (Union[list, tuple, None], optional): col_cases to use with the columns. Defaults to None.
        trim (bool, optional): If should trim the columns. Defaults to True.
        clean_case (str): Sentence col_cases to default string column cleaning. Defaults to 'l'.
    
    Returns:
        DataFrame: Returns dataframe with cleaned colname.
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
            raise Exception(f"{name} not in DF colnames!\n{df.columns}")

        is_str_col = df[name].dtype == (object)
        if is_str_col:
            df = clean_strcol(df, name, case, trim = trim)
            clean = CASE_TO_CLEAN[case].__name__
        else:
            clean = None
        
        entry = (name, is_str_col, clean)
        tbl_strcleaning.add_entry(entry)
    
    tbl_strcleaning.print_info()
    return df
