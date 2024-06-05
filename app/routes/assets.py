from flask import Blueprint, request
from app.utils.formatters import format_response
from app.utils.data_loader import load_data
from app.utils.filters import *

assets_bp = Blueprint('assets', __name__)

@assets_bp.route('/assets', methods=['GET'])
def get_assets():
    format_type = request.args.get('format', 'json')
    data = load_data('assets')
        
    id = request.args.get('id')
    if id:
        data = int_filter('id', id, data)
        
    name = request.args.get('name')
    if name:
        data =  string_filter('name', name, data)
        
    return format_response(data, format_type)