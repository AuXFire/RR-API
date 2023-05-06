from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/capture-requests/<path:data>', methods=['GET'])
def capture_requests(data):
    username = request.args.get('action')
    password = request.args.get('password')
    
    if not action:
        return jsonify({'data': data})
    
    return jsonify(data)


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
