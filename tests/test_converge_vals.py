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
def test_change_val():
    """Test change_val() function.
    """
    df = create_df.create_str_df3()
    values = ['a', 'b', 'd']
    val_index = 2
    df = pw.converge_vals(df, 'b', values, val_index)
    print(df)


##########
# Main
##########
test_change_val()