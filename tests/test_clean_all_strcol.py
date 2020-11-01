"""
Runs tests for clean_strcol() function in str_cleaning dir.
"""

##########
# Imports
##########

import pandas as pd
import numpy as numpy

try:
    from context import (
        pywrangle as pw, 
        create_df
        )

except ModuleNotFoundError:
    from .context import (
        pywrangle as pw, 
        create_df
        )
        


##########
# Tests
##########

def test_clean_all_strcols():
    """Tests output for clean_str_col against the 'animals' column
    """
    df1, df2 = (create_df.create_str_df1() for _ in range(2))

    for col in df1.columns:
        df1[col] = df1[col].str.lower()
    
    df2 = pw.clean_all_strcols(df2)

    assert df1.equals(df2)
    return


def test_clean_nonstrcols():
    df1, df2 = (create_df.create_size_df(10, 10) for _ in range(2))

    df2 = pw.clean_all_strcols(df2)
    assert df1.equals(df2)


##########
# Main
##########

if __name__ == "__main__":
    test_clean_all_strcols()
    test_clean_nonstrcols()