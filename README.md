Poll bot to ask my office peers who cooks and who eats lunch.

Usage: chmod +x pollbot.py

Set up bot:
 - talk to @BotFather and create a new bot
 - copy token and add to .dotenv (requires python3-dotenv package)
 - test if that works: https://api.telegram.org/bot===token===/getMe (replace ===token===) by actual token

Add bot to group or channel:
- add bot to relevant group chat
- talk to @RawDataBot and find out the chat id of the group

Documentation of poll API:
- https://core.telegram.org/constructor/poll

The closing_date will always be automatically 8 days from the creation of the poll.

Therefore, this script needs to be launched every Friday the week
before, or by a cronjob.
