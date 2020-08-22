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

except (ModuleNotFoundError):
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
    
    Information includes:
        - name (state of the dict, before or after)
        - number of columns
        - size of df
        - shape of df

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
# Dataframe key
##########

def _get_df_info_dict() -> dict:
    """
    Returns dictionary with information abou the dataframes to be printed.
    """
    key_info = (
        ('name', 'Dataframe'),
        ('columns', 'Num columns'),
        ('size', 'df size'),
        ('shape', 'df shape')
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
    
    Creates dicts of differences by calling 2 helper method:
        - get_df_diff_info
        - get_dict_df_diff
    """

    def get_df_diff_info(dict_recorded_info: dict, dict_new_info: dict) -> tuple:
        """Returns tuple with info on differences b/w dfs.
        
        Tuple: (diff_cols, diff_size, diff_shape).
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
    

    def get_dict_df_diff(dict_recorded_info: dict, dict_new_info: dict) -> dict:
        """Helper func to return dict of dataframe differences."""
        ## Get df diff info
        diff_cols, diff_size, diff_shape = (
            get_df_diff_info( dict_recorded_info, dict_new_info))

        diff_info_keys = (
            ('name', "difference"),
            ('columns', diff_cols),
            ('size', diff_size),
            ('shape', diff_shape)
        )
        return _create_dict(diff_info_keys)


    ## Info on new df
    dict_new_info = record_df_info(df, _name = "after")

    ## Info on df diffs
    dict_diff_info = get_dict_df_diff( dict_recorded_info, dict_new_info)
    
    ## Info on dicts
    dict_df_info = _get_df_info_dict()

    df_dicts = [
        dict_df_info,
        dict_recorded_info,
        dict_new_info,
        dict_diff_info
    ]
    printing.print_formatted_dict(df_dicts)

