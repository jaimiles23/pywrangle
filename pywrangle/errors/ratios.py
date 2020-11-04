"""
Module contains functions that return ratios b/w words.

Fuzzywuzzy formulas use levenshtein's distance to compare strings.
"""

##########
# Imports
##########

from fuzzywuzzy import fuzz, process
from metaphone import doublemetaphone

from . import constants 
from . similarity_index import calculate_similarity_index


##########
# Metaphone
##########

def check_is_metaphone(t1: str, t2: str) -> int:
    """Returns num indicating if the two words are homophones. 1 == homophones, else 0.

    Args:
        t1 (str): First text to compare.
        t2 (str): Second text to compare.

    Returns:
        int: 100, 0 indicating if homophone.
    
    NOTE:
    - Metaphone is useful because it will consider words with spaces b/w the same, 
    e.g., California == Cali fornia
    """
    t1_meta = doublemetaphone(t1)
    t2_meta = doublemetaphone(t2)

    for e in t1_meta:
        if e in t2_meta and e != '':
            return 100  # 100 match
    return 0


##########
# Ratio Dict
##########

def get_ratio_dict(t1: str, t2: str) -> int:
    """Returns the exact token ratio between the two texts.

    Args:
        t1 (str): key to compare
        t2 (str): matced key to compare

    Returns:
        int: ratio b/w exact words
    
    NOTE:
    - future iteration may like to use jaro winkler distance. This puts more emphasis on
    beginning of word and thus more likely to catch tense & plurals.

    TODO:
    - Better implementation of dict 
        - should change mean implementaiton for clarity. 
        - Should refactor ratio_dict to not include t1 name & add that in outside method.
    """
    ratio_dict = {
        constants.RATIO_DICT_KEYS[0]    :   fuzz.ratio(t1, t2),
        constants.RATIO_DICT_KEYS[1]    :   fuzz.partial_ratio(t1, t2),
        constants.RATIO_DICT_KEYS[2]    :   fuzz.token_sort_ratio(t1, t2),
        constants.RATIO_DICT_KEYS[3]    :   fuzz.token_set_ratio(t1, t2),
        constants.RATIO_DICT_KEYS[4]    :   fuzz.WRatio(t1, t2),
        constants.RATIO_DICT_KEYS[5]    :   check_is_metaphone(t1, t2)
    }
    return {
        constants.TBL_DICT_KEYS[0]    :   t1,
        constants.TBL_DICT_KEYS[1]    :   t2,
        constants.TBL_DICT_KEYS[2]    :   calculate_similarity_index(ratio_dict)
    }
