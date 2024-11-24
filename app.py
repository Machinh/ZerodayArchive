# app.py

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

def load_exploits(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    exploits = load_exploits('exploits.json')
    return render_template('index.html', exploits=exploits)

@app.route('/exploit/<int:exploit_id>')
def exploit_detail(exploit_id):
    exploits = load_exploits('exploits.json')
    exploit = next((exp for exp in exploits if exp['id'] == exploit_id), None)
    if exploit:
        return render_template('exploit_detail.html', exploit=exploit)
    return "Exploit não encontrado.", 404

if __name__ == "__main__":
    app.run(debug=True)