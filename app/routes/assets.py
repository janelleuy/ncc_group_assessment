from flask import Blueprint, jsonify, request
import json
from app.utils.formatters import format_response

assets_bp = Blueprint('assets', __name__)

@assets_bp.route('/assets', methods=['GET'])
def get_assets():
    format_type = request.args.get('format', 'json')
    with open('data/assets.json') as f:
        assets = json.load(f)
    return format_response(assets, format_type)