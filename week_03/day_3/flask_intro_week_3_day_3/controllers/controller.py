from flask import render_template

from app import app
from models.order_list import orders

@app.route('/')
def index():
    return render_template('index.html', order_list=orders)

@app.route('/order/<order_index>')
def order(order_index):
    return render_template('order.html', order=orders[int(order_index)])