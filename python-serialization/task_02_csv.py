#!/usr/bin/python3
"""Module to convert CSV data to JSON format"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON format and write to data.json"""
    try:
        data_list = []
        
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                data_list.append(row)
        
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)
        
        return True
        
    except FileNotFoundError:
        print("File not found")
        return False
    except Exception as e:
        print("An error occurred: {}".format(e))
        return False
