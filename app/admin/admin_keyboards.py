from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainMenuAdmin = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "📅 Расписания", callback_data = "schludeCall"), 
     InlineKeyboardButton(text = "📝 Заказать справки",  callback_data = "orderCertificatesCall")],
    [InlineKeyboardButton(text = '🎮 Мини-игры', callback_data = "miniGamesCallGames"),
     InlineKeyboardButton(text = "👤 Профиль", callback_data = "profileCall")],
    [InlineKeyboardButton(text = "🛠 admin panel", callback_data = "adminPanelAdmin")],
    [InlineKeyboardButton(text = "🤖 О боте", callback_data = "aboutUsCall")]
])

# -- ------------------------------------------------------------------------------------------------



# -- ------------------------------------------------------------------------------------------------

goToMainAdmin = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "‹ Назад", callback_data = "goToMainMenuCallAdmin")]
])