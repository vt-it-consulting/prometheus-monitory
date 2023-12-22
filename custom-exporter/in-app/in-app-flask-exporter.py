from werkzeug.middleware.dispatcher import DispatcherMiddleware
import prometheus_client
import flask
import random
import time
import threading


SERVICE_UPTIME = prometheus_client.Gauge('service_uptime',
                                         'Hold the time elasted since service startup')
RESPONSE_TIME = prometheus_client.Gauge('response_time_last',
                                        'Hold the last request response time')

# Create Flask APP
app = flask.Flask(__name__)


@app.route('/')
@RESPONSE_TIME.time()
def hello():
    time.sleep(random.random())
    return "Hello World"


# Prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': prometheus_client.make_wsgi_app()
})


def update_uptime():
    while True:
        SERVICE_UPTIME.inc(1)
        time.sleep(1)


SERVICE_UPTIME.set(0)
uptime_updater = threading.Thread(target=update_uptime)
uptime_updater.start()
