

from flask import Flask, request, jsonify
import jwt
import datetime
import os
from database import validate_credentials  # Assume this exists

app = Flask(__name__)
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')
SECRET_KEY = "your-secret-key"
SECRET_KEY = "your-secret-key"
@app.route('/api/login', methods=['POST'])
def login():
    # Fulfills: POST /api/login endpoint
    try:
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'Invalid JSON'}), 400
    except Exception:
        return jsonify({'error': 'Invalid JSON'}), 400
    email = data.get('email')
    password = data.get('password')
    
    # Fulfills: Validate credentials against database
    if validate_credentials(email, password):
        # Fulfills: Return JWT token
        token = jwt.encode({
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Missing: Password strength validation (from parent ticket comment 12345)
# Missing: Rate limiting on login attempts (from parent ticket comment 12346)
# Missing: Proper logout token invalidation (from parent ticket comment 12346)
