import logging

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.database.requests as rq
import app.admin.admin_keyboards as kb

admin_router = Router()

class Edit_Lesson(StatesGroup):
    count = State()
    time = State()
    name = State()
    classroom = State()
    teacher = State()


async def start_admin(message: Message):
    user = message.from_user
    logging.info(f"Moderator: @{(user.first_name).lower()} logged in")

    await message.answer("""💻 <a href = 'https://t.me/helperforgroup201is_bot'>Студенчиский платформа</a>.
Узнавайте расписание, заказывайте справки и получайте оповещение об важных события.""", 
                                    reply_markup=kb.main_menu_admin, 
                                    parse_mode="HTML")
    
# Далее главные функции и обработчики

@admin_router.callback_query(F.data.in_(["admin_panel", "back_main_menu_panel"]))
async def admin_panel(call: CallbackQuery):
    await call.message.edit_text("🛠 Выбери действие.", reply_markup=kb.main_menu_panel)

    @admin_router.callback_query(F.data.in_(["update_schlude", "back_update_schlude"]))
    async def update_schlude(call: CallbackQuery):
        await call.message.edit_text("Выбери тип расписния", reply_markup=kb.schlude_type)

        @admin_router.callback_query(F.data.in_(["update_lessons", "back_update_lessons"]))
        async def update_lessons(call: CallbackQuery):
            await call.message.edit_text("Выбери день недели", reply_markup=kb.week_type)

            global type_week; global type_day

            @admin_router.callback_query(F.data.in_(["update_even_week"]))
            async def update_even_week(call: CallbackQuery):
                global type_week; type_week = "Четная"

                await call.message.edit_text("Выбери день недели", reply_markup=kb.day_type)

                @admin_router.callback_query(F.data.in_(["update_monday"]))
                async def update_monday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Понедельник"

                    await state.set_state(Edit_Lesson.count)
                    await call.message.answer("Введите номер занятия.")

                    @admin_router.message(Edit_Lesson.count)
                    async def time(message: Message, state: FSMContext):
                        await state.update_data(count=message.text)
                        await state.set_state(Edit_Lesson.time)
                        await message.answer("Введите время занятия.")

                    @admin_router.message(Edit_Lesson.time)
                    async def name(message: Message, state: FSMContext):
                        await state.update_data(time=message.text)
                        await state.set_state(Edit_Lesson.name)
                        await message.answer("Введите название предмета.")

                    @admin_router.message(Edit_Lesson.name)
                    async def classroom(message: Message, state: FSMContext):
                        await state.update_data(name=message.text)
                        await state.set_state(Edit_Lesson.classroom)
                        await message.answer("Введите кабинет.")

                    @admin_router.message(Edit_Lesson.classroom)
                    async def teacher(message: Message, state: FSMContext):
                        await state.update_data(classroom=message.text)
                        await state.set_state(Edit_Lesson.teacher)
                        await message.answer("Введите имя преподавателя.")

                    @admin_router.message(Edit_Lesson.teacher)
                    async def teacher(message: Message, state: FSMContext):
                        global type_week; global type_day

                        await state.update_data(teacher=message.text)
                        data = await state.get_data()
                        await rq.update_lessons(type_week=type_week, type_day=type_day, count=data["count"], time=data["time"], name=data["name"], classroom=data["classroom"], teacher=data["teacher"])
                        await state.clear() 

                @admin_router.callback_query(F.data.in_(["update_tuesday"]))
                async def update_tuesday(call: CallbackQuery):
                    global type_day; type_day = "Вторник"
                    
                @admin_router.callback_query(F.data.in_(["update_wendnesday"]))
                async def update_wendnesday(call: CallbackQuery):
                    global type_day; type_day = "Среда"
                
                @admin_router.callback_query(F.data.in_(["update_thursday"]))
                async def update_thursday(call: CallbackQuery):
                    global type_day; type_day = "Четверг"
                
                @admin_router.callback_query(F.data.in_(["update_friday"]))
                async def update_friday(call: CallbackQuery):
                    global type_day; type_day = "Пятница"
                
                @admin_router.callback_query(F.data.in_(["update_saturday"]))
                async def update_saturday(call: CallbackQuery):
                    global type_day; type_day = "Суббота"
                    
            @admin_router.callback_query(F.data.in_(["update_odd_week"]))
            async def update_odd_week(call: CallbackQuery):
                global type_week; type_week = "Нечетная"

                await call.message.edit_text("Выбери день недели.", reply_markup=kb.day_type_odd)

    '''@admin_router.callback_query(F.data.in_(["calls"]))
                async def calls(call: CallbackQuery):
                    pass'''


# Далее возврат к главному сообщению

@admin_router.callback_query(F.data == "back_main_menu_admin")
async def back_main_menu_admin(call: CallbackQuery):
    await call.message.edit_text("""💻 <a href = 'https://t.me/helperforgroup201is_bot'>Студенчиский платформа</a>.
Узнавайте расписание, заказывайте справки и получайте оповещение об важных события.""", 
                                    reply_markup=kb.main_menu_admin, 
                                    parse_mode="HTML")