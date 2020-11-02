"""
Script used to identify potential matches between string keys.
"""


##########
# Imports
##########

import pandas as pd 
import numpy as np

from ..print_tbl import TableInfo

from fuzzywuzzy import process


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

    TODO:
    - Implement optional scorer option for process.extract
    """

    ## Get keys
    keys = (df[col].unique())

    for key in keys:
        matches = process.extract(key, keys)
        

    ## TODO: Identify top matches for each get.
    # matches = process.extract(query, choices)

    ## TODO: Get ratio for top matches

    ## TODO: Only add to dictionary if above theshold

    ## TODO: Print table with top matches

    ## TODO: return dict object

    pass






