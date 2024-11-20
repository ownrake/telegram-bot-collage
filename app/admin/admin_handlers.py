from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

import config as con
import app.database.requests as rq
import app.admin.admin_keyboards as kb
import app.user.user_keyboards as userKB


adminRouter = Router()


async def startAdmin(message: Message):
    global user_id
    global user_name

    user_id = message.from_user.id
    user_name = message.from_user.first_name

    await message.answer("""💻 <a href = 'https://t.me/helperforgroup201is_bot'>Студенчиский платформа</a>.
Узнавайте расписание, заказывайте справки и получайте оповещение об важных события.""", 
                                    reply_markup = kb.mainMenuAdmin, 
                                    parse_mode = "HTML")
    
# -- ------------------------------------------------------------------------------------------------

'''@adminRouter.callback_query(F.data == "schludeCallAdmin")
async def schludeCallAdmin(call: CallbackQuery):
    await call.answer("")
    await call.message.edit_text("Выберите тип расписания, который вам нужен",
                                 reply_markup = kb.schludeMainAdmin)
    
@adminRouter.callback_query(F.data == "orderCertificatesCallAdmin")
async def orderCertificatesCallAdmin(call: Message):
    await call.answer("")
    await call.message.edit_text("Для заказа справок перейдите по кнопке ниже.",
                      reply_markup = kb.orderCertificatesAdmin)
    
# "miniGamesCallAdmin" in games_handlers

@adminRouter.callback_query(F.data == "profileCallAdmin")
async def profileCallAdmin(call: CallbackQuery):
    await call.answer("")
    await call.message.edit_text(f"""👤 @{user_id.lower()}""")'''
    
# -- ------------------------------------------------------------------------------------------------

@adminRouter.callback_query(F.data == "goToMainMenuCallAdmin")
async def goToMainMenuCallAdmin(call: CallbackQuery):
    await call.answer("")
    await call.message.edit_text("""💻 <a href = 'https://t.me/helperforgroup201is_bot'>Студенчиский платформа</a>.
Узнавайте расписание, заказывайте справки и получайте оповещение об важных события.""", 
                                    reply_markup = kb.mainMenuAdmin, 
                                    parse_mode = "HTML")