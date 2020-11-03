"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-10-04 21:51:25
 * @modify date 2020-10-07 20:38:12
 * @desc [
    Contains auxiliary methods for table class.

    TODO: 
    - Will need to add other length counting methods for stri/dicts. 
    - May like to create self.c_len() methods for such
    - Integrate aligned list when passing initial keys. cntrl search "left".

    TODO:
    - In the future, create "type" dict for columns. 
        - If the column is int, then automatically format right?
        - if column is float, automatically format on decimal
        - if str, automatically format left.
        - once this is done, can remove special formatting for the records column (only ints).
 ]
 */
"""

##########
# Imports
##########
import os
import math
import shutil

try:
    from script_objects import Union, Tuple

except ModuleNotFoundError:
    from .script_objects import Union, Tuple


##########
# Auxiliary methods for the TableInfo class
##########

class Aux_TblInfo():
    """Contains aux methods & constants for the TblInfo class."""
    ALLOWED_TERM_WIDTH = 0.70
    indent = int((1 - ALLOWED_TERM_WIDTH) * 10)
    records_key = 'record'
    h_line = '-'

    ## markdown constants
    markdown = False
    mdfile = None
    writemode = 'w'

    ## Alignment constants
    align_l = 'l'
    align_r = 'r'
    md_aligns = {align_l:':--', align_r:'--:'}


    def __init__(self):
        """Attributes are instantiated in TblInfo() class."""
        self.records = 0
        self.keys = []
        self.tbl_keys = self.keys + [self.records_key]

        self.num_cols = len(self.keys) + 1   # records column
        self.width_per_col = {}

        self.col_sep = '|'
        self.num_spaces = 3

        ## markdown 
        self.col_alignment = {k: self.align_l for k in self.tbl_keys}

        ## Records col
        self.show_records = True


    ##########
    # Width Methods
    ##########
    def _set_width_attrs(self,) -> None:
        """Calls Width methods to set width attributes in class."""
        self._add_records_col_width()
        self._set_md_widths()
        self._set_width_cols_total()
        self._set_non_col_space()
        self._set_final_colwidths_dict()

    def _add_records_col_width(self) -> None:
        """Adds records column width to self._width_per_col"""
        widths = self.width_per_col
        widths[self.records_key] = len(max(str(self.records), self.records_key, key= len))
        self.width_per_col = widths
    
    def _set_md_widths(self) -> None:
        """Sets column widths minimum of markdown alignment characters"""
        if not self.markdown: return
        for k, v in self.width_per_col.items():
            col_align = self.col_alignment[k]
            if v < len(self.md_aligns[col_align]):
                self.width_per_col[k] = len(self.md_aligns[col_align])
        return

    def _set_width_cols_total(self) -> None:
        """Sets total column space used."""
        self.width_cols_total = sum(self.width_per_col.values())
    
    def _set_non_col_space(self) -> None:
        """Sets the total table width."""
        self.non_col_space = (       # Don't include end columns
            (self.num_cols * 2 - 2) * self.num_spaces + 
            (self.num_cols - 2) * len(self.col_sep)
        )


    def _set_final_colwidths_dict(self) -> dict:
        """Returns dictionary with width for each columns

        Returns:
            dict: {col_name: width}
        
        Aux functions:
            - get_col_prop_width(): returns proportion for each column
            - pad_col_prop_width(): pads proportional width for each column
        """
        def get_col_prop_width(col_width: int, allowed_width: int) -> int:
            """Returns new column width for table. Proprortionate to longest entry.
            
            Note:
                - Cannot just use the columns proportion of the table, because single digit columns
                will receive too small of a width. Instead, must pad columns after.
            """
            prop_width = int(allowed_width // (self.num_cols))
            
            if col_width < prop_width:
                return col_width
            return prop_width

        def pad_col_prop_width(prop_col_width: dict, allowed_width: int) -> dict:
            """Pads the proportional width of columns that are shorter than max length.
            
            1. Get extra padding & Columns to pad
            2. Get proportion of padding per column
            3. Add proportion of extra padding to each column.
            """
            extra_padding = allowed_width - (sum(prop_col_width[k] for k in self.tbl_keys))
            cols_to_pad = [k for k in self.tbl_keys if prop_col_width[k] < self.width_per_col[k]]

            tot_pad_needed = sum((self.width_per_col[k] for k in cols_to_pad))
            for k in cols_to_pad:
                prop_extra_padding = (self.width_per_col[k] / tot_pad_needed) * extra_padding
                col_padding =  prop_col_width[k] + int(prop_extra_padding)
                if col_padding > self.width_per_col[k]:
                    col_padding = self.width_per_col[k]     # not longer than needed

                prop_col_width[k] = col_padding

            return prop_col_width


        ## Allowed Width
        try: allowed_width = os.get_terminal_size().columns 
        except OSError: allowed_width = shutil.get_terminal_size().columns      # 3rd party app may block os method
        allowed_width *= self.ALLOWED_TERM_WIDTH
        
        if (
        self.width_cols_total + self.non_col_space <= allowed_width
        or self.markdown
        ):
           return
        
        ## Get proportional column widths
        prop_col_width = {k : get_col_prop_width(v, allowed_width) for k, v in self.width_per_col.items()}
        prop_col_width = pad_col_prop_width(prop_col_width, allowed_width)

        self.width_per_col = prop_col_width

        return


    ##########
    # Printing
    ##########
    def _print(self, *args) -> None:
        """Custom print w/ no separation/end chars."""
        try:        text = ''.join(*args)
        except:     text = ''.join([str(a) for a in args])

        if self.markdown:
            self.mdfile.write(text)
        else:   
            print(text, sep = '', end = '') 


    def _print_col_boundary(self, key: str) -> None:
        """Prints column boundary. If last key, prints new line.

        Args:
            key (str): Column key
        """
        if key == self.tbl_keys[-1]:
            self._print('\n')
        else:
            self._print_col_delim()

    
    def _print_col_delim(self) -> None:
        """Prints column delimiters: num_spaces, col_sep, num_spaces
        
        If no col_sep, prints num_spaces."""
        if len(self.col_sep) == 0:
            self._print(self.num_spaces * ' ')
        else:
            self._print(self.num_spaces * ' ', self.col_sep, self.num_spaces * ' ')
    
    def _print_cell(self, val: str, col: str, indent: bool = False):
        """Print cell contents

        Args:
            val (str): Value in cell
            col (str): Column of printing
            indent (bool, optional): Print initial indent for row. Defaults to False.
        """
        if indent:
            self._print_indent()

        align = self.col_alignment[col]
        if (align == self.align_l) or (self.markdown):
            self._print(val)
            self._fill_space(val, col)
        elif align == self.align_r:
            self._fill_space(val, col)
            self._print(val)
        else:
            Exception("Alignment not specified!")
        
        self._print_col_boundary(col)


    def _print_indent(self):
        """Prints table indent."""
        if self.markdown:
            return
        self._print(self.indent * ' ')


    def _print_headers(self) -> None:
        """Prints headers."""
        for key in self.tbl_keys:
            if key == self.records_key and not self.show_records:
                continue

            indent = True if key == self.records_key else False
            self._print_cell(key.title(), key, indent = indent)

        return
    

    def _print_horizontal_line(self) -> None:
        """Prints horizontal lines on the table."""
        def get_align_chars(k: str):
            """Returns chars to be used in each column if writing to .md, else returns self.hline"""
            align = self.col_alignment[k]
            return self.md_aligns[align]
        

        for key in self.tbl_keys:
            col_width = self.width_per_col[key]

            if key == self.records_key and not self.show_records:
                continue
            elif key == self.records_key:
                self._print_indent()

            if not self.markdown:
                self._print( self.h_line * col_width)
                self._print_col_boundary(key)
            else:
                align_chars = get_align_chars(key)
                self._print_cell( align_chars, key)
    
    
    def _print_records(self) -> None:
        """Prints table records for table.
        
        Aux functions:
            - print_row
        
        Notes:
            - v, r constants for 'values' and 'range'
            - range of -1 indicates finished printing value.
        """
        def print_row(row_records: dict, num_printed: int) -> Tuple[ dict, int]:
            """Prints values for rows without extending outside column."""
            for key in self.tbl_keys:
                indent = True if key == self.records_key else False

                if key == self.records_key and not self.show_records:
                    continue
                elif row_records[key][r] == -1:     # Check print empty cell
                    self._print_cell('', key, indent= indent)
                    continue
                
                ## Print cell
                low, upp = row_records[key][r]     ## Ranges
                val = row_records[key][v][low:upp]
                indent = True if (key == self.records_key) else False

                self._print_cell(val, key, indent)
                    
                ## Check done printing
                if upp == len(row_records[key][v]):
                    num_printed += 1
                    row_records[key][r] = -1
                    continue
                
                ## Update range
                low = upp
                if (upp + self.width_per_col[key]) < len(row_records[key][v]):
                    upp = upp + self.width_per_col[key]
                else:
                    upp = len(row_records[key][v])
                row_records[key][r] = (low, upp)
            return row_records, num_printed


        ## Main function
        v, r = 'val', 'range'
        for i in range(self.records):
            row_records = {k : {} for k in self.tbl_keys}

            # get records for row
            for key in self.tbl_keys:     
                val = str(i + 1) if (key == self.records_key) else str(getattr(self, key)[i])
                upp = len(val) if len(val) <= self.width_per_col[key] else self.width_per_col[key]
                row_records[key][v], row_records[key][r] = val, (0, upp)
            
            # print row
            num_printed = 0 if self.show_records else 1
            while num_printed != len(self.tbl_keys):
                row_records, num_printed = print_row(row_records, num_printed)
        
        self._print('\n' * 1)
        return None


    ##########
    # Spacing
    ##########
    def _fill_space(self, value: Union[int, str], col: str) -> None:
        """Prints space to fill column according to value length and column length.

        Args:
            value (Union[int, str]): int or string
            col (str): key to length of widths_per_col
        """
        col_len = self.width_per_col[col]
        _fill_space = col_len - len(str(value))
        self._print(' ' * _fill_space)
        return
    

    ##########
    # Markdown
    ##########

    def _markdown_on(self, markdown: bool, md_filename: str):
        """If markdown, sets up markdown attributes."""
        self.markdown = False
        if markdown:
            if not md_filename:
                raise Exception("Must pass `md_filename` to append table to.")
            self.markdown = True
            self.mdfile = open(md_filename, self.writemode)
        return
    
    def _markdown_off(self, md_filename: str) -> None:
        """If markdown, shutsdown markdown attributes."""
        if not self.markdown: return

        self.markdown = False
        self.mdfile.close()


    ##########
    # Alignment
    ##########

    def _parse_data_for_alignment(self) -> None:
        """Automatically checks data in column how to align data.

        Checks each record in the column and tries type conversion.
        Returns type if possible.
        """
        coltype_aligns = {
            int     :   self.align_r,
            float   :   self.align_r,
            str     :   self.align_l,
        }
        coltype_keys = list(coltype_aligns.keys())

        for k in self.col_alignment.keys():
            if k == self.records_key:
                self.col_alignment[k] = self.align_r
                continue

            check_type = 0
            for r in range(self.records):
                try:
                    coltype_keys[check_type](getattr(self, k)[r])
                except:
                    check_type += 1
                    if check_type == len(coltype_aligns) - 1:
                        break

            self.col_alignment[k] = coltype_aligns[ coltype_keys[check_type]]
        return

