from flask import Blueprint, request
import json
from app.utils.formatters import format_response

assets_bp = Blueprint('assets', __name__)

@assets_bp.route('/assets', methods=['GET'])
def get_assets():
    format_type = request.args.get('format', 'json')
    with open('data/assets.json') as f:
        assets = json.load(f)
        
    id = request.args.get('id')
    if id:
        assets = list(filter(lambda x: x['id'] == int(id), assets))
        
    name = request.args.get('name')
    if name:
        assets = list(filter(lambda x: x['name'] == name, assets))
        
    return format_response(assets, format_type)