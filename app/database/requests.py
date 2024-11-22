from app.database.models import async_session
from app.database.models import CallSchedule, User, Lesson
from sqlalchemy import select


async def set_user(user_id, user_name):
    user_name = f"@{user_name.lower()}"
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.id == user_id))

        if not user:
            session.add(User(id = user_id, user_name = user_name))
            await session.commit()

import logging

async def get_profile(user_id):
    async with async_session() as session:
        logging.info(f"Fetching profile for user_id: {user_id}")
        data = await session.scalar(select(User).where(User.id == user_id))
        result = f"👤 {data.user_name}\n\nПобеды: {data.wins}\nПроигрыши: {data.loses}\n\nprofile ID: {data.id}"

        return result
        