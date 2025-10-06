#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request


HOST = '0.0.0.0'
PORT = 5000

USERS = {}

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!", 200


@app.route('/data')
def get_data():
    return jsonify(list(USERS.keys())), 200


@app.route('/status')
def get_status():
    response = make_response("OK", 200)
    response.headers["Content-Type"] = "text/plain"
    return response


@app.route('/users')
def get_all_users():
    return jsonify(USERS), 200


@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        user_data = request.get_json()

        if not user_data or 'username' not in user_data:
            return jsonify({"error": "Username is required"}), 400

        username = user_data['username']

        if username in USERS:
            return jsonify({"error": "User already exists"}), 400

        USERS[username] = user_data

        return jsonify({
            "message": "User added successfully",
            "user": user_data
        }), 201

    except Exception as e:
        return jsonify({"error": "Invalid request"}), 400


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Endpoint not found"}), 404)


if __name__ == '__main__':
    print(f"Starting Flask server on http://localhost:{PORT}...")
    print(f"(Accessible via {HOST}:{PORT})")

    app.run(host=HOST, port=PORT, debug=True)
