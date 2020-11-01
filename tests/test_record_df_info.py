""" 
Script to test recording dataframe information.
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
# Create df
##########

def test_record_df_info():
    """Tests recording dataframe information."""
    df = create_df.create_int_df_size(10, 20)
    df_info = pw.record_df_info(df)

    print(df_info)
    assert df_info == {
        'name'  :   None,
        'cols'  :   10,
        'rows'   :   20,
        'size'  :   200
    }


##########
# Main
##########

if __name__ == "__main__":
    test_record_df_info()