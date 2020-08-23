"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-21 17:32:37
 * @modify date 2020-08-21 17:32:37
 * @desc [
    Contains Auxiliary functions to print data structures for readability on console.
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

except (ModuleNotFoundError):
    from pywrangle import aux_functions





##########
# Single Header
##########

def _print_headers_colname_oneattr(
    df: object,
    attr_header: str,
    max_colname_length: int = None,
    colname_header: str = "Column:",
    spacing: str = "\t" * 1,
    ) -> None:
    """
    Prints the headers for column names and a single attribute.
    """
    if not max_colname_length:
        max_colname_length = aux_functions.get_max_colname_length(df, colname_header= colname_header)
    extra_spaces = ' ' * (max_colname_length - len(colname_header))
    
    print(f"{colname_header}{extra_spaces}{spacing}{attr_header}")
    print(f"{len(colname_header) * '-'}{extra_spaces}{spacing}{'-' * len(attr_header)}")


def _print_tuple_with_colname_spacing(
    two_val_tuple: Tuple[ str, Any],
    max_colname_length: int = None,
    spacing: str = "\t" * 1
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

    aux_functions.print_lines(1)
    return 


##########
# Print formatted dict
##########

def print_formatted_dict(
    df_dicts: List[dict], 
    header_dict: dict,
    spacing: str = "\t" * 1,
    ) -> None:
    """
    Prints dictionaries for proper formatting.

    Calls two auxiliary functions:
        - get_key_max_charlength
        - print_dict_headers
    """

    def get_key_max_charlength(df_dicts: List[dict]) -> dict:
        """
        Returns dictionary with value max character length for all keys.

        NOTE: Uses keys from 1st dict in list to construct max dictionary.
        Can also create Set() to get all dictionary keys.
        """
        max_charlength_dict = dict()

        for k in df_dicts[0].keys():
            max_char_length = 0

            for df_dict in df_dicts:
                val = aux_functions.to_str(df_dict.get(k, ''))
                if len(val) > max_char_length:
                    max_char_length = len(val)

            max_charlength_dict[k] = max_char_length
        
        return max_charlength_dict
    
    
    def print_dict_headers( header_dict: dict, max_char_length: dict) -> None:
        """Prints headers for reading dictionary output."""
        for k in header_dict.keys():
            header = header_dict[k]
            num_extra_spaces = max_char_length[k] - len(header)
            print(
                header, 
                ' ' * num_extra_spaces,
                spacing,
                end = '')
        aux_functions.print_lines(1)
        
        for k in header_dict.keys():
            header_dashes = len( header_dict[k]) * '-'
            num_extra_spaces = max_char_length[k] - len(header_dashes)
            print(
                header_dashes, 
                ' ' * num_extra_spaces,
                spacing,
                end = '')
        aux_functions.print_lines(1)
        return None
    

    ## Get max char length dict
    max_char_length: dict = get_key_max_charlength(list(df_dicts) + [header_dict])          # df_dicts passed as tuple.

    ## Headers
    print_dict_headers(header_dict, max_char_length)

    ## Print values from all dicts
    for df_dict in df_dicts:
        for k in df_dicts[0].keys():
            
            value = df_dict[k]
            num_extra_spaces = max_char_length[k] - len(str(df_dict[k]))
            print(value, 
            ' ' * num_extra_spaces,
            spacing, 
            end = ''
            )
        print('')
    
    aux_functions.print_lines(1)
    return


##########
# Tests
##########



##########
# Main
##########

def main():
    pass


if __name__ == "__main__":
    main()

