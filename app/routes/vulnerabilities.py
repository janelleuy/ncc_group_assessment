from flask import Blueprint, request
import json
from app.utils.formatters import format_response

vulnerabilities_bp = Blueprint('vulnerabilities', __name__)

@vulnerabilities_bp.route('/vulnerabilities', methods=['GET'])
def get_vulnerabilities():
    format_type = request.args.get('format', 'json')
    with open('data/vulnerabilities.json') as f:
        vulnerabilities = json.load(f)
        
    id = request.args.get('id')
    if id:
        vulnerabilities = list(filter(lambda x: x['id'] == int(id), vulnerabilities))
        
    from_scan = request.args.get('from_scan')
    if from_scan:
        vulnerabilities = list(filter(lambda x: x['from_scan'] == int(from_scan), vulnerabilities))
        
    severity = request.args.get('severity')
    if severity:
        vulnerabilities = list(filter(lambda x: x['severity'] == severity, vulnerabilities))
         
    return format_response(vulnerabilities, format_type)
