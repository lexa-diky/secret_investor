import json
import random

from telegram import Bot
from telegram.ext import Updater, Dispatcher

with open("data.json", "r") as file:
    raw_data = json.load(file)
    clean_data = dict()
    for entry in raw_data:
        clean_data[entry["chat_id"]] = entry

    sender_keys = list(clean_data.keys())
    random.shuffle(sender_keys)
    receiver_keys = list(reversed(sender_keys))

    send_data = list()
    for idx, receiver_key in enumerate(sender_keys):
        who = clean_data[receiver_key]
        what = clean_data[receiver_keys[idx]]
        send_data.append({
            "chat_id": int(who["chat_id"]),
            "messsage": f"Oh ho ho. Secret Investor is here:\n{what['stock']}"
        })
        print(who["first_name"], who["last_name"], "gets", who["first_name"], what["stock"])

    yes = input("Commit to this result? (y/n)\n")
    if yes == "y":
        print("ok, sending...")
        updater = Updater(token="TODO")
        bot: Bot = updater.bot
        for entry in send_data:
            bot.send_message(
                chat_id=entry["chat_id"],
                text=entry["messsage"]
            )
