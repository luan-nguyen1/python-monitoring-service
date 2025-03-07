from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import psutil
import socket
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/metrics', methods=['GET'])
def custom_metrics():
    metrics_data = {
        'cpu_percent': psutil.cpu_percent(),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent,
        'hostname': socket.gethostname(),
        'timestamp': time.time()
    }
    return jsonify(metrics_data)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'service': 'Python Monitoring Microservice',
        'endpoints': [
            {'path': '/metrics', 'description': 'Get custom system metrics'},
            {'path': '/health', 'description': 'Health check endpoint'},
            {'path': '/prometheus', 'description': 'Prometheus metrics'}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
