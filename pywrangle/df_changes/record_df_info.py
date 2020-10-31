""" Function to record dataframe information: 
    - Columns
    - Rows
    - Size
"""

##########
# Imports
##########



import pandas as pd
import numpy as np


##########
# Record df info func
##########

def record_df_info( df: 'dataframe', name: str = 'before') -> dict:
    """Records information about the dataframe, including name, cols, rows, and size.

    Args:
        df (dataframe): Dataframe to recor
        name (str, optional): Name of the dataframe for comparison. Defaults to 'before'.

    Returns:
        dict: Containing df info.
    """
    if not isinstance(df, pd.DataFrame):
        raise Exception("Must pass pandas dataframe object!")

    return {
        'name'  :   name,
        'rows'  :   len(df),
        'cols'  :   len(df.columns),
        'size'  :   int(df.size)
    }
