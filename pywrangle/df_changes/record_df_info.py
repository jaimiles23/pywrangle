""" Function to record dataframe information: 
    - Columns
    - Rows
    - Size
"""

##########
# Imports
##########
from typing import Union

import pandas as pd
import numpy as np

from .constants import DF_KEYS


##########
# Record df info func
##########

def record_df_info( df: 'dataframe', name: Union[str, int] = None) -> dict:
    """Records information about the dataframe, including name, cols, rows, and size.

    Args:
        df (dataframe): Dataframe to recor
        name (Union[str, int], optional): Name of the dataframe for comparison. Defaults to None
    Returns:
        dict: Containing df info.
    
    NOTE:
    - Users may pre-emptively record a df & name it w/ this function. 
    - The dict can then be passed to print_df_info(), and the name will be preserved.
    """
    if not isinstance(df, pd.DataFrame):
        raise Exception("Must pass pandas dataframe object!")

    return {
        DF_KEYS[0]  :   name,
        DF_KEYS[1]  :   len(df.columns),
        DF_KEYS[2]  :   len(df),
        DF_KEYS[3]  :   int(df.size)
    }
