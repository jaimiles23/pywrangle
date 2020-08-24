## TODO list

### Add documentation
1. Add testing documentation.
   1. [Follow](https://python-packaging.readthedocs.io/en/latest/minimal.html)
2. Create pywrangle documentation website?

### Format printing of data frame changes
- Account for negative numbers
- Line numbers up on decimal places
- Reference aux_functions.py `is_negative` and `count_whole_digits`
  - NOTE: This will also affect the max length per columns, so need to incorporate both.

### Missing data
- null_correlation_matrix() function currently overwrites dataframe inplace. Should construct a new dataframe with the columns that contain nulls. 
- Add print statement


