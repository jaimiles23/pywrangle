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
from . import constants, similarity_index


##########
# Identify matches
##########

def identify_errors(
    df              :   'dataframe', 
    column          :   str,
    threshold       :   int = 65,
    show_progress   :   bool = False,
    limit           :   int = 5,
    ) -> None:
    """Prints to console potential data error entries in the specified DataFrame column.

    Data entry errors are identified based on string similarity, measured by a Similarity Index.
    The Similarity Index is calculated using algorithm's derived from levenshtein's distance 
    and doublemetaphone.
        https://en.wikipedia.org/wiki/Levenshtein_distance
        https://en.wikipedia.org/wiki/Metaphone
        
    Args:
        df (dataframe): DataFrame.
        column (str): Column in DataFrame to check.
        threshold (int): Rigor threshold to identify potential data errors. 
            A higher threshold returns more rigorous matching. 
            Defaults to 65 out of 100.
        show_progress (bool): Prints matching progress to console. Defaults to False.
        limit (int): Limits the number of matches to each string.
            Higher values increase computation time and return more false positives.
            Defaults to 5.
    """
    keys = sorted(df[column].unique())
    tbl_info_str_matches = TableInfo( constants.TBL_DICT_KEYS)  # printing info

    if show_progress:   print("Identifying potential data errors for:")
    for key in keys:
        if show_progress:   print(f"- {key}")

        matched_strs = sorted(
            process.extract(key, keys, limit = limit), 
            key = lambda x: x[1], 
            reverse = True)

        for match, _ in matched_strs:
            if match == key:    continue

            similarity_dict = similarity_index.get_similarity_index_dict(key, match)
            if similarity_dict[ constants.SIM_INDEX] >= threshold:
                tbl_info_str_matches.add_entry(similarity_dict)
    
    tbl_info_str_matches.print_info()
    return
