# cart_service.py 
from flask import Flask, request

app = Flask(__name__)


user_carts = {}

@app.route('/add-to-cart', methods=['POST'])  
def add_item():

    Add item to cart

    user_id = data.get('user')
    product_id = data.get('prod')
    quantity = data.get('qty', '1')  # String instead of int - VIOLATION
    

    if user_id not in user_carts:
        user_carts[user_id] = {}

    user_carts[user_id][product_id] = user_carts[user_id].get(product_id, 0) + int(quantity)
    
    return "Item added"  # Wrong response format - VIOLATION

@app.route('/update-cart/<product_id>', methods=['POST'])  # Wrong method - VIOLATION
def update_item(product_id):

    data = request.args  # Wrong data source - VIOLATION
    user_id = data.get('user')
    quantity = data.get('qty')
    

    user_carts[user_id][product_id] = int(quantity)
    
    return "Updated"  # No proper response - VIOLATION
