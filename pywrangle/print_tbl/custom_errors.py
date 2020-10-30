"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-10-04 20:13:18
 * @modify date 2020-10-07 18:21:33
 * @desc [
    custom_errors related to printing
 ]
 */
"""

##########
# Imports
##########

import warnings
from dataclasses import dataclass

try:
	from script_objects import Any, Iterator, List, Union, UserDefinedClass
except ModuleNotFoundError:
	from .script_objects import Any, Iterator, List, Union, UserDefinedClass


##########
# Warning Class
##########

@dataclass
class TblEntryWarning(UserWarning):
	"""Class to show warnings about table entries."""

	## Warning keys
	WARN_LEN = 'length'
	WARN_KEYS = 'keys'
	WARN_ATTR = 'class_attr'

	## Messages
	MSG_ITERATOR = "Iterator length did not match Table fields.\n"
	MSG_CLASS = "Class Attributes did not contain all Table fields.\n"
	MSG_DICT = "Dictionary did not contain all Table fields.\n"

	## Field assignment
	MSG_FIELD = '\nFields assigned values as follow:\n'

	##### Init
	"""Uses the warn_type (str) to determine what warning message to call.

	Args:
		entry_dict (Union[dict, Iterator[Any], UserDefinedClass]): information to record.
		tbl_info (dict): table holding information.
		show_values (bool, optional): show value assignment. Defaults to False.
	"""
	warn_type: str
	entry: Union[dict, Iterator[Any], UserDefinedClass]
	entry_dict: dict
	show_values: bool = False

	def __post_init__(self):
		self.warn_msg = self.get_warn_msg()
		self.write_warning()

	def get_warn_msg(self) -> List[str]:
		"""Returns warning message for object."""
		warn_dict = {
			self.WARN_LEN		:	self.MSG_ITERATOR,
			self.WARN_ATTR		:	self.MSG_CLASS,
			self.WARN_KEYS		:	self.MSG_DICT,
		}
		warn_msg = [warn_dict[self.warn_type]]
		if isinstance(self.entry, (list, tuple)):
			warn_msg.append(str(self.entry))
		elif isinstance(self.entry, dict):
			warn_msg.append(str(self.entry))
		else:
			warn_msg.append(str(dir(self.entry)))

		return warn_msg


	def write_warning(self):
		"""Shows warning that iterator length does not match keys length.
		
		if show_values, prints value assignment.
		"""
		warning_msg = self.warn_msg

		if self.show_values:
			warning_msg += [self.MSG_FIELD]
			for k, v in self.entry_dict.items():
				val_msg = f"\t- {k} : {v}\n"
				warning_msg.append(val_msg)

		warning_msg = ''.join(warning_msg)
		warnings.warn(warning_msg)
		# https://pymotw.com/2/warnings/ - use stack to show number of lines to move up.

