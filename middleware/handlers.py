from router import GameState


async def start_handler(state: GameState, message: str, context: dict):
    pass


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
