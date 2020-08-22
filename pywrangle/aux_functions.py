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
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

    