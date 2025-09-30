#!/usr/bin/python3
"""Module that serialize and deserialize a file to Json"""
import json


def serialize_and_save_to_file(data, filename):
    """Function that define a serialization of Json"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Function that define a deserialization of Json"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)