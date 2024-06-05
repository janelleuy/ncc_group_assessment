from flask import Blueprint, request
from app.utils.formatters import format_response
from app.utils.data_loader import load_data
from app.utils.filters import *

vulnerabilities_bp = Blueprint('vulnerabilities', __name__)

@vulnerabilities_bp.route('/vulnerabilities', methods=['GET'])
def get_vulnerabilities():
    format_type = request.args.get('format', 'json')
    data = load_data('vulnerabilities')
        
    id = request.args.get('id')
    if id:
        data = int_filter('id', id, data)
    
    from_scan = request.args.get('from_scan')
    if from_scan:
        data = int_filter('from_scan', from_scan, data)

    severity = request.args.get('severity')
    if severity:
        data = string_filter('severity', severity, data)

    return format_response(data, format_type)
