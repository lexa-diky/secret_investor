import json
import logging
import os.path

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

from create_updater import create_updater

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def save_entry(first_name, last_name, username, chat_id, stock):
    if not os.path.exists("data.json"):
        with open("data.json", "w") as file:
            file.write("[]")  # empty json

    with open("data.json", 'r') as file:
        data = json.load(file)

        data.append({
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "chat_id": chat_id,
            "stock": stock
        })
    with open("data.json", 'w') as file:
        json.dump(data, file, ensure_ascii=False)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Oh hohoho! Hello there, secret trader. Please, send me name of stock you want your reciver to buy (e.g. APPL 1000$ x 2 = 2000$)")


def update_paper(update, context):
    save_entry(first_name=update.effective_chat.first_name, last_name=update.effective_chat.last_name,
               username=update.effective_chat.username, chat_id=update.effective_chat.id, stock=update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Oh hohoho! Good choice you have there, I will save it. You can change it by sending me name of the stock again")


def rofl(update, context):
    logging.error("bot error", context.error)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Oh nononono! Some error happened...")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="https://www.youtube.com/watch?v=vTIIMJ9tUc8&list=PL8YDBoBkBP-b1E8ID91t29CwO4gRC8yzW&index=209")


updater = create_updater()
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
update_paper_handler = MessageHandler(Filters.text & (~Filters.command), update_paper)
rofl_handler = CommandHandler("rofl", rofl)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(update_paper_handler)
dispatcher.add_handler(rofl_handler)
dispatcher.add_error_handler(rofl)

updater.start_polling()
