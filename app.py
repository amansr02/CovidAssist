from flask import Flask, request
from covid import CovidAssist
import pycountry
import requests_cache
import datetime
import json
import requests
import os
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
agent = CovidAssist()
requests_cache.install_cache(cache_name='covid_cache', backend='sqlite', expire_after=86400)

@app.route('/bot', methods=['POST'])
def bot():
    # add webhook logic here and return a response
    # keys = authenticate()
    incoming_msg = request.values.get('Body')
    response = message_parser(incoming_msg)
    return response

def authenticate():
    ACCOUNT_SID = ""
    AUTH_TOKEN = ""
    with open("auth.txt","r") as f:
        return  [str(el).strip("\n") for el in f.readlines()]

def message_parser(incoming_msg):
    resp = MessagingResponse()
    msg = resp.message()
    if "information" in incoming_msg or "Information" in incoming_msg:
        agent.country=country_parser(incoming_msg)
        date = agent.get_latest_date()
        date = date.text
        data = agent.get_latest_country_data()
        data = json.loads(data)
        msg.body(" COVID-19 Cases in : "+ str(agent.country)+ 
                " \n Date Updated : " + str(date)+
                " \n\n \U0001F449 confirmed = " + str(data["result"][date]["confirmed"]) + 
                " \n \U0001F449 deaths = " + str(data["result"][date]["deaths"]) + 
                " \n \U0001F449 recoverd = " + str(data["result"][date]["recovered"]))
    elif "charts" in incoming_msg or "chart" in incoming_msg:
        pass
    else:
        msg.body("I didnot understand, could you mention 'information' or 'chart' please!")

    return str(resp)

def country_parser(incoming_msg):
    x = incoming_msg.split()
    country = pycountry.countries.search_fuzzy(x[-1])[0].alpha_3
    return country

if __name__ == '__main__':
    app.run()

