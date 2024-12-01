from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu_admin = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text="📅 Расписания", callback_data="schlude"), 
     InlineKeyboardButton(text="📝 Заказать справки",  callback_data="order_certificates")],
    [InlineKeyboardButton(text="🎮 Мини-игры", callback_data="mini_games"),
     InlineKeyboardButton(text="👤 Профиль", callback_data="profile")],
    [InlineKeyboardButton(text="🛠 admin panel", callback_data="admin_panel")],
    [InlineKeyboardButton(text="🤖 О боте", callback_data="about_us")]
])

main_menu_panel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Редактировать расписание", callback_data="update_schlude")],
    [InlineKeyboardButton(text="Отправить уведомление", callback_data="send_notification")],
    [InlineKeyboardButton(text="‹", callback_data="back_main_menu_admin")]
])

schlude_type = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Занятия", callback_data="update_lessons")],
    [InlineKeyboardButton(text="Звонки", callback_data="update_calls")],
    [InlineKeyboardButton(text="‹", callback_data="back_main_menu_panel")]
])

week_type = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Четная", callback_data="update_even_week")],
    [InlineKeyboardButton(text="Нечетная", callback_data="update_odd_week")],
    [InlineKeyboardButton(text="‹", callback_data="back_update_schlude")]
])

# -- ----------------

day_type = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Понедельник", callback_data="update_monday"),
     InlineKeyboardButton(text="Вторник", callback_data="update_tuesday")],
    [InlineKeyboardButton(text="Среда", callback_data="update_wendnesday"),
     InlineKeyboardButton(text="Четверг", callback_data="update_thursday")],
    [InlineKeyboardButton(text="Пятница", callback_data="update_friday"),
     InlineKeyboardButton(text="Суббота", callback_data="update_saturday")],
    [InlineKeyboardButton(text="‹", callback_data="back_update_lessons")]
])

# -- ----------------

day_type_odd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Понедельник", callback_data="update_monday_odd"),
     InlineKeyboardButton(text="Вторник", callback_data="update_tuesday_odd")],
    [InlineKeyboardButton(text="Среда", callback_data="update_wendnesday_odd"),
     InlineKeyboardButton(text="Четверг", callback_data="update_thursday_odd")],
    [InlineKeyboardButton(text="Пятница", callback_data="update_friday_odd"),
     InlineKeyboardButton(text="Суббота", callback_data="update_saturday_odd")],
    [InlineKeyboardButton(text="‹", callback_data="back_update_lessons")]
])

# -- ----------------

back_main_menu_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="‹", callback_data="back_main_menu_admin")]
])