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

import numpy as np
import pandas as pd


##########
# NP to String
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