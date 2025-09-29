#!/usr/bin/python3
"""Module that define a class student """


class Student:
    def __init__(self, first_name, last_name, age):
        """Function that initialize the arguments"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that returns the dictionary description
        with simple data structure (list, dictionary, string,
         integer and boolean) for JSON serialization of an object:"""
        if isinstance(attrs, list):
            new_dict = {}
            for name in attrs:
                if name in self.__dict__:
                    new_dict[name] = self.__dict__[name]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Function that reload the class"""
        for key, value in json.items():
            self.first_name = "NewValue"
