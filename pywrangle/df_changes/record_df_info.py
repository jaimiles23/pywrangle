# Contains `record_df_info` to record information: 
#     - Columns
#     - Rows
#     - Size


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
    """Returns dict with information about DataFrame, including name, cols, rows, and size.

    Args:
        df (DataFrame): DataFrame to record information from.
        name (Union[str, int], optional): Name of the DataFrame for comparison. Defaults to None.
    Returns:
        dict: Contains information about DataFrame.
    
    **Notes**

    - This function allows users change a DataFrame while recording its previous state.
    
        - For instance, after filtering a DataFrame, you may compare the two DataFrames using the **print_df_info** function.

    **Example**
    
    .. code-block:: python

        >>> df = create_df.create_int_df_size(cols= 10, rows= 20)
        >>> df_info = pw.record_df_info(df)
        >>> print(df_info)
        {'name': None, 'cols': 10, 'rows': 20, 'size': 200}

    """
    if not isinstance(df, pd.DataFrame):
        raise Exception("Must pass pandas DataFrame object!")

    return {
        DF_KEYS[0]  :   name,
        DF_KEYS[1]  :   len(df.columns),
        DF_KEYS[2]  :   len(df),
        DF_KEYS[3]  :   int(df.size)
    }
