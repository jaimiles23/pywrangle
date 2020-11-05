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


def create_str_df2() -> "dataframe":
    """Creates string dataframe 
    """
    states = [
        ## Regular word
        'california',
        'colorado',
        'utah',
        'indiana',
        'texas',
        'oklahoma',
        'Nevada',
        
        ## Random space in word
        'cali fornia',
        'colo rado',
        'ut ah',
        'i ndiana',
        'te xas',
        'okla homa',
        'Neva da',
    ]
    data = {
        'a': range(100),
        'b': range(100),
        'c': [random.choice(['a', 'b', 'c'])* random.randint(0, 5) for _ in range(100)],
        'states': [random.choice(states) + ('s' if random.random() < 0.1 else '') for _ in range(100)] # Change for s
    }
    return pd.DataFrame(data)


def create_str_df3() -> "dataframe":
    """Creates string dataframe 
    """
    int_vals = [1,2,3]
    str_vals = ['a', 'b', 'c']

    data = {
        'a' :   [random.choice(int_vals) for _ in range(20)],
        'b' :   [random.choice(str_vals) for _ in range(20)],
    }
    return pd.DataFrame(data)

