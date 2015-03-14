from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World! THIS IS STRATTON OAKMONT"

if __name__ == "__main__":
	app.run(debug=True)