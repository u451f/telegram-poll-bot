#!/usr/bin/python

import os
import requests
import json
import datetime

try:
    TOKEN = os.environ['TOKEN']
except KeyError:
    TOKEN = "Token not available!"

try:
    CHAT_ID = os.environ['CHAT_ID']
except KeyError:
    CHAT_ID = "Chat ID not available!"

base_url = "https://api.telegram.org/bot"+TOKEN+"/sendPoll"

today = datetime.date.today()
closing_date = today + datetime.timedelta(days = 8)

year, week_num, day_of_week = today.isocalendar()
if(week_num == 52):
    week_num = 0
next_week = str(week_num + 1)

parameters = {
    "chat_id" : CHAT_ID,
    "question" : "Kochen W"+next_week,
    "options" : json.dumps(["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "nur Ergebnisse sehen"]),
    "is_anonymous" : False,
    "public_voters": True,
    "allows_multiple_answers": True,
    "close_poll": closing_date
}

parameters2 = {
    "chat_id" : CHAT_ID,
    "question" : "Essen W"+next_week,
    "options" : json.dumps(["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "nur Ergebnisse sehen"]),
    "is_anonymous" : False,
    "public_voters": True,
    "allows_multiple_answers": True,
    "close_poll": closing_date
}

response = requests.get(base_url, data = parameters)
response2 = requests.get(base_url, data = parameters2)
#print(response.text)
#print(response2.text)
