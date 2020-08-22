"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-21 22:18:13
 * @modify date 2020-08-21 22:18:13
 * @desc [
    Auxiliary functions for pywrangle.
 ]
 */
"""
##########
# Imports
##########

from typing import (
    Any,
    Tuple
)

import numpy as np
import pandas as pd


##########
# To string
##########
   
def to_str(var):
    """
    Aux method to transform NP arrays into string type.

    Credit: https://stackoverflow.com/a/25085806/14122026
    """
    if type(var) is list:
        return str(var)[1:-1] # list
    if type(var) is np.ndarray:
        try:
            return str(list(var[0]))[1:-1] # numpy 1D array
        except TypeError:
            return str(list(var))[1:-1] # numpy sequence
    return str(var) # everything else


##########
# Create dictionary
##########
   
def create_dict( key_info: Tuple[ str, Any]) -> dict:
    """Returns dictionary from key_info tuple."""
    if not isinstance(key_info, tuple):       # note: can change to tuple, list generic"
        raise Exception("Must pass tuple of keys and information")

    new_dict = dict()
    for key, info in key_info:
        new_dict[key] = info
    return new_dict

##########
# Print new lines
##########

def print_lines(num_new_lines: int = 2) -> None:
    """Prints number of new_line characters."""
    print(
        "\n" * num_new_lines,
        end = '')
    return