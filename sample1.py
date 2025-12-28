
import os
import sys
import pickle
import yaml
import subprocess
import sqlite3
from flask import Flask, request, jsonify
from datetime import datetime

# ============================================================================
# VIOLATION 1: NO HARDCODED SECRETS (Multiple violations)
# ============================================================================

# 🔴 VIOLATION 1.1: Hardcoded API Keys
TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz123456"
TOKEN1 = "glpat-abcdefghijklmnopqrst"
TOKEN2 = "Yzc3ODk3OTk4OTk4Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3"
TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz123456"
TOKEN1 = "glpat-abcdefghijklmnopqrst"
TOKEN2 = "Yzc3ODk3OTk4OTk4Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3"
# 🔴 VIOLATION 1.2: Hardcoded Database Credentials
DB_HOST = "prod-db.company.com"
DB_USER = "admin_user"
DB_PASSWORD = "SuperSecurePassword123!@#"
DB_NAME = "production_database"



app = Flask(__name__)


# ============================================================================
# VIOLATION 2: NO SQL INJECTION (Multiple patterns)
# ============================================================================

def get_user_by_id_injection_v1(user_id):
    """🔴 VIOLATION 2.1: String concatenation SQL injection"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # VULNERABLE: Direct string concatenation
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    cursor.execute(query)
    return cursor.fetchall()


def get_user_by_id_injection_v2(user_id):
    """🔴 VIOLATION 2.2: F-string SQL injection"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # VULNERABLE: F-string formatting
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()


def get_user_by_id_injection_v3(username):
    """🔴 VIOLATION 2.3: .format() SQL injection"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # VULNERABLE: .format() method
    query = "SELECT * FROM users WHERE username = '{}'".format(username)
    cursor.execute(query)
    return cursor.fetchall()


def get_user_by_id_injection_v4(email):
    """🔴 VIOLATION 2.4: % formatting SQL injection"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # VULNERABLE: % formatting
    query = "SELECT * FROM users WHERE email = '%s'" % email
    cursor.execute(query)
    return cursor.fetchall()


def authenticate_user_injection(username, password):
    """🔴 VIOLATION 2.5: Login with SQL injection"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # VULNERABLE: Authentication bypass via SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return {"status": "authenticated", "user_id": user[0]}
    return {"status": "failed"}


def update_user_profile_injection(user_id, name, email, bio):
    """🔴 VIOLATION 2.6: UPDATE query with SQL injection"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # VULNERABLE: Multiple injection points
    query = f"UPDATE users SET name = '{name}', email = '{email}', bio = '{bio}' WHERE id = {user_id}"
    cursor.execute(query)
    conn.commit()


def delete_user_injection(user_id, confirmation):
    """🔴 VIOLATION 2.7: DELETE with SQL injection"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # VULNERABLE: Can delete all users
    query = f"DELETE FROM users WHERE id = {user_id} AND confirmed = {confirmation}"
    cursor.execute(query)
    conn.commit()


def search_products_injection(search_term):
    """🔴 VIOLATION 2.8: Search with SQL injection"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # VULNERABLE: Wildcard injection
    query = f"SELECT * FROM products WHERE name LIKE '%{search_term}%' OR description LIKE '%{search_term}%'"
    cursor.execute(query)
    return cursor.fetchall()


# ============================================================================
# VIOLATION 3: NO UNVALIDATED INPUT (Path traversal, command injection)
# ============================================================================

def read_user_file_path_traversal(filename):
    """🔴 VIOLATION 3.1: Path traversal vulnerability"""
    # VULNERABLE: No validation of filename
    filepath = f"/uploads/{filename}"
    
    with open(filepath, 'r') as f:
        return f.read()


def process_image_path_traversal(user_id, filename):
    """🔴 VIOLATION 3.2: Path traversal in image processing"""
    # VULNERABLE: Attacker can access any file
    filepath = f"/home/users/{user_id}/images/{filename}"
    
    # Process image
    result = subprocess.run(['convert', filepath, '-resize', '100x100', filepath], capture_output=True)
    return result.returncode == 0


def download_report_path_traversal(report_name):
    """🔴 VIOLATION 3.3: Path traversal in file download"""
    # VULNERABLE: Can download /etc/passwd, config files, etc.
    base_path = "/var/reports"
    filepath = os.path.join(base_path, report_name)
    
    with open(filepath, 'rb') as f:
        return f.read()


def execute_command_injection_v1(user_input):
    """🔴 VIOLATION 3.4: Command injection via shell=True"""
    # VULNERABLE: Direct command injection
    command = f"ping -c 1 {user_input}"
    result = subprocess.run(command, shell=True, capture_output=True)
    return result.stdout.decode()


def execute_command_injection_v2(filename):
    """🔴 VIOLATION 3.5: Command injection in file processing"""
    # VULNERABLE: Attacker can inject commands
    cmd = f"cat {filename} | grep 'ERROR' > /tmp/errors.log"
    os.system(cmd)


def execute_command_injection_v3(server, port):
    """🔴 VIOLATION 3.6: Command injection in network commands"""
    # VULNERABLE: Port can contain command injection
    command = f"telnet {server} {port}"
    subprocess.call(command, shell=True)


def process_csv_injection(csv_file):
    """🔴 VIOLATION 3.7: CSV formula injection"""
    # VULNERABLE: No validation of CSV content
    with open(csv_file, 'r') as f:
        lines = f.readlines()
    
    # Directly process without sanitization
    for line in lines:
        # If line starts with =, @, +, - it's a formula injection
        parts = line.split(',')
        # Process directly without validation
        process_data(parts)


def write_log_injection(user_input):
    """🔴 VIOLATION 3.8: Log injection"""
    # VULNERABLE: User input directly in logs
    log_message = f"User action: {user_input}"
    
    with open('/var/log/app.log', 'a') as f:
        f.write(log_message + '\n')


# ============================================================================
# VIOLATION 4: NO UNSAFE DESERIALIZATION (pickle, eval, exec)
# ============================================================================

def deserialize_pickle_unsafe(data):
    """🔴 VIOLATION 4.1: Unsafe pickle deserialization"""
    # VULNERABLE: pickle.loads() can execute arbitrary code
    try:
        obj = pickle.loads(data)
        return obj
    except:
        return None


def deserialize_yaml_unsafe(yaml_string):
    """🔴 VIOLATION 4.2: Unsafe YAML loading"""
    # VULNERABLE: yaml.load() without Loader can execute code
    config = yaml.load(yaml_string)
    return config


def eval_user_expression(expression):
    """🔴 VIOLATION 4.3: eval() on user input"""
    # VULNERABLE: eval() can execute arbitrary Python code
    result = eval(expression)
    return result


def exec_user_code(code):
    """🔴 VIOLATION 4.4: exec() on user input"""
    # VULNERABLE: exec() can execute arbitrary Python code
    exec(code)


def deserialize_json_with_eval(json_string):
    """🔴 VIOLATION 4.5: Using eval() to parse JSON"""
    # VULNERABLE: eval() instead of json.loads()
    data = eval(json_string)
    return data


def compile_and_execute(code_string):
    """🔴 VIOLATION 4.6: compile() and exec()"""
    # VULNERABLE: Compiling and executing user code
    compiled = compile(code_string, '<string>', 'exec')
    exec(compiled)


def deserialize_with_getattr(obj_string, method_name):
    """🔴 VIOLATION 4.7: getattr() with user input"""
    # VULNERABLE: Can call any method on object
    obj = pickle.loads(obj_string)
    method = getattr(obj, method_name)
    return method()


# ============================================================================
# VIOLATION 5: IMPROPER ERROR HANDLING (Bare except, silent failures)
# ============================================================================

def process_payment_bare_except(amount, card_token):
    """🔴 VIOLATION 5.1: Bare except clause"""
    try:
        # Process payment
        response = charge_card(amount, card_token)
        return response
    except:
        # VULNERABLE: Catches all exceptions, no logging
        pass


def authenticate_user_bare_except(username, password):
    """🔴 VIOLATION 5.2: Bare except with silent failure"""
    try:
        user = verify_credentials(username, password)
        return user
    except:
        # VULNERABLE: Silent failure, no error information
        return None


def load_config_bare_except(config_file):
    """🔴 VIOLATION 5.3: Bare except in config loading"""
    try:
        with open(config_file, 'r') as f:
            config = yaml.load(f)
        return config
    except:
        # VULNERABLE: Can't debug what went wrong
        return {}


def database_query_bare_except(query):
    """🔴 VIOLATION 5.4: Bare except in database operations"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except:
        # VULNERABLE: No error context
        return []


def api_call_bare_except(endpoint, params):
    """🔴 VIOLATION 5.5: Bare except in API calls"""
    try:
        import requests
        response = requests.get(endpoint, params=params, timeout=5)
        return response.json()
    except:
        # VULNERABLE: Network errors hidden
        return {}


def file_operation_bare_except(filepath):
    """🔴 VIOLATION 5.6: Bare except in file operations"""
    try:
        with open(filepath, 'r') as f:
            data = f.read()
        return data
    except:
        # VULNERABLE: File not found, permission denied - all hidden
        return ""


def json_parsing_bare_except(json_string):
    """🔴 VIOLATION 5.7: Bare except in JSON parsing"""
    import json
    try:
        data = json.loads(json_string)
        return data
    except:
        # VULNERABLE: Invalid JSON - no indication
        return None


def critical_operation_bare_except(user_id, action):
    """🔴 VIOLATION 5.8: Bare except in critical operations"""
    try:
        # Critical business logic
        process_critical_action(user_id, action)
        log_action(user_id, action)
        notify_user(user_id)
    except:
        # VULNERABLE: Critical failure hidden
        pass


# ============================================================================
# FLASK ROUTES WITH MULTIPLE VIOLATIONS
# ============================================================================

@app.route('/api/user/<user_id>')
def get_user_route_violations(user_id):
    """🔴 MULTIPLE VIOLATIONS: SQL injection + no error handling"""
    try:
        # VIOLATION: No input validation
        # VIOLATION: SQL injection
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE id = {user_id}"
        cursor.execute(query)
        user = cursor.fetchone()
        return jsonify(user)
    except:
        # VIOLATION: Bare except
        pass


@app.route('/api/upload', methods=['POST'])
def upload_file_violations():
    """🔴 MULTIPLE VIOLATIONS: Path traversal + command injection + no validation"""
    try:
        file = request.files['file']
        filename = file.filename
        
        # VIOLATION: Path traversal - no validation
        filepath = f"/uploads/{filename}"
        file.save(filepath)
        
        # VIOLATION: Command injection
        os.system(f"chmod 644 {filepath}")
        
        return jsonify({"status": "uploaded"})
    except:
        # VIOLATION: Bare except
        return None


@app.route('/api/search')
def search_products_route_violations():
    """🔴 MULTIPLE VIOLATIONS: SQL injection + no input validation"""
    try:
        search_term = request.args.get('q')
        
        # VIOLATION: No input validation
        # VIOLATION: SQL injection
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        query = f"SELECT * FROM products WHERE name LIKE '%{search_term}%'"
        cursor.execute(query)
        results = cursor.fetchall()
        
        return jsonify(results)
    except:
        # VIOLATION: Bare except
        return jsonify([])


@app.route('/api/config', methods=['POST'])
def update_config_violations():
    """🔴 MULTIPLE VIOLATIONS: Unsafe deserialization + hardcoded secrets"""
    try:
        config_data = request.get_json()
        
        # VIOLATION: Unsafe deserialization
        import pickle
        config_obj = pickle.loads(config_data['config'])
        
        # VIOLATION: Hardcoded credentials
        save_to_database(config_obj, DB_PASSWORD)
        
        return jsonify({"status": "updated"})
    except:
        # VIOLATION: Bare except
        return None


@app.route('/api/execute', methods=['POST'])
def execute_code_violations():
    """🔴 MULTIPLE VIOLATIONS: eval() + exec() + no error handling"""
    try:
        code = request.get_json()['code']
        
        # VIOLATION: eval() on user input
        result = eval(code)
        
        return jsonify({"result": result})
    except:
        # VIOLATION: Bare except
        pass


# ============================================================================
# HELPER FUNCTIONS (Stubs for demonstration)
# ============================================================================

def charge_card(amount, card_token):
    """Stub function"""
    pass


def verify_credentials(username, password):
    """Stub function"""
    pass


def process_critical_action(user_id, action):
    """Stub function"""
    pass


def log_action(user_id, action):
    """Stub function"""
    pass


def notify_user(user_id):
    """Stub function"""
    pass


def process_data(data):
    """Stub function"""
    pass


def save_to_database(config, password):
    """Stub function"""
    pass


# ============================================================================
# SUMMARY OF VIOLATIONS
# ============================================================================
"""
VIOLATION SUMMARY:

GUIDELINE 1: NO HARDCODED SECRETS
  - 5 violations: API keys, DB credentials, AWS keys, endpoints, JWT secret
  
GUIDELINE 2: NO SQL INJECTION
  - 8 violations: String concat, f-string, .format(), %, UPDATE, DELETE, LIKE
  
GUIDELINE 3: NO UNVALIDATED INPUT
  - 8 violations: Path traversal (3x), command injection (3x), CSV injection, log injection
  
GUIDELINE 4: NO UNSAFE DESERIALIZATION
  - 7 violations: pickle, yaml.load, eval, exec, getattr on pickled objects
  
GUIDELINE 5: PROPER ERROR HANDLING
  - 8 violations: Bare except clauses in critical functions and routes

TOTAL: 36+ CRITICAL VIOLATIONS
Expected CRA Suggestions: 30+ recommendations covering all guidelines
"""

if __name__ == "__main__":
    print("🔴 This file contains intentional security violations for CRA testing")
    print("🚀 CRA should generate multiple suggestions for each guideline violation")
