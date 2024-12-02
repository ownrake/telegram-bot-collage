import logging

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import config as con
import app.database.requests as rq
import app.user.user_keyboards as kb

from app.admin.admin_handlers import start_admin, back_main_menu_admin
# import app.admin.admin_keyboards as admin_kb

user_router = Router()


async def add_user(message: Message):
    user = message.from_user
    
    await rq.set_user(user_id=user.id, user_name=user.first_name)

@user_router.message(CommandStart())
async def start(message: Message):
    await add_user(message=message)

    if message.from_user.id in con.moder_id:
        await start_admin(message=message)
    else:
        await message.answer("""💻 <a href = 'https://t.me/helperforgroup201is_bot'>Студенчиский платформа</a>.
Узнавайте расписание, заказывайте справки и получайте оповещение об важных события.""", 
                                    reply_markup=kb.main_menu, 
                                    parse_mode="HTML")


# Далее главные функции и обработчики

global user_checking_week_status
global user_checking_day_status


@user_router.callback_query(F.data.in_(["schlude", "back_schlude_type"]))
async def schlude(call: CallbackQuery):
    await call.message.edit_text("Выбери тип расписания.", reply_markup=kb.schlude_type)

    @user_router.callback_query(F.data.in_(["lessons", "back_week_type", "back_week_type_odd"]))
    async def lessons(call: CallbackQuery):
        await call.message.edit_text("Выберите тип недели.", reply_markup=kb.week_type)


        @user_router.callback_query(F.data.in_(["even_week", "back_day_type"]))
        async def even_week(call: CallbackQuery):
            global user_checking_week_status
            user_checking_week_status = "Четная"
            logging.info(f"user_checking_week_status: {user_checking_week_status}")

            await call.message.edit_text("Выбери день недели.", reply_markup=kb.day_type)

            @user_router.callback_query(F.data.in_(["monday", ""]))
            async def monday(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Понедельник"
                logging.info(F"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type)


            @user_router.callback_query(F.data.in_(["tuesday", ""]))
            async def tuesday(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Вторник"
                logging.info(F"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type)


            @user_router.callback_query(F.data.in_(["wendnesday", ""]))
            async def wendnesday(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Среда"
                logging.info(F"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type)


            @user_router.callback_query(F.data.in_(["thursday", ""]))
            async def thursday(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Четверг"
                logging.info(F"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type)


            @user_router.callback_query(F.data.in_(["friday", ""]))
            async def friday(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Пятница"
                logging.info(F"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type)


            @user_router.callback_query(F.data.in_(["saturday", ""]))
            async def saturday(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Суббота"
                logging.info(F"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type)


        @user_router.callback_query(F.data.in_(["odd_week", "back_day_type_odd"]))
        async def odd_week(call: CallbackQuery):
            global user_checking_week_status
            user_checking_week_status = "Нечетная"
            logging.info(f"user_checking_week_status: {user_checking_week_status}")

            await call.message.edit_text("Выбери день недели.", reply_markup=kb.day_type_odd)


            @user_router.callback_query(F.data.in_(["monday_odd", ""]))
            async def monday_odd(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Понедельник"
                logging.info(f"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type_odd)


            @user_router.callback_query(F.data.in_(["tuesday_odd", ""]))
            async def tuesday_odd(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Вторник"
                logging.info(f"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type_odd)


            @user_router.callback_query(F.data.in_(["wendnesday_odd", ""]))
            async def wendnesday_odd(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Среда"
                logging.info(f"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type_odd)


            @user_router.callback_query(F.data.in_(["thursday_odd", ""]))
            async def thursday_odd(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Четверг"
                logging.info(f"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type_odd)


            @user_router.callback_query(F.data.in_(["friday_odd", ""]))
            async def friday_odd(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Пятница"
                logging.info(f"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type_odd)


            @user_router.callback_query(F.data.in_(["saturday_odd", ""]))
            async def saturday_odd(call: CallbackQuery):
                global user_checking_day_status
                user_checking_day_status = "Суббота"
                logging.info(f"user_checking_day_status: {user_checking_day_status}")

                await call.message.edit_text(await rq.get_schlude(type_week=user_checking_week_status,
                                            type_day=user_checking_day_status), reply_markup=kb.back_day_type_odd)


    @user_router.callback_query(F.data.in_(["calls"]))
    async def calls(call: CallbackQuery):
        await call.message.edit_text(await rq.get_time_lesson(), reply_markup=kb.back_schlude_type)


@user_router.callback_query(F.data.in_(["order_certificates"]))
async def order_certificates(call: CallbackQuery):
    await call.message.edit_text("Заказать справки вы можете перейдя по кнопке ниже.", reply_markup=kb.order_certificates)


@user_router.callback_query(F.data.in_(["profile"]))
async def profile(call: CallbackQuery):
    await call.message.edit_text(await rq.get_profile(user_id=call.from_user.id), reply_markup=kb.back_main_menu)


@user_router.callback_query(F.data.in_(["about_us"]))
async def about_us(call: CallbackQuery):
    await call.message.edit_text("unknow", reply_markup=kb.back_main_menu)


# Далее возврат к главному сообщению и отправка сообщения непонимания


@user_router.callback_query(F.data == "back_main_menu")
async def back_main_menu(call: CallbackQuery):
    if call.from_user.id in con.moder_id:
        await back_main_menu_admin(call)
    else:
        await call.message.edit_text("""💻 <a href = 'https://t.me/helperforgroup201is_bot'>Студенчиский платформа</a>.
Узнавайте расписание, заказывайте справки и получайте оповещение об важных события.""", 
                                    reply_markup=kb.main_menu, 
                                    parse_mode="HTML")
        

'''@user_router.message()
async def handle_unknown_message(message: Message):
    await message.answer("Прости я тебя не понял! Пожалуста используй кнопки.\n\nЕсли у тебя их нет используй ››› /start")
    logging.info(f"Unknow message, @{(message.from_user.first_name).lower()}. Message: {message.text}")'''