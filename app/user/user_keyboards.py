from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainMenu = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "📅 Расписания", callback_data = "schludeCall"), 
     InlineKeyboardButton(text = "📝 Заказать справки",  callback_data = "orderCertificatesCall")],
    [InlineKeyboardButton(text = '🎮 Мини-игры', callback_data = "miniGamesCall"),
     InlineKeyboardButton(text = "👤 Профиль", callback_data = "profileCall")],
    [InlineKeyboardButton(text = "🤖 О боте", callback_data = "aboutUsCall")]
])

schludeMain = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "📚 Занятия", callback_data = "lessonCall")],
    [InlineKeyboardButton(text = "🔔 Звонки", callback_data = "callCall")],
    [InlineKeyboardButton(text = "‹ Назад", callback_data = "goToMainMenuCall")]
])

schludeLessonMain = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Четная", callback_data = "evenWeekCall"),
     InlineKeyboardButton(text = "Нечетная", callback_data = "oddWeekCall")],
     [InlineKeyboardButton(text = "‹ Назад", callback_data = "GoToSchludeMainCall")]
])

goToMain = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "‹ Назад", callback_data = "goToMainMenuCall")]
])

GoToSchludeMain = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "‹ Назад", callback_data = "GoToSchludeMainCall")]
])