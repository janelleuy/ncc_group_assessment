from flask import Blueprint, jsonify, request
import json
from app.utils.formatters import format_response

scans_bp = Blueprint('scans', __name__)

@scans_bp.route('/scans', methods=['GET'])
def get_scans():
    format_type = request.args.get('format', 'json')
    with open('data/scans.json') as f:
        scans = json.load(f)
    return format_response(scans, format_type)