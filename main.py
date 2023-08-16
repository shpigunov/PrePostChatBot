import asyncio
import logging
import os

from dotenv import load_dotenv
load_dotenv('.env')
TOKEN:str = os.getenv('BOT_TOKEN')

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message

from helpers.messenger import send_message
from helpers.shared import context

from middleware.router import router

async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()

    @dp.update.outer_middleware()
    async def main_mw(
        handler,
        event,
        data,
    ):
        print('event--------------',event)
        print('data---------------',data)

        chat_id = data['event_from_user'].id

        try:
            context[chat_id]
        except:
            context[chat_id] = {}

        try:
            user_message = event.callback_query.data
        except:
            try:
                user_message = event.message.text
            except Exception as e:
                print(e)

        if event.message:
            message = event.message
            context[chat_id]['recieved_message']=message

        
        await router(chat_id, user_message)

        # print(context)
        # !!!context['chat_id']=event.chat_id
        # await send_message('Answer to message from context')
        
        return await handler(event, data)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    context['bot'] = bot
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())