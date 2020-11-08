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

def converge_sim_vals(
    df          :   'DataFrame',
    column      :   str,
    values      :   list,
    correct_index   :   int,
    ) -> "DataFrame":
    """Returns DataFrame with column cleaned so values converge to value at correct index.
    
    Args:
        df (DataFrame): DataFrame to change.
        column (str): Column name.
        values (list): Values to change
        correct_index (int): Index of value in values to converge on.
    
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
        >>> df = pw.change_values(df= df, column= 'States', 
            values= values, correct_index= index)
        >>> print(df)
                Index      States
            0      1  California
            1      2  California
            2      3  California
            3      4  California
            Index(['Index', 'States'], dtype='object')
    """
    correct_val = values[correct_index]
    del values[correct_index]

    matching_rows = df[column].isin(values)    
    df.loc[matching_rows, column] = correct_val

    return df
    