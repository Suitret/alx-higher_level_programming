#!/usr/bin/python3
"""Module containing script that adds all arguments
   to a Python list, and then save them to a file
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argc = len(sys.argv) - 1

if argc > 0:
    arguments = sys.argv[1:]
    obj = load_from_json_file("add_item.json")
    if obj is None:
        obj = []
    for item in arguments:
        obj.append(item)
    save_to_json_file(obj, "add_item.json")
