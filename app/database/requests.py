import aiosqlite as asq


async def get_all_data():
    async with asq.connect("database.sqlite3") as db:
        async with db.execute("SELECT * FROM lessons") as cursor:
            result = await cursor.fetchall()
        return result













'''from models import db, cur   
def test():
    result =  cur.execute("SELECT * FROM products;").fetchall()
    return result[0][1]
    db.commit()
print(test())'''