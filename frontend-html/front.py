import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

backend_service_host = os.getenv('BACKEND_SERVICE_HOST', 'backend-service')

@app.route('/')
def form():
    return render_template('form.html')

@app.route("/addrec", methods=['POST'])
def addrec():
    try:
        data = request.form.to_dict()
        response = requests.post(f'http://{backend_service_host}:5000/test', json=data)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
