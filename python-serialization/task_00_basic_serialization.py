#!/usr/bin/python3
"""Module that serialize and deserialize a file to Json"""
import json


def serialize_and_save_to_file(data, filename):
    """Function that define a serialization of Json"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"error : {e}")

def load_and_deserialize(filename):
    """Function that define a deserialization of Json"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Utilisation de json.load pour lire le contenu du fichier et le désérialiser.
            data = json.load(f)
            print(f"✅ Données désérialisées chargées depuis '{filename}'.")
            return data
    except FileNotFoundError:
        print(f"error '{filename}' not found")
        return {}
    except json.JSONDecodeError as e:
        print(f" Error decode '{filename}' : {e}")
        return {}
    except Exception as e:
        print(f"error : {e}")
        return {}
