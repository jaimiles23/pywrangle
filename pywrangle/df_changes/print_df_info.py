""" Function to print difference between two dataframes:
    - Columns
    - Rows
    - Size


Note: Should be able to pass list iterable.
For each one, print out size, etc.

Then, if length of the list is only 2, THAT'S WHEN print 3rd row comparing.
"""

##########
# Imports
##########

from typing import Union
import pandas as pd
import numpy as np

from .constants import DF_KEYS
from .record_df_info import record_df_info
from ..print_tbl.table_class import TableInfo


##########
# Print df 
##########

def print_df_info(
    *args: Union['df', dict],
    compare_dfs: bool = True
    ) -> None:
    """Prints df informations from dfs & recorded info in args

    Args:
        *args (Union['df', dict]): dfs & dicts of df info to print info
        compare_dfs (bool, optional): Compare 1st & last column of dfs in table. 
                                      Defaults to True.
    """
    ## Check correct args
    for a in args:
        if not (
            isinstance(a, pd.DataFrame) or
            (
                isinstance(a, dict) and  
                tuple(a.keys()) != DF_KEYS
            )
        ):
            raise Exception("Must pass pandas DataFrame or saved df_info!")
    
    ## Create table keys
    tbl_dfinfo = TableInfo(DF_KEYS)

    ## add values to table
    for a in args:
        if not isinstance(a, pd.DataFrame):
            


    

    ## Add Tables


    ## Print object
    




