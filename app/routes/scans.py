from flask import Blueprint, request
from app.utils.formatters import format_response
from app.utils.data_loader import load_data

scans_bp = Blueprint('scans', __name__)

@scans_bp.route('/scans', methods=['GET'])
def get_scans():
    format_type = request.args.get('format', 'json')
    scans = load_data('scans')
        
    id = request.args.get('id')
    if id:
        scans = list(filter(lambda x: x['id'] == int(id), scans))
        
    requested_by = request.args.get('requested_by')
    if requested_by:
        scans = list(filter(lambda x: x['requested_by'] == int(requested_by), scans))
        
    status = request.args.get('status')
    if status:
        scans = list(filter(lambda x: x['status'] == status, scans))
        
    return format_response(scans, format_type)