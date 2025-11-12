#!/usr/bin/python3
from flask import Flask, render_template, request, g
import json
import csv
import sqlite3


app = Flask(__name__)
DATABASE = 'products.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        
        cursor.execute('DROP TABLE IF EXISTS Products') 
        
        cursor.execute('''
            CREATE TABLE Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        
        db.commit()


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
    productIds = request.args.get('id')
    data = []

    if source == 'json':
        with open('products.json', 'r') as jsonFile:
            data = json.load(jsonFile)

    elif source == 'csv':
        with open('products.csv', 'r', encoding='utf-8') as csvFile:
            csv_reader = csv.DictReader(csvFile)
            data = list(csv_reader)

    elif source == 'sql':
        try:
            db = get_db()
            cursor = db.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            data = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
        except sqlite3.Error as e:
            return render_template('product_display.html', error=f'Database error: {e}')

    else:
        return render_template('product_display.html', error='Wrong source')
    
    if productIds:
        data = [item for item in data if str(item.get('id') or item['id']) == str(productIds)]
        if not data:
            return render_template('product_display.html', error='Product not found')
        
    return render_template('product_display.html', products=data, source=source)  


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)