"""
Script used to identify potential matches between string keys.
"""

##########
# Imports
##########

import numpy as np
import pandas as pd
from fuzzywuzzy import process

from ..print_tbl import TableInfo
from . import constants, ratios


##########
# Identify matches
##########

def identify_matching_strs(
    df          :   'dataframe', 
    col         :   str,
    threshold   :   int = 50
    ):
    """Identifies potential data entry errors in the column.
    Matching strings are identified based on a Similarity Index that is calculated from levenshtein's distance & doublemetaphone algorithms.

    Args:
        df (dataframe): DataFrame.
        col (str): Column to check.

    Returns:
        dict: dictionary containing ratio of matches.

    TODO:
    - Implement optional scorer option for process.extract
    - Add limit variable for parameter.
    - CONSIDER returning a dictionary of all these values -- create a second master dict that's returned. 
        Returning a dictionary with matches will be faster processing when implementing a process to clean the information.
    """

    ## Get keys
    keys = sorted(df[col].unique())

    ## TblInfo
    tbl_info_str_matches = TableInfo(
        (constants.TBL_DICT_KEYS[0],
        constants.TBL_DICT_KEYS[1],
        constants.TBL_DICT_KEYS[2]
        ))

    ## Add keys to 
    for key in keys:
        match_ratios = process.extract(key, keys, limit = 5)

        for match, _ in match_ratios:
            if match == key:    # don't compare vs self.
                continue

            ratio_dict = ratios.get_ratio_dict(key, match)
            if ratio_dict[ constants.SIM_INDEX] >= threshold:
                tbl_info_str_matches.add_entry(ratio_dict)
    
    tbl_info_str_matches.print_info()
    return
