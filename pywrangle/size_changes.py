"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-08-20 23:42:36
 * @modify date 2020-08-20 23:42:36
 * @desc [
    @size_change decorated function to tell the change in data frame size after running a funciton.
 ]
 */
"""

##########
# Imports
##########

from functools import wraps
from typing import Union

import pandas as pd


##########
# size_change
##########

def record_size_change(func, *args, **kwargs) -> None:
    """
    Prints changes to dataframes size and shape before and after the function.
    """
    def _get_df(*args, **kwarsgs) -> Union["Dataframe", None]:
        """
        Returns the dataframe from list of args.
        """
        for a in args:
            if isinstance(a, pd.DataFrame):
                return a
        for val in kwargs.values():
            if isinstance(val, pd.DataFrame):
                return val
        return None
    

    @wraps(func)
    def func_df_size_wrap(*args, **kwargs):
        df_1 = _get_df(*args, **kwargs)

        try:
            df_2 = func(*args, **kwargs)
        except:
            func(*args, **kwargs)
            df_2 = _get_df(*args, **kwargs)
        
        size_dif = df_1.size - df_2.size
        
        ## can make shape_dif into a funciton, and pass -1 to param.
        # dpeending on size differnece. This can be boolean value you subtract, 
        # e.g., larger_before
        # Then, print message accordingly, and change word to bigger/smalller.
        shape_dif = (
            df_1.shape[0] - df_2.shape[0],
            df_1.shape[1] - df_2.shape[1]
        )


        

