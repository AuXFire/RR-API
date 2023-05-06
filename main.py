from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/capture-request/<data>', methods=['GET', 'POST'])
def capture_request(data):
    request_data = data
    print(request_data)
    return jsonify(request_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
