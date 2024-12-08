from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Replace with your endpoint
SEARCH_API_URL = "https://plxbd.com/search.php"

# Start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! Send me a movie name, and I'll find it for you.")

# Search function
def search_movie(update: Update, context: CallbackContext) -> None:
    query = update.message.text
    try:
        response = requests.get(f"{SEARCH_API_URL}?q={query}")
        if response.status_code == 200:
            update.message.reply_text(response.text)
        else:
            update.message.reply_text("Error fetching data. Please try again.")
    except Exception as e:
        update.message.reply_text("An error occurred: " + str(e))

# Main function
def main():
    TOKEN = "7461087826:AAFDskohQ6qmo1yW5LxvY0muhaWn7JrgBSc"  # Replace with BotFather's token
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, search_movie))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
