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
    df          :   'dataframe', 
    col         :   str,
    threshold   :   int = 50
    ):
    """Identifies potential data entry errors in the column.

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
    tbl_info_ratios = TableInfo(['key', 'match', constants.RATIO_INDEX])

    ## Add keys to 
    for key in keys:
        match_ratios = process.extract(key, keys, limit = 5)

        for match, _ in match_ratios:
            if match == key:    # don't compare vs self.
                continue

            ratio_dict = ratios.get_ratio_dict(key, match)
            if ratio_dict[ constants.RATIO_INDEX] >= threshold:
                tbl_info_ratios.add_entry(ratio_dict)
    
    tbl_info_ratios.print_info()
    return
