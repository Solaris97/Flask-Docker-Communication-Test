from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
host_addr = "0.0.0.0"
host_port = 5000
CORS(app)

@app.route('/')
def hello():
    return 'Hello Flask World'

@app.route('/ping', methods=['POST'])
def ping():
    return {'response' : 'pong'}

if __name__ == "__main__":
    app.run(debug=True,
            host=host_addr,
            port=host_port)