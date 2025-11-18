
from flask import Flask, request, jsonify
import sqlite3
import hashlib

app = Flask(__name__)

# VIOLATION: Plain text password storage in database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username text, password text)''')
    conn.commit()
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    # VIOLATION: No input validation
    # VIOLATION: No rate limiting
    # VIOLATION: No brute force protection
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    # VIOLATION: Weak MD5 hashing
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = c.fetchone()
    conn.close()
    
    if user:
        # VIOLATION: No proper session management
        # VIOLATION: No token expiration
        return jsonify({"status": "success", "message": "Logged in"})
    else:
        # VIOLATION: Detailed error messages
        return jsonify({"status": "error", "message": "Invalid username or password"})

@app.route('/register', methods=['POST'])
def register():
    # VIOLATION: No password policy
    # VIOLATION: No terms acceptance
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    # VIOLATION: Plain text storage (weak hashing)
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "success", "message": "User registered"})

# VIOLATION: Missing all security features
# VIOLATION: No MFA
# VIOLATION: No session management
# VIOLATION: No logging
# VIOLATION: No secure headers

if __name__ == '__main__':
    init_db()
    app.run(debug=True)  # VIOLATION: Debug mode in production
