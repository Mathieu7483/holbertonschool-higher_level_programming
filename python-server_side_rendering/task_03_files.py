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
    productIds = request.args.get('Id')
    data = []

    if source == 'json':
        with open('products.json', 'r') as jsonFile:
            data = json.load(jsonFile)

    elif source == 'csv':
        with open('products.csv', 'r', encoding='utf-8') as csvFile:
            csv_reader = csv.DictReader(csvFile)
            data = list(csv_reader)

    else:
        return render_template('product_display.html', error="Wrong source")
    
    if productIds:
        target_ids = productIds.split(',')
        
        filtered_data = []
        for item in data:
            product_id_str = str(item.get('id'))
            
            if product_id_str in target_ids:
                filtered_data.append(item)
        
        data = filtered_data
        
    return render_template('product_display.html', products=data, source=source)  
        
        
if __name__ == '__main__':
   app.run(debug=True, port=5000)
