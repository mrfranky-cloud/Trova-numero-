import os
from telegram.ext import Updater, CommandHandler

# Inserisci qui il tuo token del bot di Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update, context):
    update.message.reply_text("Ciao! Il bot è attivo.")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
