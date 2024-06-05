from flask import Blueprint, request
from app.utils.formatters import format_response
from app.utils.data_loader import load_data
from app.utils.filters import *

scans_bp = Blueprint('scans', __name__)

@scans_bp.route('/scans', methods=['GET'])
def get_scans():
    format_type = request.args.get('format', 'json')
    data = load_data('scans')
        
    id = request.args.get('id')
    if id:
        data = int_filter('id', id, data)
        
    requested_by = request.args.get('requested_by')
    if requested_by:
        data = int_filter('requested_by', requested_by, data)
        
    status = request.args.get('status')
    if status:
        data = string_filter('status', status, data)
        
    return format_response(data, format_type)