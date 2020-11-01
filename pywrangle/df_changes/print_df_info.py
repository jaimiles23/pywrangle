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
    compare_dfs: bool = True,
    compare_base_df: int = 0,
    compare_end_df: int = -1
    ) -> None:
    """Prints df informations from dfs & recorded info in args

    Args:
        *args (List[ Union['df', dict]]): List of dfs & dicts of df info to print info
        compare_dfs (bool, optional): Show the difference between 2 dataframes. 
                                    Shows both absoluate and relative differences. 
                                    Defaults to True.
        compare_base_df (int): Index of base df to compare. Defaults to 0 (first df info).
        compare_end_df (int): Index of end df to compare. Defaults to -1 (last df info).
                    
    NOTE: 
    - Dataframes are assigned a name based on the index that they are passed into *args
    - Relative (%) difference is calculated as total of base df.

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

    if compare_dfs and len(args) > 1:   ## Dataframe difference

        df_abs_diff, df_rel_diff = dict(), dict()
        for key in DF_KEYS:
            if key == DF_KEYS[0]:   # name
                val_abs, val_rel = "Abs Diff", "% Diff"
            else:
                val_abs = args[compare_end_df][key] - args[compare_base_df][key]
                val_rel = round(val_abs / args[compare_base_df][key], 5) * 100

            df_abs_diff[key] = val_abs
            df_rel_diff[key] = val_rel

        tbl_df_info.add_entries(df_abs_diff, df_rel_diff)

    tbl_df_info.print_info(show_records_col= False)
    if compare_dfs:
        print(f"Compared DataFrames at index {compare_end_df} to {compare_base_df}")


