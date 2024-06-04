from flask import Blueprint, request
from app.utils.formatters import format_response
from app.utils.data_loader import load_data

assets_bp = Blueprint('assets', __name__)

@assets_bp.route('/assets', methods=['GET'])
def get_assets():
    format_type = request.args.get('format', 'json')
    assets = load_data('assets')
        
    id = request.args.get('id')
    if id:
        assets = list(filter(lambda x: x['id'] == int(id), assets))
        
    name = request.args.get('name')
    if name:
        assets = list(filter(lambda x: x['name'] == name, assets))
        
    return format_response(assets, format_type)