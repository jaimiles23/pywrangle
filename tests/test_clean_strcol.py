"""
Runs tests for clean_strcol() function in str_cleaning dir.
"""

##########
# Imports
##########

import pandas as pd
import numpy as np

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

def test_clean_strcol():
    """Tests output for clean_str_col against the 'animals' column
    """
    df1, df2 = (create_df.create_str_df1() for _ in range(2))

    CASE_LIST = ['l', 't', 'u']
    for i in range(len(CASE_LIST)):
        if i == 0:
            df2.animals = df2.animals.str.lower()
        elif i == 1:
            df2.animals = df2.animals.str.title()
        elif i == 2:
            df2.animals = df2.animals.str.upper()
        df1.animals = pw.clean_strcol(df1, 'animals', CASE_LIST[i])

        assert df1.equals(df2)

    return


##########
# Main
##########

if __name__ == "__main__":
    test_clean_strcol()