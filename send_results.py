import json
import random

from telegram import Bot

from create_updater import create_updater

with open("data.json", "r") as file:
    raw_data = json.load(file)
    clean_data = dict()
    for entry in raw_data:
        clean_data[entry["chat_id"]] = entry

    sender_keys = list(clean_data.keys())
    random.shuffle(sender_keys)
    # receivers will be same as senders, but shifted one left
    # e.g 1, 2, 3 -> 2, 3, 1
    receiver_keys = list(sender_keys)
    receiver_keys.append(receiver_keys.pop(0))

    send_data = list()
    for idx, receiver_key in enumerate(sender_keys):
        who = clean_data[receiver_key]
        what = clean_data[receiver_keys[idx]]
        send_data.append({
            "chat_id": int(who["chat_id"]),
            "messsage": f"Oh ho ho. Secret Investor is here:\n{what['stock']}"
        })
        message = '[{to_first_name} {to_last_name}] will receive "{stock}" from [{from_first_name} {from_last_name}]' \
            .format(
                to_first_name=who['first_name'],
                to_last_name=who['last_name'],
                stock=what['stock'],
                from_first_name=what['first_name'],
                from_last_name=what['last_name'],
            )
        print(message)

    yes = input("Commit to this result? (y/n)\n")
    if yes == "y":
        print("ok, sending...")
        updater = create_updater()
        bot: Bot = updater.bot
        for entry in send_data:
            bot.send_message(
                chat_id=entry["chat_id"],
                text=entry["messsage"]
            )
