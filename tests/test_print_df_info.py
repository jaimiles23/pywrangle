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