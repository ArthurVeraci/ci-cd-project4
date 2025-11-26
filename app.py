from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Aplicação Flask"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json or {}
    return jsonify({"you_sent": data}), 200

@app.route("/slow")
def slow():
    # endpoint para testar latência
    time.sleep(0.2)
    return jsonify({"ok": True})
