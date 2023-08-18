import logging
from entities.ensureUserExists import ensureUserExists

from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from .router import GameState, router

"""

@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(GameState.name)

    await message.answer(
        "Hi there! What's your name?",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:

    # Allow user to cancel any action


    current_state = await state.get_state()

    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)

    await state.clear()

    await message.answer(
        "Cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(GameState.name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)

    await state.set_state(GameState.like_bots)

    await message.answer(
        f"Nice to meet you, {html.quote(message.text)}!\nDid you like to write bots?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Yes"),
                    KeyboardButton(text="No"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(GameState.like_bots, F.text.casefold() == "no")
async def process_dont_like_write_bots(message: Message, state: FSMContext) -> None:
    data = await state.get_data()

    await state.clear()

    await message.answer(
        "Not bad not terrible.\nSee you soon.",
        reply_markup=ReplyKeyboardRemove(),
    )

    await show_summary(message=message, data=data, positive=False)


@router.message(GameState.like_bots, F.text.casefold() == "yes")
async def process_like_write_bots(message: Message, state: FSMContext) -> None:
    await state.set_state(GameState.language)

    await message.reply(
        "Cool! I'm too!\nWhat programming language did you use for it?",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(GameState.like_bots)
async def process_unknown_write_bots(message: Message) -> None:
    await message.reply("I don't understand you :(")


@router.message(GameState.language)
async def process_language(message: Message, state: FSMContext) -> None:
    data = await state.update_data(language=message.text)

    await state.clear()

    if message.text.casefold() == "python":
        await message.reply(
            "Python, you say? That's the language that makes my circuits light up! 😉"
        )

    await show_summary(message=message, data=data)


async def show_summary(
    message: Message, data: Dict[str, Any], positive: bool = True
) -> None:
    name = data["name"]

    language = data.get("language", "<something unexpected>")

    text = f"I'll keep in mind that, {html.quote(name)}, "

    text += (
        f"you like to write bots with {html.quote(language)}."
        if positive
        else "you don't like to write bots, so sad..."
    )

    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
"""

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(GameState.Start)
    ensureUserExists(message.from_user.full_name, message.from_user.id)
    
    await message.answer(
        "Hi there! Welcome to the game!",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("quit"))
async def quit_handler(message: Message, state: FSMContext) -> None:
    # Allow user to cancel any action

    current_state = await state.get_state()

    if current_state is None:
        return

    logger.info("Cancelling state %r", current_state)

    await state.clear()

    await message.answer(
        "Goodbye!",
        reply_markup=ReplyKeyboardRemove(),
    )


async def begin_game_handler(message: Message, state: FSMContext) -> None:
    pass


def lobby_handler(message: Message, state: FSMContext) -> None:
    pass


def game_create_handler(message: Message, state: FSMContext) -> None:
    pass


def in_round_handler(message: Message, state: FSMContext) -> None:
    pass


def round_result_handler(message: Message, state: FSMContext) -> None:
    pass


def game_result_handler(message: Message, state: FSMContext) -> None:
    pass
