

from lib2to3.pgen2 import token
from twilio.rest import Client
import os 
from pprint import pprint
from gtts import gTTS
import requests
import json



# https://www.geeksforgeeks.org/send-text-messages-to-any-mobile-number-using-fast2sms-api-in-python/?ref=lbp
"""
Sending Text Messages using twilio
    Seding customers like never 

REQUIREMENT.
Create a twilio account    
Create a phone number
Install twilio
pip install twilio
Account SID: export ACCOUNT_SID
uth Token: export AUTH_TOKEN
"""

# Create a client object. 

# Sending Text Messages 
"""
client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    to = "2024288812",
    from_= TWILIO_NUMBER,
    body= "This message is comming from kojitechs\nPlease your payment is due",
)

print(message.sid)

"""

# Sending TEXT MESSAGES FUNCTION

def sending_sending(to, message):
    try:
        ACCOUNT_SID = os.environ['ACCOUNT_SID'] 
        AUTH_TOKEN = os.environ['AUTH_TOKEN']
        TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        call = client.messages.create(
        to = to,
        from_= TWILIO_NUMBER,
        body= message,
        )
        print(call.sid)
    except Exception as e:
        print(e)
    return None    



# Now we are all set to write a sample program that converts text to speech
"""  
# The text that you want to convert to audio
mytext = 'Welcome to kojitechs everyone'
  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("audioplayer/welcome.mp3")
  
# Playing the converted file
os.system("mpg321 audioplayer/welcome.mp3")

"""
def reading_text(message):
    try:
        mytext = message
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("audioplayer/welcome.mp3")
        os.system("mpg321 audioplayer/welcome.mp3")
    except Exception as e:
        print(e)    

# Sending slack message

def sedning_slack(message):
    try:
        webhook = os.environ.get("slack_token")
        client = WebClient(token=webhook)
        response = client.chat_postMessage(channel='#random', text= message)
    
    except SlackApiError as e:
        print("Invalid token")
    else:
        print("Sedning slack messages")   
              
sedning_slack("this is from koji")
      