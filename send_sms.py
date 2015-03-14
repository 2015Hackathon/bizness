from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC32a3c49700934481addd5ce1659f04d2"
auth_token = "ACbafba7fad2737f6e521740284014349f"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Jenny please?! I love you <3", to="++447934171645", from_="+441669912029") # Replace with your Twilio number

print (message.sid)

# http://twimlets.com/echo?Twiml=%3CResponse%3E%3CSms%3EThe+Price+of+Coffee+is+%24503031%3C%2FSms%3E%3C%2FResponse%3E