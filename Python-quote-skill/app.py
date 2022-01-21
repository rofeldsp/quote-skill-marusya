from random import randrange
from flask import Flask
from flask import request
from datetime import datetime
import requests
import re

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("\nrequest.data={}".format(request.data))
    return request.data
# @app.route("/webhook", methods=['POST', 'GET'])
# def getQuote():
#     request_data = request.json
#     response = requests.post("http://api.forismatic.com/api/1.0/", data={'method': 'getQuote', 'format': 'json', 'key': randrange(1000000)})
#     data = response.json()
#     response_message = {
#         "response": {
#             "text": data.get("quoteText") + "\n\n " + data.get("quoteAuthor") if data.get("quoteAuthor") != "" else "",
#             "tts": data.get("quoteText") + "\n\n " + data.get("quoteAuthor") if data.get("quoteAuthor") != "" else "",
#             "end_session": False
#         },
#         "session": request_data.get("session"),
#         "version": request_data.get("version")
#     }
#     print(response_message);
#     return response_message;

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content