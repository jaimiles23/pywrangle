""" Function to test converge vals.
Must be visually checked.
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
# Test Change values
##########
def test_change_val1():
    """Test change_val() function.
    """
    df = create_df.create_str_df3()
    values = ['a', 'b', 'd']
    val_index = 2
    df = pw.converge_vals(df, 'b', values, val_index)
    print(df)


def test_change_val2():
    """Test change_val() function.
    """
    df = create_df.create_str_df4()
    print(df)
    values = ['California', 'Californias', 'Californi a']
    index = 0
    df = pw.converge_vals(df= df, column= 'States', 
        values= values, val_index= index)
    print(df)


##########
# Main
##########
if __name__ == "__main__":
    # test_change_val1()
    test_change_val2()