from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond to incoming calls with a simple text message."""
	resp = twilio.twiml.Response()
	with resp.message("Hello, Mobile Monkey") as m:
	m.media("http://i.imgur.com/O2NQNvP.jpg")
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)