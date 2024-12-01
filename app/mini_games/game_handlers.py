import logging
import random

from aiogram import F, Router
from aiogram.types import CallbackQuery

import app.database.requests as rq
import app.mini_games.game_keyboards as kb

game_router = Router()


@game_router.callback_query(F.data.in_(["mini_games", "back_main_menu_game"]))
async def mini_games(call: CallbackQuery):
    await call.message.edit_text("Выбери мини-игру.", reply_markup=kb.main_menu_game)


@game_router.callback_query(F.data.in_(["rsp_game", "back_rsp_game"]))
async def rsp_game(call: CallbackQuery):
    await call.message.edit_text("Выбери камень/ножницы/бумагу.", reply_markup=kb.rsp_choice)

    @game_router.callback_query(F.data.in_(["rock", "scissors", "paper"]))
    async def rock(call: CallbackQuery):
        choice_user = call.data
        choice_bot = random.choice(["rock", "scissors", "paper"])

        if choice_user == choice_bot:
            result = f"Ничья! Оба выбрали {choice_user}"
        elif (choice_user == "rock" and choice_bot == "scissors") or \
            (choice_user == "scissors" and choice_bot == "paper") or \
            (choice_user == "paper" and choice_bot == "rock"):
            result = f"Вы выиграли! Ваш {choice_user} уничтожает {choice_bot}"
            await rq.add_point(call.from_user.id)
        else:
            result = f"Вы проиграли! Ваш {choice_user} слабее {choice_bot}"
            await rq.del_point(call.from_user.id)

        await call.message.edit_text(f"{result}\n\nЕще раз или хватит?", reply_markup=kb.rsp_end)