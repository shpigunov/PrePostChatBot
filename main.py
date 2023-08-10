import asyncio
import logging
import os

from dotenv import load_dotenv
load_dotenv('.env')
TOKEN:str = os.getenv('BOT_TOKEN')

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message

from helpers.messenger import send_simple_message
from helpers.shared import context

async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()

    @dp.update.outer_middleware()
    async def main_mw(
        handler,
        event,
        data,
    ):
        context['message']=event.message
        await send_simple_message('Answer to message from env')
        
        return await handler(event, data)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


# All handlers should be attached to the Router (or Dispatcher)
# router = Router()


# @router.message(Command(commands=["start"]))
# async def command_start_handler(message: Message) -> None:
#     """
#     This handler receive messages with `/start` command
#     """
#     # Most event objects have aliases for API methods that can be called in events' context
#     # For example if you want to answer to incoming message you can use `message.answer(...)` alias
#     # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
#     # method automatically or call API method directly via
#     # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
#     await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


# @router.message()
# async def echo_handler(message: types.Message) -> None:
#     """
#     Handler will forward received message back to the sender

#     By default, message handler will handle all message types (like text, photo, sticker and etc.)
#     """
#     try:
#         # Send copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")


# async def main() -> None:
#     # Dispatcher is a root router
#     dp = Dispatcher()
#     # ... and all other routers should be attached to Dispatcher
#     dp.include_router(router)

#     # Initialize Bot instance with a default parse mode which will be passed to all API calls
#     bot = Bot(TOKEN, parse_mode="HTML")
#     # And the run events dispatching
#     await dp.start_polling(bot)
