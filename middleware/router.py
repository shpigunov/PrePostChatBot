# import handlers  # імпорт повністю
from aiogram import Router
from aiogram.fsm.state import State, StatesGroup

# ROUTER = {
#     GameState.NotStarted: handlers.start_handler,
#     GameState.Start: handlers.start_handler,
#     GameState.BeginGame: handlers.begin_game_handler,
#     GameState.GameCreate: handlers.game_create_handler,
#     GameState.Lobby: handlers.lobby_handler,
#     GameState.InRound: handlers.in_round_handler,
#     GameState.RoundResult: handlers.round_result_handler,
#     GameState.GameResult: handlers.game_result_handler,
# }

router = Router()


class GameState(StatesGroup):
    NotStarted = State()
    Start = State()
    BeginGame = State()
    Lobby = State()
    GameCreate = State()
    InRound = State()
    RoundResult = State()
    GameResult = State()
