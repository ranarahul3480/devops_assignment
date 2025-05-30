from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

@app.route("/")
def hello():
    REQUEST_COUNT.inc()
    return "Hello from Flask!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

@app.route("/healthz")
def healthz():
    return "OK", 200

@app.route("/ready")
def ready():
    return "READY", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
