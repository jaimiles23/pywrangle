"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-10-28 19:54:12
 * @modify date 2020-10-28 19:54:12
 * @desc [
    Tests for when cleaning string case.
 ]
 */
"""

##########
# Imports
##########

import pandas as pd 


##########
# Create dataframes
##########
"""
Test data contains 3 columns:
- ID
- Cleaned string
- uncleaned string
"""

df_cols = ['id', 'cleaned', 'uncleaned']
data = [
    [1, 'hello', ' hello'],
    [2, 'hello', 'HELLO'],
    [3, 'hello', ' HELLO '],
    [4, 'hello', 'Hello   '],
]

df_test = pd.DataFrame(data, columns = df_cols)


##########
# Test dataframes
##########

def test_case():
    assert 42 == 42
