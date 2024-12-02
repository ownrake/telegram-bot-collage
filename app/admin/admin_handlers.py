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

class Edit_call(StatesGroup):
    first_lesson = State()
    second_lesson = State()
    third_lesson = State()
    fourth_lesson = State()
    fifth_lesson = State()
    sixth_lesson = State()


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

            @admin_router.callback_query(F.data.in_(["update_even_week", "back_update_lessons"]))
            async def update_even_week(call: CallbackQuery):
                global type_week; type_week = "Четная"

                await call.message.edit_text("Выбери день недели", reply_markup=kb.day_type)

                @admin_router.callback_query(F.data.in_(["update_monday"]))
                async def update_monday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Понедельник"

                    await update_lesson(call, state)

                @admin_router.callback_query(F.data.in_(["update_tuesday"]))
                async def update_tuesday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Вторник"

                    await update_lesson(call, state)

                @admin_router.callback_query(F.data.in_(["update_wendnesday"]))
                async def update_wendnesday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Среда"

                    await update_lesson(call, state)

                @admin_router.callback_query(F.data.in_(["update_thursday"]))
                async def update_thursday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Четверг"

                    await update_lesson(call, state)

                @admin_router.callback_query(F.data.in_(["update_friday"]))
                async def update_friday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Пятница"

                    await update_lesson(call, state)

                @admin_router.callback_query(F.data.in_(["update_saturday"]))
                async def update_saturday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Суббота"

                    await update_lesson(call, state)

            @admin_router.callback_query(F.data.in_(["update_odd_week", "back_update_lessons_odd"]))
            async def update_odd_week(call: CallbackQuery):
                global type_week; type_week = "Нечетная"

                await call.message.edit_text("Выбери день недели.", reply_markup=kb.day_type_odd)

                @admin_router.callback_query(F.data.in_(["update_monday_odd"]))
                async def update_monday_odd(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Понедельник"

                    await update_lesson(call, state)

                @admin_router.callback_query(F.data.in_(["update_tuesday_odd"]))
                async def update_tuesday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Вторник"

                    await update_lesson(call, state)

                @admin_router.callback_query(F.data.in_(["update_wendnesday_odd"]))
                async def update_wendnesday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Среда"

                    await update_lesson(call, state)

                @admin_router.callback_query(F.data.in_(["update_thursday_odd"]))
                async def update_thursday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Четверг"

                    await update_lesson(call, state)

                @admin_router.callback_query(F.data.in_(["update_friday_odd"]))
                async def update_friday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Пятница"

                    await update_lesson(call, state)

                @admin_router.callback_query(F.data.in_(["update_saturday_odd"]))
                async def update_saturday(call: CallbackQuery, state: FSMContext):
                    global type_day; type_day = "Суббота"

                    await update_lesson(call, state)

        @admin_router.callback_query(F.data.in_(["update_calls"]))
        async def calls(call: CallbackQuery, state: FSMContext):
            await state.set_state(Edit_call.first_lesson)
            await call.message.answer("Введите время первого занятия.")

            @admin_router.message(Edit_call.first_lesson)
            async def first_lesson(message: Message, state: FSMContext):
                await state.update_data(first_lesson=message.text)
                await state.set_state(Edit_call.second_lesson)
                await message.answer("Введите время второго занятия.")

            @admin_router.message(Edit_call.second_lesson)
            async def second_lesson(message: Message, state: FSMContext):
                await state.update_data(second_lesson=message.text)
                await state.set_state(Edit_call.third_lesson)
                await message.answer("Введите время третьего занятия.")

            @admin_router.message(Edit_call.third_lesson)
            async def fourth_lesson(message: Message, state: FSMContext):
                await state.update_data(third_lesson=message.text)
                await state.set_state(Edit_call.fourth_lesson)
                await message.answer("Введите время четвертого занятия.")

            @admin_router.message(Edit_call.fourth_lesson)
            async def fourth_lesson(message: Message, state: FSMContext):
                await state.update_data(fourth_lesson=message.text)
                await state.set_state(Edit_call.fifth_lesson)
                await message.answer("Введите время пятого занятия")

            @admin_router.message(Edit_call.fifth_lesson)
            async def fifth_lesson(message: Message, state: FSMContext):
                await state.update_data(fifth_lesson=message.text)
                await state.set_state(Edit_call.sixth_lesson)
                await message.answer("Введите время шестого занятия")

            @admin_router.message(Edit_call.sixth_lesson)
            async def sixth_lesson(message: Message, state: FSMContext):
                await state.update_data(sixth_lesson=message.text)
                data = await state.get_data()
                await rq.update_calls(first_lesson=data["first_lesson"], second_lesson=data["second_lesson"], third_lesson=data["third_lesson"],
                    fourth_lesson=data["fourth_lesson"], fifth_lesson=data["fifth_lesson"], sixth_lesson=data["sixth_lesson"])
                await state.clear()

                await call.message.answer("Выбери тип расписния", reply_markup=kb.schlude_type)
                


# Далее возврат к главному сообщению

@admin_router.callback_query(F.data == "back_main_menu_admin")
async def back_main_menu_admin(call: CallbackQuery):
    await call.message.edit_text("""💻 <a href = 'https://t.me/helperforgroup201is_bot'>Студенчиский платформа</a>.
Узнавайте расписание, заказывайте справки и получайте оповещение об важных события.""", 
                                    reply_markup=kb.main_menu_admin, 
                                    parse_mode="HTML")

async def update_lesson(call, state):
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
        await rq.update_lessons(type_week=type_week, type_day=type_day, count=data["count"], time=data["time"],
            name=data["name"], classroom=data["classroom"], teacher=data["teacher"])
        await state.clear()

        await call.message.answer("Выбери тип расписния", reply_markup=kb.schlude_type)