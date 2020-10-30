"""
Runs tests for clean_strcol() function in str_cleaning dir.
"""

##########
# Imports
##########

import pathlib
import os
import pandas as pd
import numpy as np
from context import pywrangle as pw 

try:
    from context import pywrangle as pw 
except ModuleNotFoundError: 
    from .context import pywrangle as pw



# print(pywrangle)


##########
# Create df
##########

def create_df() -> "dataframe":
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


##########
# Tests
##########

def test_clean_all_strcols():
    """Tests output for clean_str_col against the 'animals' column
    """
    df1 = create_df()
    df2 = create_df()

    for col in df1.columns:
        df1[col] = df1[col].str.lower()
    
    df2 = pw.clean_all_strcols(df2)

    assert df1.equals(df2)
    return



##########
# Main
##########

if __name__ == "__main__":
    test_clean_all_strcols()