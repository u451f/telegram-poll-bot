# What's that thing?

This is a poll bot to ask my office peers who cooks and who wants to eat lunch.
Super precise, but maybe you can adapt it to your needs. Also… it talks
German :)

# Usage

chmod +x pollbot.py

# Set up the bot

On Telegram:

- talk to @BotFather and create a new bot
- copy token and add to .dotenv (requires python3-dotenv package) →
  or actually add that to Github secrets - this is what we work with.
- test if token works: https://api.telegram.org/botTOKEN/getMe (replace TOKEN) by actual token

## Add bot to the group or channel where it shall post the polls

- add bot to relevant group chat
- talk to @RawDataBot and find out the chat id of the group

# Documentation of poll API

- https://core.telegram.org/constructor/poll

# Specifics

The closing_date will always be automatically 8 days from the creation of the poll.

This script needs to be launched every Friday the week before (using Github), or by a cronjob.

# check for broken requirements

`python -m pip check`
