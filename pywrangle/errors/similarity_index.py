"""
Algorithms to calcualte similarity ration between two words.

Fuzzywuzzy uses levenshtein's distance to calculate distance between strings, and 
metaphone uses the doublemetaphone algorithm to identify homophones.

https://en.wikipedia.org/wiki/Levenshtein_distance
https://en.wikipedia.org/wiki/Metaphone
"""


##########
# Imports
##########

from fuzzywuzzy import fuzz, process
from metaphone import doublemetaphone

from . import constants 


##########
# Metaphone
##########

def check_is_metaphone(str_1: str, str_2: str) -> int:
    """Returns integer depending on if the two words are homophones.
    
    Returns 100 if the words are homophones. Otherwise 0.

    Args:
        str_1 (str): First text to compare.
        str_2 (str): Second text to compare.

    Returns:
        int: 100 if str_1 and str_2 are homophones. Else 0.
    
    NOTE:
    - The doublemetaphone algorithm will return 100 for words with incorrect spacing.
    e.g., California == Cali fornia
    """
    str_1_meta = doublemetaphone(str_1)
    str_2_meta = doublemetaphone(str_2)

    for e in str_1_meta:
        if e in str_2_meta and e != '':
            return 100  # 100 match
    return 0


##########
# Similary index
##########

def calculate_similarity_index(ratios_dict: dict) -> float:
    """Returns index representing string similarity from ratios_dict.

    Index drops the lowest 2 string matching values to reduce chance of Type II error, 
    and missing matching strings.  This makes the index more likely to identify potential errors. 
    Note, one of these values is likely from the double metaphone algoirthm, which returns 0
    when the strings are not homophones.

    Args:
        ratios_dict (dict): Dictionary of ratio values.

    Returns:
        float: Represents the Similarity Index between two strings.
    """
    vals = [ v for v in ratios_dict.values() if isinstance(v, (int, float))]
    for _ in range(2):  vals.remove(min(vals))
    return round(sum(vals) / len(vals), 2)


##########
# Ratio Dict
##########

def get_similarity_index_dict(str_1: str, str_2: str) -> int:
    """Returns the exact token ratio between the two texts.

    Args:
        str_1 (str): First string to compare.
        str_2 (str): Second string to compare.

    Returns:
        int: Similarity Index from 0 to 100 representing the similarity of the two strings.
    
    NOTE:
    - future iteration may like to use jaro winkler distance. This puts more emphasis on
    beginning of word and thus more likely to catch tense & plurals.
    """
    ratio_dict = {
        constants.RATIO_DICT_KEYS[0]    :   fuzz.ratio(str_1, str_2),
        constants.RATIO_DICT_KEYS[1]    :   fuzz.partial_ratio(str_1, str_2),
        constants.RATIO_DICT_KEYS[2]    :   fuzz.token_sort_ratio(str_1, str_2),
        constants.RATIO_DICT_KEYS[3]    :   fuzz.token_set_ratio(str_1, str_2),
        constants.RATIO_DICT_KEYS[4]    :   fuzz.WRatio(str_1, str_2),
        constants.RATIO_DICT_KEYS[5]    :   check_is_metaphone(str_1, str_2)
    }
    return {
        constants.TBL_DICT_KEYS[0]    :   str_1,
        constants.TBL_DICT_KEYS[1]    :   str_2,
        constants.TBL_DICT_KEYS[2]    :   calculate_similarity_index(ratio_dict)
    }
