
##########
# Imports 
##########

import pandas as pd 


##########
# Constants
##########
# Dictionary of tuple keys indicating what str.clean method to use

CASE_TO_CLEAN = {
    ('l', 0)    :   str.lower,
    ('t', 1)    :   str.title,
    ('u', 2)    :   str.upper,
}

