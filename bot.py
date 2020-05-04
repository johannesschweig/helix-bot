import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import random  # for random select
import json # to read joke file
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
with open('token.txt', 'r') as f:
  TOKEN = f.readlines()[0]

# jokes
jokes = json.load(open('jokes.json'))

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def joke(update, context):
    # Tell user a joke out of categories (if he/she knows them; otherwise just the bad ones) 
    usi = update.message.text.lower()
    if (usi == 'frau' or usi == 'frauen'):
      update.message.reply_text(random.choice(jokes['Frau']))
    elif (usi == 'mann' or usi == 'männer'):
      update.message.reply_text(random.choice(jokes['Mann']))
    elif (usi == 'schwarz'):
      update.message.reply_text(random.choice(jokes['Schwarz']))
    elif (usi == 'bedenklich'):
      update.message.reply_text(random.choice(jokes['Bedenklich']))
    else:
      update.message.reply_text(random.choice(jokes['Flach']))

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