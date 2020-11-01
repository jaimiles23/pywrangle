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

from typing import Union, List
import pandas as pd
import numpy as np

from .constants import DF_KEYS
from .record_df_info import record_df_info
from ..print_tbl.table_class import TableInfo


##########
# Print df 
##########

def print_df_info(
    *args: List[ Union['df', dict]],
    compare_dfs: bool = True
    ) -> None:
    """Prints df informations from dfs & recorded info in args

    Args:
        *args (List[ Union['df', dict]]): List of dfs & dicts of df info to print info
        compare_dfs (bool, optional): Show the differnece between the 1st & last df. Defaults to True.
    
    Note: Dataframes are assigned a name based on the position they are passed into *args
    """
    args = list(args)

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
    tbl_df_info = TableInfo(DF_KEYS)

    ## add values to table
    for i in range(len(args)):
        if not isinstance(args[i], dict):
            args[i] = record_df_info(args[i], name = i)
        
        if args[i][DF_KEYS[0]] is None: [DF_KEYS[0]] = i  # Change name if not indicated
        tbl_df_info.add_entry(args[i])

    ## Calculate difference value, if applicable
    if compare_dfs and len(args) > 1:

        df_diff_info = dict()
        for key in DF_KEYS:
            if key == DF_KEYS[0]:   # name
                value = 'Difference'
            else:
                value = args[0][key] - args[-1][key]
            df_diff_info[key] = value

        tbl_df_info.add_entry(df_diff_info)

    tbl_df_info.print_info()


