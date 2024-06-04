import json

def load_data(file_path):
    file_path = 'data/' + file_path + '.json'
    with open(file_path) as f:
        return json.load(f)