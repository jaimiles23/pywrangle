# Documentation
This file provides documentation on pywrangle functionalities.

- [Documentation](#documentation)
- [String cleaning](#string-cleaning)
  - [clean_all_strcols](#clean_all_strcols)
  - [Clean strcol](#clean-strcol)
- [Dataframe changes](#dataframe-changes)
  - [Print df info](#print-df-info)
  - [Record df info](#record-df-info)
- [String matching](#string-matching)
  - [Identify errors](#identify-errors)
    - [Example](#example)

# String cleaning

## clean_all_strcols
```python
def clean_all_strcols(
    df: "dataframe", 
    columns: Union[list, tuple, None] = None, 
    col_cases: Union[ list, tuple, None] = None, 
    trim: bool = True,
    clean_case: str = 'l'
    ) -> 'dataframe':
```
    Cleans string columns in dataframe. Prints column names and cleaning method used.

    Args:
        df (dataframe): Dataframe to clean
        col_cases (Union[ list, tuple, None]): Names of the columns to clean. Defaults to None.
        columns (Union[list, tuple, None], optional): col_cases to use with the columns. Defaults to None.
        trim (bool, optional): If should trim the columns. Defaults to True.
        clean_case (str): Sentence col_cases to default string column cleaning. Defaults to 'l'.
    
    Returns:
        DataFrame: Returns dataframe with cleaned colname.
    
    Notes:
    - Available cases include: 'l', 'u', and 't', for lower, upper and title respectively.



## Clean strcol
```python
def clean_strcol(
    df: "dataframe", 
    colname: str, 
    case: Union[str, int] = 'l', 
    trim: bool = True
) -> 'DataFrame':
```
    Cleans column in dataframe based on case and trim args.

    Args:
        df (dataframe): Dataframe to clean
        colname (str): Column to clean
        case (Union[str, int]): Case to standardize column, available in constants.py module. Defaults to 'l'.
        trim (bool, optional): If should trim white spaces from column. Defaults to True.

    Returns:
        DataFrame: Returns dataframe with cleaned colname.

# Dataframe changes
Prints out information about the dataframe for use.

## Print df info
```python
print_df_info(
    *args: List[ Union['df', dict]],
    compare_dfs: bool = True,
    compare_base_df: int = 0,
    compare_end_df: int = -1
    ) -> None:
```
    Prints df informations from dfs & recorded info passed as args.

    Args:
        *args (List[ Union['df', dict]]): List of dfs & dicts of df info to print info
        compare_dfs (bool, optional): Show the difference between 2 dataframes. 
                                    Shows both absoluate and relative differences. 
                                    Defaults to True.
        compare_base_df (int): Index of base df to compare. Defaults to 0 (first df info).
        compare_end_df (int): Index of end df to compare. Defaults to -1 (last df info).

    NOTE: 
    - Dataframes are assigned a name based on the index that they are passed into *args
    - Relative (%) difference is calculated as total of base df.


## Record df info
```python
def record_df_info( 
    df: 'dataframe', 
    name: Union[str, int] = None
    ) -> dict:
```
    Records information about the dataframe, including name, cols, rows, and size.

    Args:
        df (dataframe): Dataframe to recor
        name (Union[str, int], optional): Name of the dataframe for comparison. Defaults to None
    Returns:
        dict: Containing df info.
    
    NOTE:
    - Users may pre-emptively record a df & name it w/ this function. 
    - The dict can then be passed to `print_df_info()`, and the name will be preserved.

# String matching

## Identify errors
```python
def identify_matching_strs(
    df          :   'dataframe', 
    col         :   str,
    threshold   :   int = 50
    ):
```
    Identifies potential data entry errors in the column. 
    Prints a table with a row indicating the string and its matches.
    Strings matches are ranked by a "Similarity Index" that uses levenshtein's distance and double metaphone algorithms.
    
    Only matches above a certain threshold are shown.

    Args:
        df (dataframe): DataFrame.
        col (str): Column to check.
        threshold (int): Minimum Similarity Index to show. Defaults to 50.

    Returns:
        dict: dictionary containing ratio of matches.

    TODO:
    - Implement optional scorer option for process.extract
    - Add limit variable for parameter.
    - CONSIDER returning a dictionary of all these values -- create a second master dict that's returned. 
        Returning a dictionary with matches will be faster processing when implementing a process to clean the information.

### Example
```python
>>> pw.identify_matching_strs(df, 'states')     # identify matching strings in the states column.
...
Record   |   Key           |   Match         |   Ratio Index
------   |   -----------   |   -----------   |   -----------
    1    |   Neva da       |   Neva das      |          94.4
    2    |   Neva da       |   Nevada        |      65.33333
    3    |   Neva das      |   Neva da       |          94.4
    4    |   Neva das      |   Nevada        |          73.8
    5    |   Nevada        |   Neva da       |      65.33333
    6    |   Nevada        |   Neva das      |          73.8
    7    |   cali fornia   |   california    |          78.5
    8    |   cali fornia   |   californias   |            91
    9    |   cali fornia   |   colorado      |          52.4
    10   |   cali fornia   |   i ndiana      |          54.8
    11   |   california    |   cali fornia   |          78.5
```