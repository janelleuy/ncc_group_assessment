from flask import Blueprint, jsonify, request
import json
from app.utils.formatters import format_response

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    format_type = request.args.get('format', 'json')
    with open('data/users.json') as f:
        users = json.load(f)
    return format_response(users, format_type)