# Converge all values in a Column to a single value.


##########
# Imports
##########

from typing import Any, Union
import pandas as pd 
import numpy as np


##########
# Dataframe
##########

def converge_sim_vals(
    df          :   'DataFrame',
    column      :   str,
    values      :   Union[tuple, list],
    index       :   int,
    ) -> "DataFrame":
    """Returns DataFrame with similar values in column 'converge' to the value at index.
    
    Args:
        df (DataFrame): DataFrame to change.
        column (str): Column name.
        values (Union[tuple, list]): Values to change.
        index (int): index in values for similar values to converge.
    
    **Example**

    .. code-block:: python

        >>> df = create_df.create_str_df4()
        >>> print(df)
                Index       States
            0      1    california
            1      2    california
            2      3   cali fornia
            3      4   californias
            4      5   californi a
            Index(['Index', 'States'], dtype='object')

        >>> values = ['california', 'cali fornia', 'californias', 'californi a']
        >>> index = 0
        >>> df = pw.converge_sim_vals(df= df, column= 'States', 
            values= values, index= index)
        >>> print(df)
                Index      States
            0      1   california
            1      2   california
            2      3   california
            3      4   california
            4      5   california    
            Index(['Index', 'States'], dtype='object')
    """
    correct_val = values[index]
    del values[index]

    matching_rows = df[column].isin(values)    
    df.loc[matching_rows, column] = correct_val

    return df
    