import os

from telegram.ext import Updater


def create_updater() -> Updater:
    file_name = 'token.txt'
    if not os.path.exists(file_name):
        raise NameError('Create file %s and put token into it' % file_name)
    with open(file_name) as f:
        contents = f.read()
        return Updater(token=contents)
