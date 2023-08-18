import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, F, html
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from middleware.router import GameState, router
from middleware.handlers import *  # noqa: F403

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
if not TOKEN:
    sys.exit("Set BOT_TOKEN env variable")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    try:
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
