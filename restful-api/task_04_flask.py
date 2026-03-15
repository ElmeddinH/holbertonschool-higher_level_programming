#!/usr/bin/python3
"""Simple API using Flask"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Get list of all usernames"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Status endpoint"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Get user by username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user"""
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == '__main__':
    app.run()
