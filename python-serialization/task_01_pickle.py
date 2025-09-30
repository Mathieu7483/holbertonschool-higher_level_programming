#!/usr/bin/python3
"""Module that serialize and deserialize a file to Json"""
import pickle


class CustomObject:
    """Custom class for serialization with pickle"""

    def __init__(self, name, age, is_student):
        """Initialize CustomObject instance"""
        self.name = name 
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """Serialize the object to a file using pickle"""
        try: 
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print("Error during serialization: {}".format(e))

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print("Error during deserialization: {}".format(e))
