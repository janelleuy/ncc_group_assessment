from flask import Blueprint, request
from app.utils.formatters import format_response
from app.utils.data_loader import load_data

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    format_type = request.args.get('format', 'json')
    users = load_data('users')
        
    id = request.args.get('id')
    if id:
        users = list(filter(lambda x: x['id'] == int(id), users))
        
    username = request.args.get('username')
    if username:
        users = list(filter(lambda x: x['username'] == username, users))

    email = request.args.get('email')
    if email:
        users = list(filter(lambda x: x['email'] == email, users))
        
    first_name = request.args.get('first_name')
    if first_name:
        users = list(filter(lambda x: x['first_name'] == first_name, users))
        
    last_name = request.args.get('last_name')
    if last_name:
        users = list(filter(lambda x: x['last_name'] == last_name, users))
        
    return format_response(users, format_type)