import logging

from flask import Flask

logging.basicConfig(filename='../logs/flask.log',level=logging.DEBUG)

app = Flask(
	__name__,
)

@app.route('/')
def hello_world():
	logging.info("I'm a log and i work");
	return "Hello world!"