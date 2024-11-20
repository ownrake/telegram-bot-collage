from aiogram import F, Router
from aiogram.types import CallbackQuery

#import app.user.user_keyboards as userKB
import app.mini_games.game_keyboards as gameKB
from app.user.user_keyboards import schludeMain

gameRouter = Router()


@gameRouter.callback_query(F.data == "miniGamesCall")
async def miniGames(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("ПРивет")