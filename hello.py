from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)
# Try adding your own number to this list!
callers = {
"+14158675309": "Curious George",
"+14158675310": "Boots",
"+14158675311": "Virgil",
"+447934171645": "Mr. Paul",
}

@app.route("/")
@app.route("/index")
def index():
	"""Present the main page"""
	return """
		<html>
		<head>
		 
		  <!-- Basic Page Needs
		  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
		  <meta charset="utf-8">
		  <title>Stratton Oakmont</title>
		  <meta name="description" content="">
		  <meta name="author" content="">
		 
		  <!-- Mobile Specific Metas
		  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
		  <meta name="viewport" content="width=device-width, initial-scale=1">
		 
		  <!-- FONT
		  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
		  <link href="//fonts.googleapis.com/css?family=Raleway:400,300,600" rel="stylesheet" type="text/css">
		 
		  <!-- CSS
		  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
		  <link rel="stylesheet" href="css/normalize.css">
		  <link rel="stylesheet" href="css/skeleton.css">
		 
		  <!-- Favicon
		  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
		  <link rel="icon" type="image/png" href="images/favicon.png">
		 
		</head>
		<body>
		 
		  <!-- Primary Page Layout
		  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
		  <div class="container">
		    <div class="row">
		      <div class="one-half column" style="margin-top: 25%">
		        <h3>Stratton Oakmont </h3>
		          <img src="http://s3.amazonaws.com/FratMusic-Site-Images/assets/cover/stratton.png" />
		        <p>We are a trustworthy and experienced set of business/engineering individuals interested in making absolutely legal and morally strong business decisions to honourable business men and women working in the stockexchange market of the 80s.
		 
		We are Paul Scherer, Chris Swart, David Schott and Nial Atkin (in no particular order).</p>
		      </div>
		    </div>
		  </div>
		 
		<!-- End Document
		  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
		</body>
		</html>
			"""

@app.route("/phone", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond and greet the caller by name."""
	
	from_number = request.values.get('From', None)
	message_body = request.values.get('Body', None)
	if from_number in callers:
		message = callers[from_number] + ", thanks for the message!" + message_body
	else:
		message = "Non Stratton Oakmont Client, thanks for the message! But please sign up for our Service"

	resp = twilio.twiml.Response()
	resp.message(message)
	
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)

@app.route("/phone", methods =['GET', 'POST'])
def  callhandle():
	""" 
	Responds to different callers based on their message and
	calls then by name if they are part of the callers list.
	"""

	from_number = request.values.get('From', None)
	message_body = request.values.get('Body', None)

	if from_number in callers:
		if 
		message = "Hello " + callers[from_number] + ", thanks for the message"
	else:
		message = "Hello you are not a Stratton Oakmont Client, but thanks for the message! Please sign "