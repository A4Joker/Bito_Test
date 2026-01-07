

import pickle
import sqlite3
import yaml
import os
from flask import Flask, request

app = Flask(__name__)


API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz"
DATABASE_URL = "postgresql://admin:Password123@db.company.com:5432/production"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
JWT_SECRET = "my-super-secret-jwt-key-12345"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
SLACK_WEBHOOK = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX"
API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz"
DATABASE_URL = "postgresql://admin:Password123@db.company.com:5432/production"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
JWT_SECRET = "my-super-secret-jwt-key-12345"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
SLACK_WEBHOOK = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX"
DB_CONFIG = {
    "host": "db.production.com",
    "user": "root",
    "password": "RootPassword@123",
    "database": "company_data"
}



def get_user_by_id_vulnerable(user_id):
  
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
   
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()

def get_user_by_email_vulnerable(email):

    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE email = '{}'".format(email)
    cursor.execute(query)
    return cursor.fetchall()

def authenticate_user_vulnerable(username, password):

    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    return user is not None


@app.route('/upload', methods=['POST'])
def upload_file_vulnerable():

    filename = request.form.get('filename')
    filepath = f"/uploads/{filename}"
    

    with open(filepath, 'wb') as f:
        f.write(request.files['file'].read())
    
    return "File uploaded successfully"

@app.route('/execute', methods=['POST'])
def execute_command_vulnerable():


    command = request.args.get('cmd')
    user_id = request.args.get('user_id')
    

    os.system(f"echo 'Processing user {user_id}' && {command}")
    
    return "Command executed"

@app.route('/process', methods=['POST'])
def process_data_vulnerable():

    age = request.form.get('age')
    quantity = request.form.get('quantity')
    

    total_price = 100 * int(age) + int(quantity)
    
    return f"Total: {total_price}"

def deserialize_user_data_vulnerable(serialized_data: bytes) -> any:
def deserialize_user_data_vulnerable(serialized_data: bytes) -> any:

    user_data = pickle.loads(serialized_data)
    return user_data

def process_config_vulnerable(config_string):

    config = eval(config_string)
    return config

def load_yaml_vulnerable(yaml_content):

    data = yaml.load(yaml_content)
    return data

def execute_template_vulnerable(template_code):

    exec(template_code)

@app.route('/api/data', methods=['POST'])
def receive_data_vulnerable():

    pickled_data = request.data
    user_data = pickle.loads(pickled_data)
    
    return "Data received"


def process_payment_vulnerable(amount, card_number):

    
    try:

        charge_amount = amount / 0  
        process_card(card_number, charge_amount)
        
    except:
 
        pass
    
    return "Payment processed"

def read_config_file_vulnerable(filename):

    
    try:
        with open(filename, 'r') as f:
            config = f.read()
    except:

        pass

    return config

def database_query_vulnerable(query):

    
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    

    result = cursor.execute(query)
    
    return result.fetchall()

def api_call_vulnerable(url, timeout=5):

    import requests
    
    try:
 
        response = requests.get(url, timeout=timeout)
        data = response.json()
        
    except:

        pass

    return data

def process_user_list_vulnerable(users):

    
    results = []
    
    for user in users:
        try:

            user_id = user['id']
            email = user['email']
            age = user['age']
            
            # Process user
            processed = process_user(user_id, email, age)
            results.append(processed)
            
        except:

            pass
    
    return results



@app.route('/super-vulnerable', methods=['POST'])
def super_vulnerable_endpoint():

    
    try:

        conn = sqlite3.connect(DATABASE_URL)
        
  
        user_id = request.form.get('user_id')
        username = request.form.get('username')
        action = request.form.get('action')
        
  
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE id = {user_id} AND username = '{username}'"
        cursor.execute(query)
        user = cursor.fetchone()
        

        serialized_data = request.form.get('data')
        data = pickle.loads(serialized_data)
        

        exec(action)
        
    except:

        pass
    
    return "Done"


def process_card(card_number, amount):
    pass

def process_user(user_id, email, age):
    pass

if __name__ == '__main__':
    app.run(debug=True)
