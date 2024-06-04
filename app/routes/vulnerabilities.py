from flask import Blueprint, jsonify, request
import json
from app.utils.formatters import format_response

vulnerabilities_bp = Blueprint('vulnerabilities', __name__)

@vulnerabilities_bp.route('/vulnerabilities', methods=['GET'])
def get_vulnerabilities():
    format_type = request.args.get('format', 'json')
    with open('data/vulnerabilities.json') as f:
        vulnerabilities = json.load(f)
    return format_response(vulnerabilities, format_type)