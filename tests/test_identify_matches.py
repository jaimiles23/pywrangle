"""Script to test identifying matches
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
# Test identifying matches
##########

def test_identifying_matches():
    """Test identifying matches algo. This requires visual confirmation
    """

    df = create_df.create_str_df2()

    pw.identify_errors(df, 'states')



##########
# Main
##########

if __name__ == "__main__":
    test_identifying_matches()

