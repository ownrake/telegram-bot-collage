import logging

from app.database.models import async_session
from app.database.models import Lesson, CallSchlude, User
from sqlalchemy import select


async def set_user(user_id, user_name):
    user_name = f"@{user_name.lower()}"
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.id == user_id))

        if not user:
            session.add(User(id = user_id, user_name = user_name))
            await session.commit()


async def get_schlude():
    async with async_session as session:
        pass


async def get_time_lesson():
    async with async_session() as session:
        data = await session.scalar(select(CallSchlude))
        result = f"""Расписание звонков:
        
1 пара: {data.first_lesson}

2 пара: {data.second_lesson}

3 пара: {data.third_lesson}

4 пара: {data.fourth_lesson}

5 пара: {data.fifth_lesson}

6 пара: {data.sixth_lesson}"""

        return result


async def get_profile(user_id):
    async with async_session() as session:
        logging.info(f"Fetching profile for user_id: {user_id}")
        data = await session.scalar(select(User).where(User.id == user_id))
        result = f"👤 {data.user_name}\n\nПобеды: {data.wins}\nПроигрыши: {data.loses}\n\nprofile ID: {data.id}"

        return result
        