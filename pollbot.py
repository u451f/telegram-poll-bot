#!/usr/bin/python

"""
Telegram polling using a bot
"""

import os
import json
import datetime
import requests

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

year, WEEK_NUM, day_of_week = today.isocalendar()
if WEEK_NUM == 52:
    WEEK_NUM = 0
NEXT_WEEK = str(WEEK_NUM + 1)

parameters = {
    "chat_id" : CHAT_ID,
    "question" : "Kochen W"+NEXT_WEEK,
    "options" : json.dumps([
                "Montag",
                "Dienstag",
                "Mittwoch",
                "Donnerstag",
                "Freitag",
                "nur Ergebnisse sehen"
                ]),
    "is_anonymous" : False,
    "public_voters": True,
    "allows_multiple_answers": True,
    "close_poll": closing_date
}

parameters2 = {
    "chat_id" : CHAT_ID,
    "question" : "Essen W"+NEXT_WEEK,
    "options" : json.dumps([
                "Montag",
                "Dienstag",
                "Mittwoch",
                "Donnerstag",
                "Freitag",
                "nur Ergebnisse sehen"
                ]),
    "is_anonymous" : False,
    "public_voters": True,
    "allows_multiple_answers": True,
    "close_poll": closing_date
}

response = requests.get(base_url, data = parameters, timeout=60)
response2 = requests.get(base_url, data = parameters2, timeout=60)
#print(response.text)
#print(response2.text)
