from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from helpers.shared import context

def button_builder(buttons, order):
    builder = InlineKeyboardBuilder()
    
    for button in buttons:
        builder.button(text=button['text'], callback_data=button['command'])
    
    builder.adjust(*order)

    return builder.as_markup()

async def send_message(text:str, chat_id, buttons=None, order=None):
    bot = context['bot']
    

    if buttons != None and order != None:
        markup = button_builder(buttons, order)
        sent_message = await bot.send_message(chat_id, text, reply_markup=markup)
    else:
        sent_message = await bot.send_message(chat_id, text)
    
    context[chat_id]['last_sent_message'] = sent_message

    print('sent_message:_______________________', sent_message)
        
async def update_last_message(text:str, chat_id, buttons=None, order=None):
    bot = context['bot']
    message_id = context[chat_id]['last_sent_message'].message_id

    if buttons != None and order != None:
        markup = button_builder(buttons, order)
        await bot.edit_message_text(text, chat_id, message_id, reply_markup=markup)
    else:
        await bot.edit_message_text(text, chat_id, message_id)
