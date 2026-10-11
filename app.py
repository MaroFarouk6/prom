from flask import Flask, jsonify, request
from prometheus_client import start_http_server, Counter, Gauge, Summary
from time import sleep
from random import randint   

app = Flask(__name__)
# counter = Counter('http_request', 'A simple counter')
# guage = Gauge('http_processing', 'A simple guage')
REQUEST_TIME = Summary('task_duration_seconds', 'Time spent processing request')

@app.route('/')
@REQUEST_TIME.time()
def hello_world():
    # counter.inc()
    # guage.inc()
    # sleep(30)
    # guage.dec()
    sleep(randint(1, 10))
    return 'Hello World!'

if __name__ == '__main__':
    start_http_server(8050)
    app.run(host='0.0.0.0', port=5000)