"""Auxiliary functions to generate dataframes.
"""

##########
# Imports
##########

import pandas as pd 
import random

##########
# Int df Size
##########

def create_int_df_size(cols: int, rows: int) -> "dataframe":
    """Returns test dataframe with passed number of columns and rows.
    """
    df_dict = {
        chr(65 + i) : range(0, rows) for i in range(cols)
    }
    return pd.DataFrame(data = df_dict)


##########
# Str df Size
##########

def create_mixed_df_size(cols: int, rows: int) -> 'dataframe':
    """Returns test df with mixed number of columns and rows
    """
    str_data = ['a', 'b', 'c', 'd']
    data = dict()

    for i in range(cols):
        if i % 2:
            val = [ random.choice(str_data) * random.randint(0, 2) for _ in range(rows)]
        else:
            val = range(0, rows)
        
        data[chr(65 + i)] = val
    return pd.DataFrame(data)


##########
# String dfs
##########

def create_str_df1() -> "dataframe":
    """Returns test dataframe.
    """
    data = [
        ['Cat', 'Python', 'The'],
        ['doG', 'r', 'A'],
        ['biRd', 'SQL', None]
    ]
    columns = ('animals', 'languages', 'determiners')
    df = pd.DataFrame(data=data, columns=columns)
    return df
