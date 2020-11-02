"""
Module contains functions that return ratios b/w words.

Fuzzywuzzy formulas use levenshtein's distance to compare strings.
"""

##########
# Imports
##########

import statistics
from fuzzywuzzy import fuzz, process
from metaphone import doublemetaphone

from . import constants


##########
# Metaphone
##########

def check_is_metaphone(t1: str, t2: str) -> int:
    """Returns num indicating if the two words are homophones. 1 == homophones, else 0.

    Args:
        t1 (str): First text to compare.
        t2 (str): Second text to compare.

    Returns:
        int: 1, 0 indicating if homophone.
    """
    t1_meta = doublemetaphone(t1)
    t2_meta = doublemetaphone(t2)

    for e in t1_meta:
        if e in t2_meta and e != '':
            return 1
    return None


##########
# Ratio Dict
##########

def get_ratio_dict(t1: str, t2: str) -> int:
    """Returns the exact token ratio between the two texts.

    Args:
        t1 (str): first text to compare
        t2 (str): second text to compare

    Returns:
        int: ratio b/w exact words
    """
    ratio_dict = {
        constants.RATIO_TYPES[0]    :   fuzz.ratio(t1, t2),
        constants.RATIO_TYPES[1]    :   fuzz.partial_ratio(t1, t2),
        constants.RATIO_TYPES[2]    :   fuzz.token_sort_ratio(t1, t2),
        constants.RATIO_TYPES[3]    :   fuzz.token_set_ratio(t1, t2),
        constants.RATIO_TYPES[4]    :   fuzz.WRatio(t1, t2),
        constants.RATIO_TYPES[5]    :   check_is_metaphone(t1, t2)
    }

    ratio_dict[constants.RATIO_INDEX] = statistics.mean([v for v in ratio_dict.values() if v != 0])     # Don't include 0 metaphone.
    return ratio_dict