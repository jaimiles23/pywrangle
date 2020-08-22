"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-20 23:42:36
 * @modify date 2020-08-21 20:31:04
 * @desc [
    @size_change decorated function to tell the change in data frame size after running a funciton.
 ]
 */
"""

##########
# Imports
##########

from typing import (
    Tuple, Any
)

import numpy as np
import pandas as pd


try:
    import printing
    import aux_functions
except:
    from pywrangle import printing
    from pywrangle import aux_functions


##########
# Auxiliary functions
##########

def _create_dict( key_info: Tuple[ str, Any]) -> dict:
    """Returns dictionary from key_info tuple."""
    if not isinstance(key_info, tuple):       # note: can change to tuple, list generic"
        raise Exception("Must pass tuple of keys and information")

    new_dict = dict()
    for key, info in key_info:
        new_dict[key] = info
    return new_dict


##########
# Record df info
##########

def record_df_info(df, _name: str = "before") -> dict:
    """Records information about the dataframe.
    
    recorded dataframe information is passed to compare_dfs()
    to check differences between dataframes.
    """
    if not isinstance(df, pd.DataFrame):
        raise Exception("Must pass pandas dataframe object.")
    
    key_info = (
        ('name', _name),
        ('columns', len(df.columns)),
        ('size', df.size),
        ('shape', df.shape),
    )
    return _create_dict(key_info)


##########
# Print df changes
##########

def print_df_changes(
        df,
        dict_recorded_info: dict,
        show_col_names: bool = False
    ) -> None:
    """Differences between dataframe and previously recorded information.
    
    Calls auxiliary get_columns_difference method.
    """


    def get_df_diff_info(dict_recorded_info: dict, dict_new_info: dict) -> list:
        """Returns tuple with info on new df: (missing_cols, new_cols, diff_cols).
        """
        ## Columns
        num_cols_before, num_cols_after = (
            dict_recorded_info['columns'], dict_new_info['columns'])
        diff_cols = num_cols_before - num_cols_after

        ## Size
        diff_size = dict_new_info['size'] - dict_recorded_info['size']

        ## Shape
        diff_shape = ( [dict_new_info['shape'][i] - 
            dict_recorded_info['shape'][i] for i in range(2)])

        return (diff_cols, diff_size, diff_shape)


    ## Info on new df
    dict_new_info = record_df_info(df, _name = "after")

    ## Get df diff info
    diff_cols, diff_size, diff_shape = (
        get_df_diff_info( dict_recorded_info, dict_new_info))

    diff_info_keys = (
        ('name', "difference"),
        ('columns', diff_cols),
        ('size', diff_size),
        ('shape', diff_shape)
    )
    dict_diff_info = _create_dict(diff_info_keys)

    df_dicts = [
        dict_recorded_info,
        dict_new_info,
        dict_diff_info
    ]
    printing.print_formatted_dict(df_dicts)

