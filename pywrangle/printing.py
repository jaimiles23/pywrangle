"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-21 17:32:37
 * @modify date 2020-08-21 17:32:37
 * @desc [
    Auxiliary functions to "pretty print" data structures.
 ]
 */
"""

##########
# Imports
##########

from typing import (
    Tuple, 
    Any, 
    List,
)


import numpy as np
import pandas as pd 


try:
    import aux_functions
except:
    from pywrangle import aux_functions


##########
# Max col length
##########

def get_max_colname_length(df, colname_header: str = "Column:") -> int:
    """
    Returns the longest column name from the dataframe, including the passed colname_header.
    """
    max_coltitle_length: int = len(
        max((df.columns, colname_header), key = len))
    return max_coltitle_length


##########
# Single Header
##########

def _print_headers_colname_singleattr(
    df: object,
    singleattr_header: str,
    max_colname_length: int = None,
    colname_header: str = "Column:",
    spacing: str = "\t" * 2,
    ) -> None:
    """
    Prints the headers for column names and a single attribute.
    """
    if not max_colname_length:
        max_colname_length = get_max_colname_length(df, colname_header= colname_header)
    extra_spaces = ' ' * (max_colname_length - len(colname_header))
    
    print(f"{colname_header}{extra_spaces}{spacing}{singleattr_header}")
    print(f"{len(colname_header) * '-'}{extra_spaces}{spacing}{'-' * len(singleattr_header)}")


def _print_tuple_with_spacing(
    two_val_tuple: Tuple[ str, Any],
    max_colname_length: int = None,
    spacing: str = "\t" * 2
    ) -> None:
    """
    Prints tuple of values with spacing between two values.
    """
    for val1, val2 in two_val_tuple:
        extra_spaces = ' ' * (max_colname_length - len(val1))
        print(
            val1,
            extra_spaces,
            spacing,
            val2,
        )
    return 


##########
# Print formatted dict
##########

def print_formatted_dict(
    df_dicts: List[dict], 
    spacing: str = "\t" * 2, 
    header_key: str = "name"
    ) -> None:
    """
    Prints dictionaries for proper formatting.
    """
    def get_key_max_charlength(df_dicts: List[dict]) -> dict:
        """
        Returns dictionary with max character length for all values.
        """
        max_charlength_dict = dict()

        for k in df_dicts[0].keys():
            max_char_length = 0

            for df_dict in df_dicts:
                val = aux_functions.to_str(df_dict[k])
                if len(val) > max_char_length:
                    max_char_length = len(val)

            max_charlength_dict[k] = max_char_length
        
        return max_charlength_dict
    

    ## Get max char length dict
    max_char_length: dict = get_key_max_charlength(df_dicts)

    ## Print headers:
    for df_dict in df_dicts:

        header = df_dict[header_key]
        num_extra_spaces = max_char_length[header_key] - len(header)
        print(
            header, 
            ' ' * num_extra_spaces,
            spacing,
            end = '')
    print('')

    ## Print header dashes
    for df_dict in df_dicts:

        header_dashes = len(df_dict[header_key]) * '-'
        num_extra_spaces = max_char_length[header_key] - len(header)
        print(
            header_dashes, 
            ' ' * num_extra_spaces,
            spacing,
            end = '')
    print('')

    ## Print values
    for df_dict in df_dicts:
        for k in df_dicts[0].keys():

            if k == header_key:
                continue

            value = df_dict[k]
            num_extra_spaces = max_char_length[k] - len(df_dict[k])
            print(value, 
            ' ' * num_extra_spaces,
            spacing, 
            end = ''
            )
        print('')



##########
# Tests
##########

def test_print_headers():
    _print_headers_colname_singleattr(
        None, 
        "Null",
        5
    )
    
##########
# Main
##########

def main():
    test_print_headers()


if __name__ == "__main__":
    main()
