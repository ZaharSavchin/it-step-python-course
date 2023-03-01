import aiosqlite
from datetime import datetime


class DB:

    @staticmethod
    async def create_table():
        async with aiosqlite.connect('weather.db') as db:
            await db.execute('CREATE TABLE IF NOT EXISTS weather (date text, city text, weather text)')
            await db.commit()

    @staticmethod
    async def save_to_db(city, weather_data):
        async with aiosqlite.connect('weather.db') as db:
            await db.execute('INSERT INTO weather VALUES (?, ?, ?)', (datetime.now(), city, weather_data))
            await db.commit()