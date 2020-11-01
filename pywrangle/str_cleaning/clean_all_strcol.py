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
    all_strcols: bool = True,
    default_clean_case: Union[ str, None] = None
    ) -> 'dataframe':
    """Cleans string columns in dataframe.

    Args:
        df (dataframe): Dataframe to clean
        col_cases (Union[ list, tuple, None]): Names of the columns to clean. Defaults to None.
        columns (Union[list, tuple, None], optional): col_cases to use with the columns. Defaults to None.
        trim (bool, optional): If should trim the columns. Defaults to True.
        all_strcols (bool, optional): If col_cases & column names are not provided, clean all string columns
        default_clean_case (Union[ str, None]): Sentence col_cases to default string column cleaning. Defaults to None.
    
    Returns:
        DataFrame: Returns dataframe with cleaned colname.
    """
    ## Check columns passed
    if columns is None:
        columns = df.columns
    elif not isinstance(columns, (list, tuple)):
        raise Exception("Must pass list or tuple for columns!")
    
    ## Check case provided
    if col_cases is None:
        col_cases = ['l' for c in columns]
    elif not isinstance(col_cases, (list, tuple)):
        raise Exception("Must pass list or tuple for case!")

    if len(columns) != len(col_cases):
        raise Exception("Number of columns must match number of cases provided!")
    
    ## Create table to print information
    tbl_strcleaning_keys = ('Column', 'String Cleaning')
    tbl_strcleaning = TableInfo(tbl_strcleaning_keys)

    ## Iterate through columns.
    for info in zip(columns, col_cases):
        name, case = info

        df = clean_strcol(df, name, case, trim = trim)

        entry = (name, CASE_TO_CLEAN[case].__name__)
        tbl_strcleaning.add_entry(entry)
    
    tbl_strcleaning.print_info()
    return df
