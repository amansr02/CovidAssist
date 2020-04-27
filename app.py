from flask import Flask, request
from covid import CovidAssist
import datetime
import json
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
agent = CovidAssist()

@app.route('/bot', methods=['POST'])
def bot():
    # add webhook logic here and return a response
    incoming_msg = request.values.get('Body')
    resp = MessagingResponse()
    msg = resp.message()
    if "information" in incoming_msg:
        x = incoming_msg.split()
        agent.country=x[-1]
        date = agent.get_latest_date()
        date = date.text
        data = agent.get_latest_country_data()
        data = json.loads(data)
        msg.body(" confirmed = " + str(data["result"][date]["confirmed"]) + 
                " \n deaths = " + str(data["result"][date]["deaths"] + 
                " \n recoverd = " + str(data["result"][date]["recovered"]  )
    #if "information" in incoming_msg and ("chart" in incoming_msg or "charts" in incoming_msg):
    #    pass
    #else if "information" in incoming_msg:
    #    pass
    #else if "charts" incoming_msg or "chart" in incoming_msg:
    #    pass
    #else:
    #    msg.body("I didnot understand, could you mention 'information' or 'chart' please!")
    return str(resp)

if __name__ == '__main__':
    app.run()
