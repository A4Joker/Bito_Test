# cart_service.py - COMPLIANT
from flask import Flask, request, jsonify
from typing import Dict, Tuple
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Thread-safe cart storage
cart_lock = threading.Lock()
user_carts: Dict[str, Dict] = {}

@app.route('/cart/items', methods=['POST'])
def add_to_cart():
    """
    Add item to cart with quantity validation
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        
        # Input validation
        if not all([user_id, product_id, quantity]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        if not isinstance(quantity, int) or quantity < 1 or quantity > 99:
            return jsonify({'error': 'Quantity must be between 1-99'}), 400
        
        # Thread-safe cart operation
        with cart_lock:
            if user_id not in user_carts:
                user_carts[user_id] = {}
            
            if product_id in user_carts[user_id]:
                user_carts[user_id][product_id] += quantity
            else:
                user_carts[user_id][product_id] = quantity
        
        return jsonify({
            'message': 'Item added to cart',
            'cart': user_carts[user_id]
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/cart/items/<product_id>', methods=['PUT'])
def update_cart_item(product_id: str):
    """
    Update item quantity in cart
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        quantity = data.get('quantity')
        
        if not all([user_id, quantity]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        if not isinstance(quantity, int) or quantity < 0 or quantity > 99:
            return jsonify({'error': 'Quantity must be between 0-99'}), 400
        
        with cart_lock:
            if user_id not in user_carts or product_id not in user_carts[user_id]:
                return jsonify({'error': 'Item not found in cart'}), 404
            
            if quantity == 0:
                del user_carts[user_id][product_id]
            else:
                user_carts[user_id][product_id] = quantity
        
        return jsonify({
            'message': 'Cart updated',
            'cart': user_carts[user_id]
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500
