"""
Functions to track dataframe changes
"""

##########
# Imports
##########

from typing import (
    Union
)

import pandas as pd
import numpy as np
from ..print_tbl.table_class import TableInfo


##########
# Print df changes
##########

def print_df_changes(
        df,
        dict_recorded_info: dict,
        show_col_names: bool = False
    ) -> None:
    """
    Prints differences between dataframe and previously recorded information.
    
    Creates dicts of differences by calling 2 helper method:
        - get_df_diff_info
        - get_dict_diff_info
    
    >>> old_df = pw.df_info(df)
    >>> ... # some change to df
    >>> pw.print_df_changes(df, old_df)
    """

    def get_df_diff_info(dict_recorded_info: dict, dict_new_info: dict) -> tuple:
        """Returns tuple with info on differences b/w dfs.
        
        Tuple: (diff_rows, diff_cols, diff_size).
        """
        ## Rows & Cols
        diff_rows = dict_new_info['rows'] - dict_recorded_info['rows']
        diff_cols =  dict_new_info['columns'] - dict_recorded_info['columns']

        ## Size
        diff_size = dict_new_info['size'] - dict_recorded_info['size']

        return (diff_rows, diff_cols, diff_size )


    def get_dict_diff_info(dict_recorded_info, dict_new_info) -> dict:
        """Returns dictionary of differences between recorded and new dataframes."""
        ## get differences
        diff_rows, diff_cols, diff_size  = (
            get_df_diff_info( dict_recorded_info, dict_new_info))
        
        diff_info_keys = (
            ('name', "df diff"),
            ('rows', diff_rows),
            ('columns', diff_cols),
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
            'size',
        )

        for k in diff_percent_keys:
            try:
                diff_val, recorded_val = dict_diff_info[k], dict_recorded_info[k]
                val =  aux_functions.get_percent(diff_val / recorded_val)

            except (ZeroDivisionError):
                val = '--'
            
            dict_percent_diff_info[k] = val
        
        dict_percent_diff_info['name'] = "% diff"
        return dict_percent_diff_info


    def get_df_dict_headers() -> dict:
        """
        Returns dictionary with information abou the dataframes to be printed.

        NOTE: func should specify df_change_headers
        """
        key_info = (
            ('name', 'df'),
            ('rows', 'num rows'),
            ('columns', 'num columns'),
            ('size', 'df.size'),
        )
        return aux_functions.create_dict(key_info)


    ## Info on new df
    dict_new_info = record_df_info(df, _name = "after")

    ## Info on df diffs
    dict_diff_info = get_dict_diff_info( dict_recorded_info, dict_new_info)
    
    ## Info on df % diffs
    dict_percent_diff_info = get_dict_df_percent_diff( dict_recorded_info, dict_diff_info)

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
        
