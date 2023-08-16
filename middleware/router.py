from helpers.shared import context
from helpers.messenger import send_message, update_last_message



async def router(chat_id, user_message):

    # if user_message == '/start'

    buttons1 = [{'text':'BTN', 'command':'btn'},{'text':'BUTTON', 'command':'button'},{'text':'BUTTON 2', 'command':'button3'}]
    buttons2 = [{'text':'BTN 5', 'command':'btn'},{'text':'BUTTON 6', 'command':'button'},{'text':'BUTTON 7', 'command':'button3'}]
    order = [1,2]

    await send_message('test 2', chat_id, buttons1, order)
    await update_last_message('test 5', chat_id, buttons2, order)
    return