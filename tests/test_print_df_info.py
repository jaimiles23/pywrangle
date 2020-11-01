"""Runs tests for print_df_info()
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
# test print df info
##########

def test_print_df_info():
    """Tests printing dataframe information.
    """
    df1, df2 = (create_df.create_size_df(i * 10, i * 20) for i in range(1, 3))

    pw.print_df_info(df1, df2, compare_dfs=True)


##########
# Main
##########

if __name__ == "__main__":
    test_print_df_info()