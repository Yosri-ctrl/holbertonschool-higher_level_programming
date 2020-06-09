#!/usr/bin/python3
"""
Creating the class Base
"""
import json as j


class Base:
    """
    Base is the foundation of the other classes
    eche object created has his owen id
    even if it's not givin
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return j.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list = []
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write(Base.to_json_string("[]"))
            for obj in list_objs:
                list.append(obj.to_dictionary())
            f.write(Base.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return j.loads(json_string)
