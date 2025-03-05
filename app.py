from flask import Flask, jsonify
import psutil
import os
import socket
import time

app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def get_metrics():
    metrics = {
        'cpu_percent': psutil.cpu_percent(),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent,
        'hostname': socket.gethostname(),
        'timestamp': time.time()
    }
    return jsonify(metrics)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'service': 'Python Monitoring Microservice',
        'endpoints': [
            {'path': '/metrics', 'description': 'Get system metrics'},
            {'path': '/health', 'description': 'Health check endpoint'}
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)