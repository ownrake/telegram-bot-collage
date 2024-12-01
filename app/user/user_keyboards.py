from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config as con

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📅 Расписания", callback_data="schlude"), 
     InlineKeyboardButton(text="📝 Заказать справки",  callback_data="order_certificates")],
    [InlineKeyboardButton(text="🎮 Мини-игры", callback_data="mini_games"),
     InlineKeyboardButton(text="👤 Профиль", callback_data="profile")],
    [InlineKeyboardButton(text="🤖 О боте", callback_data="about_us")]
])

back_main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="‹", callback_data="back_main_menu")]
])

schlude_type = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📚 Занятия", callback_data="lessons"),
     InlineKeyboardButton(text="🔔 Звонки", callback_data="calls")],
    [InlineKeyboardButton(text="‹", callback_data="back_main_menu")]
])

week_type = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Четная", callback_data="even_week"),
     InlineKeyboardButton(text="Нечетная", callback_data="odd_week")],
    [InlineKeyboardButton(text="‹", callback_data="back_schlude_type")]
])

# -- ------------------------------------------------------------------------------------

day_type = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Понедельник", callback_data="monday"),
     InlineKeyboardButton(text="Вторник", callback_data="tuesday")],
    [InlineKeyboardButton(text="Среда", callback_data="wendnesday"),
     InlineKeyboardButton(text="Четверг", callback_data="thursday")],
    [InlineKeyboardButton(text="Пятница", callback_data="friday"),
     InlineKeyboardButton(text="Суббота", callback_data="saturday")],
    [InlineKeyboardButton(text="‹", callback_data="back_week_type")]
])

back_day_type = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="‹", callback_data="back_day_type")]
])

# -- ------------------------------------------------------------------------------------

day_type_odd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Понедельник", callback_data="monday_odd"),
     InlineKeyboardButton(text="Вторник", callback_data="tuesday_odd")],
    [InlineKeyboardButton(text="Среда", callback_data="wendnesday_odd"),
     InlineKeyboardButton(text="Четверг", callback_data="thursday_odd")],
    [InlineKeyboardButton(text="Пятница", callback_data="friday_odd"),
     InlineKeyboardButton(text="Суббота", callback_data="saturday_odd")],
    [InlineKeyboardButton(text="‹", callback_data="back_week_type_odd")]
])

back_day_type_odd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="‹", callback_data="back_day_type_odd")]
])

# -- ------------------------------------------------------------------------------------

back_schlude_type = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="‹", callback_data="back_schlude_type")]
])

order_certificates = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="‹", callback_data="back_main_menu"),
     InlineKeyboardButton(text="Заказать", url=con.link)]
])