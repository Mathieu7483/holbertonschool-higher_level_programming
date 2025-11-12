#!/usr/bin/python3
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
        items_list = data.get('items', [])
    return render_template('items.html', items=items_list)

@app.route('/products')
def products(csv_filename='products.csv' , json_filename='products.json'):
    try:
        data_list = []
        
        with open(products.csv, 'r', encoding='utf-8') as products.csv:
            csv_reader = csv_filename.DictReader(products.csv)

            for row in csv_reader:
                data_list.append(row)

        with open('products.json', 'w', encoding='utf-8') as json_filename:
            json.dump(data_list, json_filename)

        return render_template('products.html', products=data_list)

    except FileNotFoundError:
        print("File not found")
        return False
    except Exception as e:
        print("An error occurred: {}".format(e))
        return False

if __name__ == '__main__':
    app.run(debug=True, port=5000)
