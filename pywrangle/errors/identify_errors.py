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

def identify_errors(
    df              :   'dataframe', 
    column          :   str,
    threshold       :   int = 65,
    show_progress   :   bool = False, 
    ):
    """Identifies potential data entry errors in the column.
    Matching strings are identified based on a Similarity Index.
    This index is calculated from levenshtein's distance & doublemetaphone algorithms.
        https://en.wikipedia.org/wiki/Levenshtein_distance
        https://en.wikipedia.org/wiki/Metaphone
        
    Args:
        df (dataframe): DataFrame.
        column (str): column to check.
        threshold (int): Similarity index match threshold. A higher threshold returns more rigorous matching. Defaults to 65 out of 100.
        show_progress (bool): Identifying potential errors may be computationally intense. This prints matching progress to console. Defaults to False.

    Returns:
        dict: dictionary containing ratio of matches.

    TODO:
    - Implement optional scorer option for process.extract
    - Add limit variable for parameter.
    - CONSIDER returning a dictionary of all these values -- create a second master dict that's returned. 
        Returning a dictionary with matches will be faster processing when implementing a process to clean the information.
    """

    ## Get keys
    keys = sorted(df[column].unique())

    ## TblInfo
    tbl_info_str_matches = TableInfo(
        (constants.TBL_DICT_KEYS[0],
        constants.TBL_DICT_KEYS[1],
        constants.TBL_DICT_KEYS[2]
        ))

    ## Add keys to 
    if show_progress: print("Identifying potential errors for:")
    for key in keys:
        if show_progress:
            print(f"- {key}")

        match_ratios = sorted(
            process.extract(key, keys, limit = 5), 
            key = lambda x: x[1], 
            reverse= True)

        for match, _ in match_ratios:
            if match == key:    # don't compare vs self.
                continue

            ratio_dict = ratios.get_ratio_dict(key, match)
            if ratio_dict[ constants.SIM_INDEX] >= threshold:
                tbl_info_str_matches.add_entry(ratio_dict)
    
    tbl_info_str_matches.print_info()
    return
