from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app, group_by='endpoint')


@app.route('/')
def fnc_hl_wrld():
    return 'Hello World'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
