# SendMessage
# SendMessageWithKeyboard
# UpdateLastMessage
# UpdateLastMessageWithKeyboard

from aiogram.types import Message
from helpers.shared import context

async def send_simple_message(text:str):
    message:Message = context['message']
    await message.answer(text)