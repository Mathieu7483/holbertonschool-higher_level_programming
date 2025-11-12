#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv


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
def products():
    source = request.args.get('source')
    productIds = request.args.get('productIds')
    data = []

    if source == 'json':
        with open('products.json', 'r') as jsonFile:
            data = json.load(jsonFile)

    elif source == 'csv':
        with open('products.csv', 'r') as csvFile:
            data = csv.DictReader(csvFile)
            data = list(data)
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if productIds:
        data = [item for item in data if item['id'] in productIds.split(',')]
        if not data:
            return render_template('product_display.html', error="No products found")   
        
        
if __name__ == '__main__':
   app.run(debug=True, port=5000)
