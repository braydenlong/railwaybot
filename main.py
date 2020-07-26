import logging
import requests
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import re
import telepot
import os
PORT = int(os.environ.get('PORT', 5000))
# import daemon #supposed to run the bot without running the file


# from telegram_bot import TelegramBot
token = '1192184755:AAFkF7Vp3HYmMUioW-V9Ny1bFunwZep2-Os'
TelegramBot = telepot.Bot(token)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


url = "https://api.telegram.org/bot1192184755:AAFkF7Vp3HYmMUioW-V9Ny1bFunwZep2-Os"

# create func that get chat id


def start(update, context):
    reply_keyboard = [['/help', '/joke', '/enter', '/status']]
    update.message.reply_text("Hello! Welcome To Railway! How can I help you? Who are you?",
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))


def help(update, context):

    update.message.reply_text(
        "You can contact us @whysocereals or @ernestlim8 for any queries! ")


def enter(update, context):
    update.message.reply_text(
        "Here's the link to the webpage! https://railway-platform.herokuapp.com/")


def echo(update, context):
    reply_keyboard = [['/help', '/joke', '/enter', '/status']]
    update.message.reply_text("Oh no! Choose a valid command!",
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))


def get_url():

    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

    # def get_image_url():
    #     allowed_extension = ['jpg', 'jpeg', 'png']
    #     file_extension = ''
    #     while file_extension not in allowed_extension:
    #         url = get_url()
    #         file_extension = re.search("([^.]*)$", url).group(1).lower()
    #     return url


def bop(bot, update):
    # url = https://specials-images.forbesimg.com/imageserve/1143890227/960x0.jpg?fit=scale
    chat_id = update.message.chat_id
    bot.send_photo(
        chat_id=chat_id, photo=url)


def get_joke(update, context):
    """Fetch joke from the web and return."""
    url = 'https://icanhazdadjoke.com/'
    headers = {'Accept': 'application/json'}
    joke_msg = requests.get(url, headers=headers).json().get('joke')
    update.message.reply_text(joke_msg)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(
        "1192184755:AAFkF7Vp3HYmMUioW-V9Ny1bFunwZep2-Os", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("joke", get_joke))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("enter", enter))
    # dp.add_handler(CommandHandler("bop", bop))  # spoilt function
    dp.add_handler(MessageHandler(Filters.text, echo))
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
