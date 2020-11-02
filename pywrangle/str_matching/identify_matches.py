"""
Script used to identify potential matches between string keys.
"""


##########
# Imports
##########

import pandas as pd 
import numpy as np

from ..print_tbl import TableInfo


##########
# Identify matches
##########

def identify_errors(
    df  :   'dataframe', 
    col :   str,
    ) -> dict:
    """Identifies potential data entry errors in the column.

    Args:
        df (dataframe): DataFrame.
        col (str): Column to check.

    Returns:
        dict: dictionary containing ratio of matches.
    """

    ## TODO: Get keys

    ## TODO: Identify top matches for each get.

    ## TODO: Get ratio for top matches

    ## TODO: Only add to dictionary if above theshold

    ## TODO: Print table with top matches

    ## TODO: return dict object

    pass






