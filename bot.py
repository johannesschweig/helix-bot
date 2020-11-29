import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import os
import math
from utils import get_joke, categories_cleaned
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
# token
TOKEN = os.environ.get('TOKEN', None)

# create a keyboard with 3 categories per row
rows = []
for i in range(0, math.ceil(len(categories_cleaned)/3)):
  rows.append(categories_cleaned[i*3:(i+1)*3])
markup = ReplyKeyboardMarkup(rows)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!\nIch bin der Helix-Witz-Bot. Witze mit Niveau von Helix!')
    update.message.reply_text('Wähle eine Kategorie:', reply_markup=markup)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def joke(update, context):
    update.message.reply_text(get_joke(update.message.text), reply_markup=markup)
    
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - tell a random joke
    dp.add_handler(MessageHandler(Filters.text, joke))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://afternoon-ocean-20209.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()