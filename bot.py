from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

class TelegramBot:

    """
    Default telegram bot instance that works with its own menu and db (for testing purposes)
    """

    def __init__(self, token, database, menu):
        self.application = ApplicationBuilder().token(token).build()
        self.db = database
        self.menu = menu()
        self.setup_handlers()

    def setup_handlers(self):
        for command, function, _ in self.menu.get_handler_entries():  # getting list of command executions
            self.application.add_handler(CommandHandler(command, function))
            
        self.application.add_handler(MessageHandler(filters.COMMAND, self.default_message))  # default
        self.application.add_error_handler(self.error_handler) # errors

    async def default_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("I didn't understand that command. Use /help for assistance.")

    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f"An error occurred: {context.error}")

    def run(self):
        self.application.run_polling()