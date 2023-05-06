from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/capture-request/<data>', methods=['GET', 'POST'])
def capture_request(data):
    request_data = data
    print(request_data)
    return jsonify(request_data)


@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()
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
