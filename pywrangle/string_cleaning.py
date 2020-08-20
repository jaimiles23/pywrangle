"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-20 16:08:02
 * @modify date 2020-08-20 16:08:02
 * @desc [
    Contains pywrangle functions for cleaning string data.
 ]
 */
"""

##########
# Imports
##########

import typing

import numpy as np
import pandas as pd


##########
# Imports
##########

def clean_str_columns(df: object, col_strcase_tuple: tuple) -> object:
    """Master function to clean string columns using col_strcase_tuple key.

    col_strcase_tuple is a tuple of tuples representing the column names to be cleaned
    and an ordinal number for the pandas str cleaning method to use.
    Ordinal case control structure to determine case:
    0 : lower_case
    1 : title_case
    2 : upper_case
    
    ## Tests
    >>> df_winereviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv")
    >>> col_strcase_tuple = (
            ("country", 2),
            ("description", 0)
            ("province", 1),
        )
    >>> df_winereviews = clean_str_columns( df_winereviews, col_strcase_tuple)
        column name:0		str.clean_method
        country     		upper
        description 		lower
        province    		title
    
    https://www.kaggle.com/jaimiles23/wine-tasting
    """

    def _clean_str_data(
        df: object, 
        col_name: str, 
        case: int,
        max_coltitle_len: int,
        spacing: str,
        ) -> object:
        """
        Auxiliary function called on by the clean_str_columns.
        Cleans strings in dataframe for passed column name.
        
        Ordinal case control structure to determine sentence case:
        NOTE: case control structure for case is ostentatious. Re-try.
        0 : lower_case
        1 : title_case
        2 : upper_case

        NOTE: 
        df not accepting pandas str methods as first class functions.
        Implemented with if-else statements. Retained dict for case-cleaning message.

        TODO:
        - Add testing documentation
        """
        
        ## 1st class functions
        case_structure = {
            0 : str.lower,
            1 : str.title,
            2 : str.upper
        }
        
        if col_name not in df.columns:
            print(f"{col_name} not found in columns names: \n {df.columns}")
            raise NameError

        # Considers case_structure as a df attribute...
        # df[col_name] = df.loc[:, col_name].case_structure[case]().strip()
        
        df[col_name] = df.loc[:, col_name].str.strip()
        
        if case == 0:
            df[col_name] = df.loc[:, col_name].str.lower()
        elif case == 1:
            df[col_name] = df.loc[:, col_name].str.title()
        elif case == 2:
            df[col_name] = df.loc[:, col_name].str.upper()
        else:
            print(f"{case} not supported case.")
            return df
            
        extra_space = max_coltitle_len - len(col_name)
        print_message = [
            col_name, 
            " " * extra_space,
            spacing, 
            str(case_structure[case].__name__)
        ]
        print_message = ''.join(print_message)
        print(print_message)
        
        return df


    ## Cleans string column names
    title = "column name:"
    spacing = "\t" * 2
    
    max_coltitle_length = len(
        max((df.columns, title), key = len))
    extra_space = max_coltitle_length - len(title)
    
    print(f"{title}{extra_space}{spacing}str.clean_method")
    
    
    for col_name, sent_case in col_strcase_tuple:
        df = _clean_str_data(
            df = df,
            col_name = col_name,
            case = sent_case,
            max_coltitle_len = max_coltitle_length,
            spacing = spacing
        )
    return df
