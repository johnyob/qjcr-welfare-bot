from collections import namedtuple
import traceback
import json

import logging


class BotException(Exception):
    pass


def read_json(file):
    try:
        with open(file) as f:
            return json.load(f, object_hook=lambda d: namedtuple("JSON_OBJ", d.keys())(*d.values()))
    except Exception as e:
        raise BotException(e)


def error(err):
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    logging.error(('```py\n{1}{0}: {2}\n```').format(type(err).__name__, _traceback, err))
    return ":warning: An error occured... :("