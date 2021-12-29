# Bot

This is telegram bot that is used for secret santa investor.    
Using https://github.com/python-telegram-bot/python-telegram-bot

## Before

- create file `token.txt` in  the root folder (ignored by git)
- fill it with your Telegram Bot Token

## How to start

- `pip install -r requirements.txt`
- `python3 main.py`
- that's all! bot just works

## Debug

- bot has logging enabled
- `data.json` - file where all data is stored, can be manually changed if neaded

# Result Sender

## How run

- `pip install -r requirements.txt`
- `python3 send_results.py`
- check output for errors
- press y to send data or something else to abort
