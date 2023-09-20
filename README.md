# What's that thing?

This is a poll bot to ask my office peers who cooks and who wants to eat lunch.
Super precise, but maybe you can adapt it to your needs. Also… it talks
German :)

# Usage

chmod +x pollbot.py

# Set up the bot

On Telegram:

- talk to @BotFather and create a new bot
- copy token and add to .dotenv (requires python3-dotenv package) → or
  actually add that to Github secrets (settings → secrets and variables
  → actions → Repository secrets) - this is what we work with (we need
  TOKEN and CHAT_ID)
- test if token works: https://api.telegram.org/botTOKEN/getMe (replace
  TOKEN) by actual token

## Add bot to the group or channel where it shall post the polls

- add bot to relevant group chat
- talk to @RawDataBot and find out the chat id of the group

# Documentation of poll API

- https://core.telegram.org/constructor/poll

# Launching the script

This script needs to be launched every Friday the week before. This can
be done by a cronjob or by a Github workflow (see .github/workflows for
code). We are currently using the Github workflow.

# Specifics

The closing_date will always be automatically 8 days from the creation of the poll.


# Check for broken requirements

`python -m pip check`
