#!/usr/bin/python3
'''
script that adds all arguments to a Python list,
and then save them to a file
'''


import sys


save_file = __import__('7-save_to_json_file').save_to_json_file
load_file = __import__('8-load_from_json_file').load_from_json_file
my_list = []
try:
    tmp_list = load_file("add_item.json")
    my_list = tmp_list
except Exception as e:
    pass

length = len(sys.argv)
for i in range(1, length):
    my_list.append(sys.argv[i])

my_list = save_file(my_list, "add_item.json")
