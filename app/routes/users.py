from flask import Blueprint, request
from app.utils.formatters import format_response
from app.utils.data_loader import load_data
from app.utils.filters import *

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    format_type = request.args.get('format', 'json')
    data = load_data('users')
        
    id = request.args.get('id')
    if id:
        data = int_filter('id', id, data)
        
    username = request.args.get('username')
    if username:
        data = string_filter('username', username, data)

    email = request.args.get('email')
    if email:
        data = string_filter('email', email, data)

    first_name = request.args.get('first_name')
    if first_name:
        data = string_filter('first_name', first_name, data)

    last_name = request.args.get('last_name')
    if last_name:
        data = string_filter('last_name', last_name, data)

    return format_response(data, format_type)