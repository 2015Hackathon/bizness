from flask import Flask, request, redirect, render_template
from current_data_dynamic import request_this
import json
import twilio.twiml
import ast

app = Flask(__name__)
# Try adding your own number to this list!
callers = {
"+447934171645": "Mr. Paul",
"+447703450135": "Mr. Nial",
}

securities = ["ACC US Equity", "GOOG US Equity", "AAPL US Equity"]

@app.route("/")
@app.route("/index")
def index():
	"""Present the main page"""
	return render_template('index.html')

# @app.route("/phone", methods=['GET', 'POST'])
# def hello_monkey():
# 	"""Respond and greet the caller by name."""
	
# 	from_number = request.values.get('From', None)
# 	message_body = request.values.get('Body', None)
# 	if from_number in callers:
# 		message = callers[from_number] + ", thanks for the message!" + message_body
# 	else:
# 		message = "Non Stratton Oakmont Client, thanks for the message! But please sign up for our Service"

# 	resp = twilio.twiml.Response()
# 	resp.message(message)
	
# 	return str(resp)

# if __name__ == "__main__":
# 	app.run(debug=True)

@app.route("/phone", methods =['GET', 'POST'])
def  callhandle():
	""" 
	Responds to different callers based on their message and
	calls then by name if they are part of the callers list.
	"""

	from_number = request.values.get('From', None)
	message_body = request.values.get('Body', None)

	if from_number in callers:
		message = "Hello " + callers[from_number] + ", thanks for the message \n"

		# Party Time
		if message_body in ["party time", "party", "p time"]:
			message = "Are you sure " + callers[from_number] + "?"
			resp = twilio.twiml.Response()
			resp.message(message)
			
			return str(resp)

		if message_body in ["oh yass", "oh yes"]:
			message = "Ok Sir, its time to party like its 1989, the current street price on the following fun stuffs is \n" + "COCO = $30/g\n" + "Chocolate Milk = $3\n" + "Silly String = $3\n"
			resp = twilio.twiml.Response()
			resp.message(message)
			
			return str(resp)

		if message_body in ["yes"]:
			message = "Ok Sir, its time to party like it 1989, the current street price on the following fun stuffs in \n" + "Chocolate = $0.03/g\n" + "Chocolate Milk = $3\n" + "Ethanol = $0.05/l\n"

		# Bloomberg API section
		if message_body in securities:
			bloomberg_json = request_this([message_body],["PX_LAST"])
			bloomberg_dict = ast.literal_eval(bloomberg_json)
			bloomberg_info = str(bloomberg_dict["data"][0]["securityData"][0]["fieldData"]["PX_LAST"])


			message = message + "You have requested the last price on: " + message_body + " here you go: " + bloomberg_info + " have a wonderful day."
			resp = twilio.twiml.Response()
			resp.message(message)
			
			return str(resp)
		else: 
			message = message + "You have requested information on a stock that does not exist, or one we do not have information on currently"
			resp = twilio.twiml.Response()
			resp.message(message)
			
			return str(resp)
	
	else:
		message = "Hello non Stratton Oakmont Client, thanks for the message!\n"
		
		# Bloomberg API section
		if message_body in securities:
			bloomberg_json = request_this([message_body],["PX_LAST"])
			bloomberg_dict = ast.literal_eval(bloomberg_json)
			bloomberg_info = str(bloomberg_dict["data"][0]["securityData"][0]["fieldData"]["PX_LAST"])


			message = message + "You have requested the last price on: " + message_body + " here you go: " + bloomberg_info + " have a wonderful day." + " Please sign up with one of our members if you want to use our venerable service - Stratton Oakmont 1989"
			resp = twilio.twiml.Response()
			resp.message(message)
			
			return str(resp)
		else: 
			message = message + "You have requested information on a stock that does not exist, or one we do not have information on currently.\n" + "Please sign up with one of our members if you want to use our venerable service - Stratton Oakmont 1989"
			resp = twilio.twiml.Response()
			resp.message(message)
			
			return str(resp)


		resp = twilio.twiml.Response()
		resp.message(message)
		
		return str(resp)