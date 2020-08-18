"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-15 17:25:12
 * @modify date 2020-08-15 18:07:37
 * @desc [
    Contains PyWrangler class with utility functions to clean pandas data frames.

    Auxiliary methods to handle:
    - Missing data
    - String cleaning

    TODO:

    - Add input type checks & appropriate messages.
 ]
 */
"""


##########
# Imports
##########

## functools for wrappers
import numpy as np
import pandas as pd



##########
# PyWrangler
##########

class PyWrangler(object):
    """
    Class containing pandas datafrmae cleaning functions:
        - Missing data
        - String cleaning
        - DF wrappers
    
    The PyWrangler class can be imported as pw via:
    >>> from pywrangle import PyWrangler as pw
    """

    ##########
    # Missing data
    ##########

    @staticmethod
    def get_nulls_per_col(df) -> None:
        """
        Calculates number of null values in each column and prints result.
        
        Calls 2 auxiliary functions:
        - _count_column_nulls
        - _print_column_nulls

        ## Tests
        >>> df_winereviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv")
        >>> get_nulls_per_col(df_winereviews)
            89977	region_2
            45735	designation
            25060	region_1
            13695	price
            5	    country
            5	    province
            0	    description
            0	    points
            0	    variety
            0	    winery
        https://www.kaggle.com/jaimiles23/wine-tasting

        TODO:
            - Refactor lambda expression for clarity
            - Create auxiliary function to count total chars
            - Use aux func & switch num_nulls & col name columns
            - Update testing documentation to be compliant with pytests
        """

        @staticmethod        
        def _count_column_nulls(df) -> list:
            """
            Returns list of tuples (int, str) indicating number of nulls per column.
            """
            ## Column null values
            col_nulls = []

            ## Create tuples of number of nulls in respective column.
            for col in df.columns:
                num_null = df[col].isna().sum()
                col_nulls.append( (num_null, col))

            col_nulls.sort(key = lambda x: x[0], reverse = True)
            return col_nulls


        def _print_column_nulls(null_per_columns: list) -> None:
            """
            Prints null values and column name in tuple.

            Pass list returned from _count_column_nulls.
            """
            print("NULLS\tColumn_name")
            for val, name in null_per_columns:
                print(val, name, sep = "\t")
        
        
        ## Call auxiliary functions.
        null_per_column = _count_column_nulls(df)
        _print_column_nulls(null_per_column)


    ##########
    # String cleaning
    ##########

    @staticmethod
    def clean_str_columns(df: object, str_col_name_case: tuple):
        """Master function to clean string columns using str_col_name_case key.

        str_col_name_case is a tuple of tuples representing the column names to be cleaned
        and an ordinal number for the pandas str cleaning method to use.
        Ordinal case control structure to determine case:
        0 : lower_case
        1 : title_case
        2 : upper_case
        
        ## Tests
        >>> df_winereviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv")
        >>> str_col_name_case = (
                ("country", 2),
                ("description", 0)
                ("province", 1),
            )
        >>> df_winereviews = clean_str_columns( df_winereviews, str_col_name_case)
            column name:0		str.clean_method
            country     		upper
            description 		lower
            province    		title
        
        https://www.kaggle.com/jaimiles23/wine-tasting
        """

        @staticmethod
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
        
        
        for col_name, sent_case in str_col_name_case:
            df = _clean_str_data(
                df = df,
                col_name = col_name,
                case = sent_case,
                max_coltitle_len = max_coltitle_length,
                spacing = spacing
            )
        return df


    ##########
    # DF change wrapper function
    ##########



