from config import TOKEN
import logging
from app.bot import TelegramBot
from app.menu import BotMenu
from app.database import Database

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

if __name__ == "__main__":

    database = Database()

    bot = TelegramBot(TOKEN, database, BotMenu)
    bot.run()