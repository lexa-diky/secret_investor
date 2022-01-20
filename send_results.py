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
            "message": f"Oh ho ho. Secret Investor is here:\n{what['stock']}"
        })
        name_to = "[%s %s @%s]" % (who['first_name'], who['last_name'], who['username'])
        name_from = "[%s %s @%s]" % (what['first_name'], what['last_name'], what['username'])
        message = '#{id} {name_to} will receive "{stock}" from {name_from}'.format(
            id=idx,
            name_to=name_to,
            name_from=name_from,
            stock=what['stock'],
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
                text=entry["message"]
            )
