# Print DataFrame Information with differences between two DataFrames:
#     - Columns
#     - Rows
#     - Size


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
    compare_end_df: int = -1,
    abs_comparison: bool = True,
    relative_comparison: bool = True,
    ) -> None:
    """Prints DataFrame information from args. 

    Args may include either be either pd.DataFrame or a dict returned from the
    `record_df_info` function.

    Args:
        args (List[ Union['df', dict]]): List of DataFrames & dicts to print information.
        compare_dfs (bool, optional): Show the difference between 2 DataFrames. 
            May show absolute and relative differences. Defaults to True.
        compare_base_df (int): Index of base DataFrame for comparison. Defaults to 0.
        compare_end_df (int): Index of DataFrame to compare to base. Defaults to -1.
        abs_comparison (bool): If should show absolute comparison between DataFrames. Defaults to True.
        relative_comparison (bool): If should show relative comparison between DataFrames. Defaults to True.         
    
    **Notes**
    
    - DataFrames are assigned a name based on the index that they are passed into args.
    - Relative (%) difference is calculated as total of base df.

    **Example**

    .. code-block:: python

        >>> df1, df2 = (create_df.create_int_df_size(cols= i * 10, rows= i * 20) for i in range(1, 3))
        >>> pw.print_df_info(df2, df1)

        Name       |    Cols   |    Rows   |    Size
        --------   |   -----   |   -----   |   -----
        0          |      20   |      40   |     800
        1          |      10   |      20   |     200
        Abs Diff   |     -10   |     -20   |    -600
        % Diff     |   -50.0   |   -50.0   |   -75.0

        Compared indices -1 & 0
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
        
        if args[i][DF_KEYS[0]] is None: 
            [DF_KEYS[0]] = i  # Change name if not indicated
        tbl_df_info.add_entry(args[i])

    ## Comparison
    if compare_dfs and len(args) > 1:   ## Dataframe difference

        df_abs_diff, df_rel_diff = dict(), dict()
        for key in DF_KEYS:
            if key == DF_KEYS[0]:   # name
                dif_abs, dif_relative = "Abs Diff", "% Diff"
            else:
                dif_abs = args[compare_end_df][key] - args[compare_base_df][key]
                dif_relative = round(dif_abs / args[compare_base_df][key] * 100, 5)

            df_abs_diff[key] = dif_abs
            df_rel_diff[key] = dif_relative

        if abs_comparison: 
            tbl_df_info.add_entry(df_abs_diff)
        if relative_comparison: 
            tbl_df_info.add_entry(df_rel_diff)


    tbl_df_info.print_info(show_records_col= False)
    if compare_dfs:
        print(f"Compared indices {compare_end_df} & {compare_base_df}")


