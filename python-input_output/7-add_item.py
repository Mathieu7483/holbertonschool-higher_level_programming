#!/usr/bin/python3
""" Script that add all the arguments in command line"""
import sys
import os
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
args = sys.argv
if os.path.exists(filename):
    try:
        my_list = load_from_json_file(filename)
        if not isinstance(my_list, list):
            my_list = []
    except (json.JSONDecodeError, FileNotFoundError):
        my_list = []
else:
    my_list = []
    
my_list.extend(args[1:])
save_to_json_file(my_list, filename)
