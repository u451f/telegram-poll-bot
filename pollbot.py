#!/usr/bin/python

"""
Poll bot to ask my office peers who cooks and who eats lunch.

chmod +x pollbot.py

Set up bot:
 - talk to @BotFather and create a new bot
 - copy token and add to .dotenv (requires python3-dotenv package)
 - test if that works: https://api.telegram.org/bot===token===/getMe (replace ===token===) by actual token

Add bot to group or channel (for testing)
- add bot to relevant group chat
- talk to @RawDataBot and find out the chat id of the group

Documentation of poll API:
- https://core.telegram.org/constructor/poll

The closing_date will always be automatically 8 days from the creation of the poll.

Therefore, the poll either needs to be launched manually every Friday the week
before, or by a cronjob.
"""
import os
import requests
import json
import datetime

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

base_url = "https://api.telegram.org/bot"+TOKEN+"/sendPoll"

today = datetime.date.today()
closing_date = today + datetime.timedelta(days = 8)

year, week_num, day_of_week = today.isocalendar()
next_week = str(week_num + 1)

parameters = {
    "chat_id" : CHAT_ID,
    "question" : "Kochen W"+next_week,
    "options" : json.dumps(["Mo", "Di", "Mi", "Do", "Fr"]),
    "is_anonymous" : False,
    "public_voters": True,
    "allows_multiple_answers": True,
    "close_poll": closing_date
}

parameters2 = {
    "chat_id" : CHAT_ID,
    "question" : "Essen W"+next_week,
    "options" : json.dumps(["Mo", "Di", "Mi", "Do", "Fr"]),
    "is_anonymous" : False,
    "public_voters": True,
    "allows_multiple_answers": True,
    "close_poll": closing_date
}

response = requests.get(base_url, data = parameters)
response2 = requests.get(base_url, data = parameters2)
print(response.text)
print(response2.text)
