"""Auxiliary functions to generate dataframes.
"""

##########
# Imports
##########

import pandas as pd 


##########
# Size df
##########

def create_size_df(cols: int, rows: int) -> "dataframe":
    """Returns test dataframe with passed number of columns and rows.
    """
    df_dict = {
        chr(65 + i) : range(0, rows) for i in range(cols)
    }
    return pd.DataFrame(data = df_dict)


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
