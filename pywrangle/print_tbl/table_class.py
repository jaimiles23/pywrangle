"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-10-04 21:25:45
 * @modify date 2020-10-05 14:58:33
 * @desc [
    Contains TableInfo class. Stores & Prints information.

TODO:
	- Add show_records parameter. If false, uses .keys instead of .tbl_keys for printing.
		- can assign one of these to a master self attr, e.g., self.print_keys.
]
*/
"""

##########
# Initialize table
##########

try:
	from tblinfo_aux import Aux_TblInfo
	from custom_errors import TblEntryWarning
	from script_objects import Any, Iterator, Table, Union, UserDefinedClass
except ModuleNotFoundError:
	from .tblinfo_aux import Aux_TblInfo
	from .custom_errors import TblEntryWarning
	from .script_objects import Any, Iterator, Table, Union, UserDefinedClass


##########
# TableInfo Class
##########

class TableInfo(Aux_TblInfo):
	"""Custom object to store user information"""
	##########
	# Init
	##########
	def __init__(self, tbl_keys: Union[dict, Iterator[Any]], col_alignment: Union[dict, None] = None):
		"""Initializes TableInfo objects with attributes based on TableInfo keys.

		Args:
			tbl_keys (Union[dict, Iterator[Any]]): List of attr keys to store information in tbl.
			col_alignment (Union[dict, None], optional): Alignment for markdown table. Defaults to None
		
		TODO: Test if passing dict.keys() works.
		"""
		if not hasattr(tbl_keys, '__iter__'):
			raise Exception("Initialization TableInfo must be type: List, Tuple, or Dictionary.")
		if isinstance(tbl_keys, list):		pass
		elif isinstance(tbl_keys, tuple):	tbl_keys = list(tbl_keys)
		elif isinstance(tbl_keys, dict):	tbl_keys = list(tbl_keys.keys())

		## Record information
		self.records = 0
		self.keys = tbl_keys
		self.tbl_keys = [self.records_key] + tbl_keys
		self.col_alignment = col_alignment if col_alignment else {k: 'l' for k in self.tbl_keys}

		## Info for printing
		self.num_cols = len(self.keys) + 1   # records col
		self.width_per_col = {k: len(k) for k in tbl_keys}
		self.col_sep = '|'
		self.num_spaces = 3

		for k in self.keys:
			setattr(self, k, list())
		return None
	

	##########
	# Add Entry
	##########
	def add_entry(
		self,
		entry: Union[dict, Iterator[Any], UserDefinedClass],
		user_object: bool = False,
		ignore_warnings: bool = False,
		show_warning: bool = True,
		show_warn_vals: bool = False
	) -> None:
		"""Adds entry to table class holding information

		Args:
			entry (Union[dict, Iterator[Any], UserDefinedClass]): Info to add to table.
			user_object (bool, optional): If entry is user_object. Defaults to False.
			ignore_warnings (bool, optional): Ignore all warnings. Defaults to False.
			show_warning (bool, optional): Show warnings when adding entry. Defaults to True.
			show_warn_vals (bool, optional): Show value assignments in warning. Defaults to False.
		
		Auxiliary methods:
			- convert_class_to_dict(): converts class to dict
			- convert_iter_to_dict(): convert iter to dict
		"""
		def convert_class_to_dict(entry: UserDefinedClass) -> dict:
			attr_dict = {}
			for k in self.keys:
				try: 					val = getattr(entry, k)
				except AttributeError:	val = None
				finally:				attr_dict[k] = val
			return attr_dict
		
		def convert_iter_to_dict(entry: Iterator) -> dict:
			iter_dict = {}
			for i in range(len(self.keys)):
				if i < len(entry):	val = entry[i] 
				else:				val = None
				iter_dict[self.keys[i]] = val
			return iter_dict


		##### add_entry parent method()
		flag_show_warning, warn_type = False, None
		
		## Make dict type
		if user_object:
			entry_dict = convert_class_to_dict(entry)
			if None in entry_dict.values():
				flag_show_warning, warn_type = True, TblEntryWarning.WARN_ATTR

		elif isinstance(entry, (list, tuple)):
			entry_dict = convert_iter_to_dict(entry)
			if len(entry) != len(self.keys):
				flag_show_warning, warn_type = True, TblEntryWarning.WARN_LEN

		elif isinstance(entry, dict):
			entry_dict = entry
			if list(entry.keys()) != self.keys:
				flag_show_warning, warn_type = True, TblEntryWarning.WARN_KEYS
		

		## Add info to Table.
		for k in self.keys:
			val = entry_dict.get(k, None)
			tbl_info = getattr(self, k) + [val]
			setattr(self, k, tbl_info)
		
		if flag_show_warning and not ignore_warnings:
			TblEntryWarning(
				warn_type= warn_type, 
				entry = entry,
				entry_dict= entry_dict, 
				show_values= show_warn_vals)
		
		## Miscellaneous
		self.records += 1
		self.update_col_lengths(entry_dict)
		return None


	def update_col_lengths(self, entry_dict) -> None:
		"""Updates the column lengths if entry_dict[k] is > than entry.

		Args:
			entry_dict (dict): values to compare to current column lengths.
		"""
		for k in self.keys:
			val = entry_dict.get(k, 0)
			if len(str(val)) > self.width_per_col[k]:
				self.width_per_col[k] = len(str(val))
		return None
	

	def add_entries(self, *args: Iterator, user_objects: bool = False) -> None:
		"""Calls add_entry() method on iterable.

		Args:
			entries (Iterator): Iterable of entries to add.
			user_objects (bool, optional): Indicates if entries are user defined objects. Defaults to False.
		"""

		for a in args:
			self.add_entry(a, user_object= user_objects)
		return None


	##########
	# Print information
	##########
	def print_info(
		self,
		num_spaces: int = 3,
		v_lines: bool = True,
		show_records_col: bool = True,

		column_alignment: Union[dict, None] = {},
		guess_alignment: bool = True, 
		
		markdown: bool = False,
		md_filename: str = None,
		write_type: str = 'w',
	):
		"""Prints information stored in the table.

		Args:
			num_spaces (int, optional): Number of spaces b/w col separator. Defaults to 3.
			v_lines (bool, optional): Print lines b/w columns. Defaults to True.
			show_records_column (bool, optional): If should show record number. Defaults to True.

			column_alignment (Union[dict, None], optional): colname: (l,r,c) alignment. Defaults to None.
			guess_alignment (bool): Autoassigns the column alignment by parsing the column.
			
			markdown (bool, optional): Instead of printing to console, writes to markdown file. Defaults to False.
			md_filename (str, optional): markdown filename to append to. Defaults to None
			write_type (str, optional): How to write to file - write or append. Defaults to 'ws'.
		
		Note:
			- Print methods used are stored in the Auxiliary methods module.
		"""
		## Print constants
		self.num_spaces = num_spaces
		self.col_sep = self.col_sep if v_lines else ''
		self.col_alignment = column_alignment if column_alignment else self.col_alignment

		## Records column
		self.show_records = show_records_col
		
		## Check alignment
		if guess_alignment and not column_alignment:
			self._parse_data_for_alignment()

		## Checks markdown
		self._markdown_on(markdown, md_filename)
		if not self.markdown:
			print('\n' * 1, end = '')	# space @ beginning
		else:
			self.writemode = write_type
		
		## Table Widths
		self._set_width_attrs()
		
		self._print_headers()
		self._print_horizontal_line()
		self._print_records()

		self._markdown_off(md_filename)