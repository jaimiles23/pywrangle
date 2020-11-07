"""Contains `record_df_info` to record information: 
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

def record_df_info(
    df: 'DataFrame',
    name: Union[str, int] = None
    ) -> dict:
    """Records information about the DataFrame, including name, cols, rows, and size.

    Args:
        df (DataFrame): DataFrame to record information from.
        name (Union[str, int], optional): Name of the DataFrame for comparison. Defaults to None.
    Returns:
        dict: Contains information on DataFrame
    
    NOTE:
    - This function allows users to record a DataFrame state and then change it. For instance,
      filtering for a subset of data. The two states can then be compared using the `print_df_info` function.
    """
    if not isinstance(df, pd.DataFrame):
        raise Exception("Must pass pandas DataFrame object!")

    return {
        DF_KEYS[0]  :   name,
        DF_KEYS[1]  :   len(df.columns),
        DF_KEYS[2]  :   len(df),
        DF_KEYS[3]  :   int(df.size)
    }
