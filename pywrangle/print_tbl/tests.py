"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-10-04 20:15:35
 * @modify date 2020-10-06 15:16:30
 * @desc [
    Tests for TableInfo: init, adding, & printing
 ]
 */
"""

##########
# Imports
##########

import random

from table_class import TableInfo
from dataclasses import dataclass


##########
# Tests Init
##########

def test_init_tbl() -> bool:
	"""Tests table init working as intended."""
	print_test_header("Initialize table tests")
	## Test information
	keys_results = (
		(
			['info'], 
			{'info': [], 'records': 0, 'keys': ['info']}
		),
		(
			['test', 'info'],
			{'test': [], 'info': [], 'records': 0, 'keys': ['test', 'info']}
		),
		(
			['a', 'b', 'c', 'd'],
			{'a': [], 'b': [], 'c': [], 'd': [], 'records': 0, 'keys': ['a', 'b', 'c', 'd']}
		),
		(
			[],
			{'records': 0, 'keys': []}
		)
	)
	## Run tests
	for tbl_key, tbl_attrs in keys_results:
		test = TableInfo(tbl_key)

		for key, value in tbl_attrs.items():
			try:
				assert getattr(test, key) == value
			except:
				print( getattr(test, key), value)
				raise Exception()


##########
# Test Add entry
##########

def test_add_entries() -> bool:
	"""Test tbl.add_entry() working as intended."""
	###### By List
	print_test_header("Test Adding by List")
	keys = ['a', 'b', 'c', 'd']
	entry_results = (
		( [1,2,3,4], {'a':[1], 'b':[2], 'c':[3], 'd':[4]} ),
		( [1,2,3], {'a':[1], 'b':[2], 'c':[3], 'd':[None]} ),
		( [1,2], {'a':[1], 'b':[2], 'c':[None], 'd':[None]} ),
	)
	for e, r in entry_results:
		tbl = None
		tbl = TableInfo(keys)
		tbl.add_entry(e, show_warn_vals= True)
		for k, v in r.items():
			try:			
				assert getattr(tbl, k) == v
			except:
				print(k, v)
				print(getattr(tbl, k), v)
				raise Exception
	
	# ###### By Dict
	# print_test_header("Test Add items by dict")
	# keys = ['a', 'b', 'c']
	# entry_results = (
	# 	( {'a': 1, 'b':2, 'c': 3}, {'a':[1], 'b':[2], 'c':[3]}),
	# 	( {'a': 1, 'c': 3}, {'a':[1], 'b':[None], 'c':[3]} ),
	# 	( {'a': 1, 'b':2, 'd': 3}, {'a':[1], 'b':[2], 'c':[None]} ),
	# )
	# for e, r in entry_results:
	# 	tbl = None
	# 	tbl = TableInfo(keys)
	# 	tbl.add_entry(e)
	# 	for k, v in r.items():
	# 		try:			
	# 			assert getattr(tbl, k) == v
	# 		except:
	# 			print(k, v)
	# 			print(getattr(tbl, k), v)
	# 			raise Exception
	
	# ###### By Class
	# print_test_header("Test Add items by Class")
	# keys = ['a', 'b']
	# @dataclass
	# class test1():
	# 	a: int
	# 	b: int
	# @dataclass
	# class test2():
	# 	a: int
	# 	c: int
	
	# a = test1(1, 2)
	# b = test2(1,2)

	# entry_results = (
	# 	(a, {'a':[1], 'b': [2]}),
	# 	(b, {'a':[1], 'b': [None]})
	# )
	# for e, r in entry_results:
	# 	tbl = None
	# 	tbl = TableInfo(keys)
	# 	tbl.add_entry(e, user_object=True)
	# 	for k, v in r.items():
	# 		try:			
	# 			assert getattr(tbl, k) == v
	# 		except:
	# 			print(k, v)
	# 			print(getattr(tbl, k), v)
	# 			raise Exception


def test_print_info():
	print_test_header("Testing print info")
	## Test 1
	keys = ['a', 'b', 'c', 'd']
	tbl = TableInfo(keys)

	records = (
		[1,2,3,4],
		[1,2,3],
		[1,2,3,4],
		[]
	)
	for r in records:
		tbl.add_entry(r)
	
	tbl.print_info()

	## Test 2
	keys = ['a', 'b', 'c', 'd']
	tbl = TableInfo(keys)

	records = (
		['asdfasf', 1, 2, '1' * 500],
		[None, None, 1, 2],
		['adsfadsfh', 5, 5, ''],
		[]
	)
	for r in records:
		tbl.add_entry(r)
	
	tbl.print_info()


	## Test 3
	keys = ['a', 'b', 'c', 'd']
	tbl = TableInfo(keys)

	records = (
		['asdfasf', 1, 2, '1' * 500],
		[None, None, 1, 2],
		['adsfadsfh', '5' * 100, 5, '12'],
		[]
	)
	for r in records:
		tbl.add_entry(r)
	
	tbl.print_info()

	## Test 4
	keys = ['a', 'b', 'c', 'd', 'e']
	tbl = TableInfo(keys)

	for _ in range(100):
		entry = [random.randint(1, 10) for _ in keys]
		tbl.add_entry(entry)
	
	tbl.print_info()


def print_test_header(text: str):
	header = '#' * 10
	spacing = '\n'
	print(spacing, header,spacing, header[0], text,spacing, header, spacing)


##########
# Main
##########

def main():
	# test_init_tbl()
	test_add_entries()
	# test_print_info()


if __name__ == "__main__":
	main()

