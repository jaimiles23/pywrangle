# Constants for the String Cleaning Sub Package.

##########
# Imports 
##########

import pandas as pd 


##########
# Constants
##########
# Dictionary of tuple keys indicating what str.clean method to use

CASE_TO_CLEAN = {
    'l'    :   str.lower,
    't'    :   str.title,
    'u'    :   str.upper,
}

