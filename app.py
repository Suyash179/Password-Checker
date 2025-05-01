from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    strength = 5 - sum(errors)
    return strength

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')
    strength = check_password_strength(password)
    if strength == 5:
        message = "Strong Password"
        color = "green"
    elif strength >= 3:
        message = "Moderate Password"
        color = "orange"
    else:
        message = "Weak Password"
        color = "red"
    return jsonify({'message': message, 'color': color})

# No app.run() here, Vercel handles serving
