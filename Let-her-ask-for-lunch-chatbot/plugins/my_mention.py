from slackbot.bot import *
import re
import sys, os.path
sys.path.append(os.path.abspath('../'))
from emojis import *

@respond_to(r"Hello|Hi", re.IGNORECASE)
def mention_func(message):
    message.reply('Hi, I am chaitu-assistant, here to help chaitu')
    message.react(REACT_EMOJI_SUNGLASSES)


@respond_to("help", re.IGNORECASE)
def mention_func(message):
    message.reply('I am improving still, try these commands 1) Hello ')


@listen_to('assistant')
def listen_func(message):
    message.send('I always listen to your conversation, dont worry')      # send normal text message, as response
    message.reply('Am I doing correct？')                           # send reply with metioning of user tagged


@default_reply()
def default_func(message):
    message.react(REACT_EMOJI_SOB)
    message.reply('I am still learning, for now please excuse me with your question. Try command help')
