import json
import yaml
from dicttoxml import dicttoxml
from flask import Response

def format_response(data, format_type='json'):
    if format_type == 'json':
        return Response(json.dumps(data, indent=4), mimetype='application/json')
    elif format_type == 'xml':
        return Response(dicttoxml(data).decode(), mimetype='application/xml')
    elif format_type == 'yaml':
        return Response(yaml.dump(data, default_flow_style=False), mimetype='application/x-yaml')
    else:
        raise ValueError("Unsupported format type")