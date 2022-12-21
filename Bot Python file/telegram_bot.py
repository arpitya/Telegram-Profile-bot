import json
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
updater = Updater("5985249377:AAEJEMKDHApvV7Q4FdSG2-bWJfpIDrCbQLw",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
            "Hello sir/Ma'am, Welcome to my Profile_Bot. Please write\
		/help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
	/Resume - To get the youtube URL
	/LinkedIn - To get the LinkedIn profile URL
	/Email - To get gmail URL
	/Github - To get the GeeksforGeeks URL""")


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "<b>Gmail<b/> => arpityasingh@gmail.com  ")


def resume(update: Update, context: CallbackContext):
    update.message.reply_text("Resume Link => shorturl.at/mor13")


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "LinkedIn URL => https://www.linkedin.com/in/arpitya-singh-239457215/")


def Github(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Github URL => https://github.com/arpitya")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('resume', resume))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('Github', Github))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
