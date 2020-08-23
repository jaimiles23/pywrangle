"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-20 23:42:36
 * @modify date 2020-08-22 15:16:38
 * @desc [
    Contains two methods that work in tandem:
    - record_df_info, to record information about the dataframe before a change.
    - print_df_changes, to print information about changes to dataframe since recorded info.
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
# Record df info
##########

def record_df_info(df, _name: str = "before") -> dict:
    """Records information about the dataframe.
    
    Information includes:
        - name (state of the dict, before or after)
        - number of columns
        - number of rows
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
        ('rows', len(df)),
        ('size', int(df.size)),
        ('shape', df.shape),
    )
    return aux_functions.create_dict(key_info)


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
        
        Tuple: (diff_cols, diff_rows, diff_size, diff_shape).
        """
        ## Columns
        num_cols_before, num_cols_after = (
            dict_recorded_info['columns'], dict_new_info['columns'])
        diff_cols = num_cols_before - num_cols_after

        ## rows
        diff_rows = dict_recorded_info['rows'] - dict_new_info['rows']

        ## Size
        diff_size = dict_new_info['size'] - dict_recorded_info['size']

        ## Shape
        diff_shape = ( [dict_new_info['shape'][i] - 
            dict_recorded_info['shape'][i] for i in range(2)])

        return (diff_cols, diff_rows, diff_size, diff_shape)
    

    def get_dict_df_diff(dict_recorded_info: dict, dict_new_info: dict) -> dict:
        """Helper func to return dict of dataframe differences."""
        ## Get df diff info
        diff_cols, diff_rows, diff_size, diff_shape = (
            get_df_diff_info( dict_recorded_info, dict_new_info))

        diff_info_keys = (
            ('name', "df diff"),
            ('columns', diff_cols),
            ('rows', diff_rows),
            ('size', diff_size),
            ('shape', diff_shape)
        )
        return aux_functions.create_dict(diff_info_keys)
    

    def get_df_dict_headers() -> dict:
        """
        Returns dictionary with information abou the dataframes to be printed.

        NOTE: func should specify df_change_headers
        """
        key_info = (
            ('name', 'df'),
            ('columns', 'Num columns'),
            ('rows', 'Num rows'),
            ('size', 'df.size'),
            ('shape', 'df.shape')
        )
        return aux_functions.create_dict(key_info)


    ## Info on new df
    dict_new_info = record_df_info(df, _name = "after")

    ## Info on df diffs
    dict_diff_info = get_dict_df_diff( dict_recorded_info, dict_new_info)
    
    ## Headers
    df_headers: dict = get_df_dict_headers()

    df_dicts = [
        dict_recorded_info,
        dict_new_info,
        dict_diff_info
    ]
    printing.print_formatted_dict(
        df_dicts = df_dicts,
        header_dict = df_headers)
        
