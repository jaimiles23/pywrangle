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

from . import ratios


##########
# Identify matches
##########

def identify_errors(
    df  :   'dataframe', 
    col :   str,
    threshold: int = 50
    ) -> dict:
    """Identifies potential data entry errors in the column.

    Args:
        df (dataframe): DataFrame.
        col (str): Column to check.

    Returns:
        dict: dictionary containing ratio of matches.

    TODO:
    - Implement optional scorer option for process.extract
    - Add limit variable for parameter.
    """

    ## Get keys
    keys = sorted(df[col].unique())


    ## TODO: Create table info
    ## TODO: Don't need match_dict, can just add immediately to table info
    ## TODO: Should probably also create constants with ALL keys?

    for key in keys:
        matches = process.extract(key, keys, limit = 5)

        for m in matches:
            if m == key:    # don't compare vs self.
                continue

            ratio_dict = ratios.get_ratio_dict(key, m)
            if ratio_dict[ ratios.RATIO_INDEX] >= threshold:
                match_dict[key] = ratio_dict
        



    ## TODO: Identify top matches for each get.
    # matches = process.extract(query, choices)

    ## TODO: Get ratio for top matches

    ## TODO: Only add to dictionary if above theshold

    ## TODO: Print table with top matches

    ## TODO: return dict object

    pass






