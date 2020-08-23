"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-20 23:42:36
 * @modify date 2020-08-22 15:16:38
 * @desc [
    Contains two methods that work in tandem:
    - record_df_info, to record information about the dataframe before a change.
    - print_df_changes, to print information about changes to dataframe since recorded info.

TODO:
    - Add Df diff row to print_df_diff
 ]
 */
"""

##########
# Imports
##########

from typing import (
    Any, Tuple
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
        - number of rows
        - number of columns
        - shape of df
        - size of df

    recorded dataframe information is passed to compare_dfs()
    to check differences between dataframes.

    >>> old_df = pw.df_info(df)
    >>> ... # some change to df
    >>> pw.print_df_changes(df, old_df)
    """
    if not isinstance(df, pd.DataFrame):
        raise Exception("Must pass pandas dataframe object.")
    
    key_info = (
        ('name', _name),
        ('rows', len(df)),
        ('columns', len(df.columns)),
        ('shape', df.shape),
        ('size', int(df.size)),
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
    """
    Differences between dataframe and previously recorded information.
    
    Creates dicts of differences by calling 2 helper method:
        - get_df_diff_info
        - get_dict_diff_info
    
    >>> old_df = pw.df_info(df)
    >>> ... # some change to df
    >>> pw.print_df_changes(df, old_df)
    """

    def get_df_diff_info(dict_recorded_info: dict, dict_new_info: dict) -> tuple:
        """Returns tuple with info on differences b/w dfs.
        
        Tuple: (diff_rows, diff_cols, diff_shape, diff_size).
        """
        ## Rows & Cols
        diff_rows = dict_new_info['rows'] - dict_recorded_info['rows']
        diff_cols =  dict_new_info['columns'] - dict_recorded_info['columns']

        ## Shape
        diff_shape = ( [dict_new_info['shape'][i] - 
            dict_recorded_info['shape'][i] for i in range(2)])
        ## Size
        diff_size = dict_new_info['size'] - dict_recorded_info['size']

        return (diff_rows, diff_cols, diff_shape, diff_size )


    def get_dict_diff_info(dict_recorded_info, dict_new_info) -> dict:
        """Returns dictionary of differences between recorded and new dataframes."""
        ## get differences
        diff_rows, diff_cols, diff_shape, diff_size  = (
            get_df_diff_info( dict_recorded_info, dict_new_info))
        
        diff_info_keys = (
            ('name', "df diff"),
            ('rows', diff_rows),
            ('columns', diff_cols),
            ('shape', diff_shape),
            ('size', diff_size),
        )
        return aux_functions.create_dict(diff_info_keys)


    def get_dict_df_percent_diff(
        dict_recorded_info: dict,
        dict_diff_info: dict,
        ) -> dict:
        """Helper function to return dictionary of percentages of dataframe differences."""

        dict_percent_diff_info = dict()
        diff_percent_keys = (
            'rows', 
            'columns',
            'shape',
            'size',
        )

        for k in diff_percent_keys:
            try:
                diff_val, recorded_val = dict_diff_info[k], dict_recorded_info[k]
                val =  aux_functions.get_percent(diff_val / recorded_val)
            
            except (TypeError):
                val1 = aux_functions.get_percent(diff_val[0] / recorded_val[0])
                val2 = aux_functions.get_percent(diff_val[1] / recorded_val[1])
                val = (val1, val2)
            
            dict_percent_diff_info[k] = val
        
        dict_percent_diff_info['name'] = "df % diff"
        return dict_percent_diff_info


    def get_df_dict_headers() -> dict:
        """
        Returns dictionary with information abou the dataframes to be printed.

        NOTE: func should specify df_change_headers
        """
        key_info = (
            ('name', 'df'),
            ('rows', 'Num rows'),
            ('columns', 'Num columns'),
            ('shape', 'df.shape'),
            ('size', 'df.size'),
        )
        return aux_functions.create_dict(key_info)


    ## Info on new df
    dict_new_info = record_df_info(df, _name = "after")

    ## Info on df diffs
    dict_diff_info = get_dict_diff_info( dict_recorded_info, dict_new_info)
    
    ## Info on df % diffs
    dict_percent_diff_info = get_dict_df_percent_diff(dict_recorded_info, dict_diff_info)

    ## Headers
    df_headers: dict = get_df_dict_headers()

    df_dicts = (
        dict_recorded_info,
        dict_new_info,
        dict_diff_info,
        dict_percent_diff_info
    )
    printing.print_formatted_dict(
        df_dicts = df_dicts,
        header_dict = df_headers)
        
