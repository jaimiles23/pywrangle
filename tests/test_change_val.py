""" 
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
    print(df)
    df = pw.change_val(df, column= 'a', current_val = 1, desired_val = 'FIXED')


##########
# Main
##########
test_change_val()