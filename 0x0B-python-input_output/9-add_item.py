#!/usr/bin/python3
"""
Creat an object from JSON file
"""
from sys import argv
import json as j
save_to_json = __import__('7-save_to_json_file').save_to_json_file
load_from_json = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        l = load_from_json("add_item.json")
    except:
        pass
        l = []
    for i in argv[1:]:
        l.append(i)
    save_to_json(l, "add_item.json")
