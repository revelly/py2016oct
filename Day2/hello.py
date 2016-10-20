from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/index")
def index():
	file = open("index.htm","r")
	return file.read()
	
if __name__ == "__main__":
	app.run()