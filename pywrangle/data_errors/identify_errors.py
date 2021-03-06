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
    """Prints potential data errors in the specified DataFrame column.

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
    
    **Notes**

    - Data entry errors are identified based on a Similarity Index.
    - The Similarity Index is calculated using algorithm's derived from levenshtein's distance and doublemetaphone.

        - `Levenstein's distance <https://en.wikipedia.org/wiki/Levenshtein_distance>`_
        - `Metaphone <https://en.wikipedia.org/wiki/Metaphone>`_


    **Example**

    .. code-block:: python

        >>> df = create_df.create_str_df2()
        ## Identify potential errors in the state column
        >>> pw.identify_errors(df= df, column= 'states', threshold= 70)     
        Record   |   String         |   Match          |   Similarity Index
        ------   |   ------------   |   ------------   |   ----------------
            1    |   california     |   californi as   |              92.75
            2    |   california     |   californi a    |               97.0
            3    |   california     |   californias    |              94.25
            4    |   california     |   cali fornia    |               96.0
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
