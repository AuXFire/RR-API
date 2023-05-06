from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/capture-request/', methods=['GET', 'POST'])
def capture_requests():
    args = request.query_string.decode()
    if args:
        return args
    else:
        return "No query parameters were found."


@app.route('/process_data/<path:request_data>', methods=['GET'])
def process_data(request_data):
    data = json.loads(request_data)
    processed_data = {}

    for item in data:
        for key, value in item.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    new_key = f"{key}:{sub_key}"
                    processed_data[new_key] = sub_value
            else:
                processed_data[key] = value

    return jsonify(processed_data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
