from helpers.messenger import send_message, update_last_message

from router import GameState


async def start_handler(state: GameState, message: str, context: dict):
    if message == "/help":
        # TODO: read help message from a file?
        help_message = "I am a help message!"
        await send_message(help_message, context["chat_id"])
        return GameState.Start
    elif message == "/play":
        await send_message("Вітаємо у чат боті!", context["chat_id"])
        return GameState.BeginGame
    else:
        await send_message(
            "Не розумію вашої відповіді. Спробуйте ще раз.", context["chat_id"]
        )
        return GameState.Start


async def begin_game_handler(state: GameState, message: str, context: dict):
    pass


async def lobby_handler(state: GameState, message: str, context: dict):
    pass


async def game_create_handler(state: GameState, message: str, context: dict):
    pass


async def in_round_handler(state: GameState, message: str, context: dict):
    pass


async def round_result_handler(state: GameState, message: str, context: dict):
    pass


async def game_result_handler(state: GameState, message: str, context: dict):
    pass
