"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-20 23:42:36
 * @modify date 2020-08-21 14:32:12
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
# Funcs
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
        ('columns', df.columns.tolist()),
        ('size', df.size),
        ('shape', df.shape),
    )
    return _create_dict(key_info)


def print_df_changes(
        df,
        dict_recorded_info: dict,
        show_col_names: bool = False
    ) -> None:
    """Differences between dataframe and previously recorded information.
    
    Calls auxiliary get_column_info method.
    """
    

    def get_column_info(dict_recorded_info: dict, dict_new_info: dict) -> tuple:
        """Returns tuple with info on new df: (missing_cols, new_cols, diff_cols).
        """
        missing_cols = ['-' + column for column in
            np.setdiff1d( dict_recorded_info['columns'], dict_new_info['columns'], assume_unique = True)]
        new_cols = np.setdiff1d( dict_new_info['columns'], dict_recorded_info['columns']).tolist()

        diff_cols = missing_cols + new_cols
        return (missing_cols, new_cols, diff_cols)


    ## Info on new dict
    dict_new_info = record_df_info(df, _name = "after")

    ## Get column information
    missing_cols, new_cols, diff_cols = get_column_info(
        dict_new_info, dict_recorded_info)

    ## Size & Shape
    diff_size = dict_new_info['size'] - dict_recorded_info['size']
    diff_shape = [dict_new_info['shape'][i] - dict_recorded_info['shape'][i] for i in range(2)]
    
    diff_info_keys = (
        ('name', "Difference"),
        ('columns', diff_cols),
        ('size', diff_size),
        ('shape', diff_shape)
    )
    dict_diff_info = _create_dict(diff_info_keys)
    
    df_dfinfo = pd.DataFrame.from_dict([dict_recorded_info, dict_new_info, dict_diff_info])
    print(df_dfinfo)

