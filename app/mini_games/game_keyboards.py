from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu_game = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🪨 ✂️ 📄", callback_data="rsp_game")],
    [InlineKeyboardButton(text="‹", callback_data="back_main_menu")]
])

rsp_choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🪨", callback_data="rock"),
     InlineKeyboardButton(text="✂️", callback_data="scissors"),
     InlineKeyboardButton(text="📄", callback_data="paper")]
])

rsp_end = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="‹ Выйти", callback_data="back_main_menu_game"),
     InlineKeyboardButton(text="Снова", callback_data="back_rsp_game")]
])