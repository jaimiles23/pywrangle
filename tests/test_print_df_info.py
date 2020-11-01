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
    df1, df2, df3, df4, df5 = (create_df.create_size_df(i * 10, i * 20) for i in range(1, 6))

    ## Compare 2 dfs
    pw.print_df_info(df2, df1)
    pw.print_df_info(df2, df1, compare_dfs= False)

    ## Print all dfs
    pw.print_df_info(df1, df2, df3, df4, df5, compare_dfs = False)
    pw.print_df_info(df1, df2, df3, df4, df5)
    pw.print_df_info(df1, df2, df3, df4, df5, compare_base_df= 3, compare_end_df=4)
    pw.print_df_info(df1, df2, df3, df4, df5, compare_base_df= 4, compare_end_df=3)


##########
# Main
##########

if __name__ == "__main__":
    test_print_df_info()