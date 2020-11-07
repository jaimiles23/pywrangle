# Converge all values in a Column to a single value.


##########
# Imports
##########

from typing import Any
import pandas as pd 
import numpy as np


##########
# Dataframe
##########

def converge_vals(
    df          :   'DataFrame',
    column      :   str,
    values      :   list,
    val_index   :   int,
    ) -> "DataFrame":
    """Returns DataFrame with all values in column changed to value at val_index.

    This function will have all 'values' converge on the value at the specified index.

    Args:
        df (DataFrame): DataFrame to change.
        column (str): Column name.
        values (list): Values to change
        val_index (int): Index of value in values to converge on.
    
    **Example**

    .. code-block:: python

        >>> df = create_df.create_str_df4()
        >>> print(df)
                Index       States
            0      1   California
            1      2   California
            2      3  Californias
            3      4  Californi a
            Index(['Index', 'States'], dtype='object')

        >>> values = ['California', 'Californias', 'Californi a']
        >>> index = 0
        >>> df = pw.converge_vals(df= df, column= 'States', 
            values= values, val_index= index)
        >>> print(df)
                Index      States
            0      1  California
            1      2  California
            2      3  California
            3      4  California
            Index(['Index', 'States'], dtype='object')
    """
    correct_val = values[val_index]
    del values[val_index]

    matching_rows = df[column].isin(values)    
    df.loc[matching_rows, column] = correct_val

    return df
    