#!/usr/bin/python3
"""
Flask API with Basic Authentication and JWT Authentication
Implements role-based access control
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configuration
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'
jwt = JWTManager(app)

# User data stored in memory
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Auth"""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle fresh token requirement"""
    return jsonify({"error": "Fresh token required"}), 401


# Routes

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication"""
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to obtain JWT token"""
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data['username']
    password = data['password']

    # Check if user exists and password is correct
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create JWT token with user role embedded
    additional_claims = {"role": users[username]['role']}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )

    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route using JWT Authentication"""
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted", "user": current_user}), 200


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Protected route accessible only to admin users"""
    # Get the JWT claims
    claims = get_jwt()
    role = claims.get('role', None)

    # Check if user has admin role
    if role != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    current_user = get_jwt_identity()
    return jsonify({"message": "Admin Access: Granted", "user": current_user}), 200


if __name__ == '__main__':
    app.run()