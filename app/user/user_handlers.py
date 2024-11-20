import asyncio

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.user.user_keyboards as kb
from app.admin.admin_handlers import startAdmin
import config as con


userRouter = Router()

user_id = None
user_name = None


@userRouter.message(CommandStart())
async def start(message: Message):
    global user_id
    global user_name

    user_id = message.from_user.id
    user_name = message.from_user.first_name

    if user_id in con.moder_id:
        await startAdmin(message)
    elif user_id not in con.moder_id:
        await message.answer("""💻 <a href = 'https://t.me/helperforgroup201is_bot'>Студенчиский платформа</a>.
Узнавайте расписание, заказывайте справки и получайте оповещение об важных события.""", 
                                    reply_markup = kb.mainMenu, 
                                    parse_mode = "HTML")
    
# -- ------------------------------------------------------------------------------------------------

@userRouter.callback_query(F.data == "schludeCall")
async def schludeCall(call: CallbackQuery):
    await call.answer("")
    await call.message.edit_text("Выберите тип расписания, который вам нужен",
                                 reply_markup = kb.schludeMain)
    
@userRouter.callback_query(F.data == "orderCertificatesCall")
async def orderCertificatesCall(call: Message):
    await call.answer("")
    await call.message.edit_text("Для заказа справок перейдите по кнопке ниже.",
                      reply_markup = kb.orderCertificates)

# -- ------------------------------------------------------------------------------------------------
@userRouter.callback_query(F.data == "goToMainMenuCall")
async def goToMainMenuCall(call: CallbackQuery):
    await call.message.edit_text("""💻 <a href = 'https://t.me/helperforgroup201is_bot'>Студенчиский платформа</a>.
Узнавайте расписание, заказывайте справки и получайте оповещение об важных события.""", 
                                    reply_markup = kb.mainMenu, 
                                    parse_mode = "HTML")


@userRouter.message()
async def echo(message: Message):
    print(f"INFO:aiogram.dispatcher:Unknow message, @{(message.from_user.first_name).lower()} say: {message.text}")
    await message.reply("Прости я тебя не понял. Используй /start")