from telegram import Update
from telegram.ext import ContextTypes

class DefaultMenu:

    """
    Default menu instance. Autogenerates help and start messages. Expects to be initialised in child
    """

    def __init__(self):
        self._entries = []
        self.add_entry("help", self.help, "Shows this text")
        self.add_entry("start", self.start, "Shows start text")
    
    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_text = "Available commands:"
        for command, _, description in self._entries:
            help_text += f"\n/{command} - {description}"

        await update.message.reply_text(help_text)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Default start reply. Call /help for commandlist")

    def add_entry(self, command, function, description):
        bound_function = function.__get__(self, self.__class__)
        self._entries.append((command, bound_function, description))

    def get_handler_entries(self):
        return self._entries
    

class BotMenu(DefaultMenu):

    def __init__(self):
        super().__init__()
        
        self.add_entry("horse", self.horse_shit, "Writes in horse language")
        self.add_entry("morse", self.morse_code, "Writes in morse code")

    async def horse_shit(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hrrrphh")

    async def morse_code(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(".... . .-.. .-.. ---")

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Botting scene warm welcome!")