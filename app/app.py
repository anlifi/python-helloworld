from flask import Flask
from flask import json
import logging

app = Flask(__name__)

# logging.basicConfig(filename="app.log", format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s', level=logging.DEBUG)   # only logs to file, but not console
handler = logging.FileHandler("app.log")
formatter = logging.Formatter(f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

@app.route("/status")
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype="application/json"
    )

    app.logger.info("Status request successfull")
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype="application/json"
    )

    app.logger.info("Metrics request successfull")
    return response

@app.route("/")
def hello():
    app.logger.info("Main request successfull")

    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6111)
