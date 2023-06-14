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

    with open("add_item.json", "a+") as f:
        nb_chars = f.read()
        if nb_chars == "":
            obj = []
        else:
            obj = load_from_json_file("add_item.json")

    for item in arguments:
        obj.append(item)

    save_to_json_file(obj, "add_item.json")
