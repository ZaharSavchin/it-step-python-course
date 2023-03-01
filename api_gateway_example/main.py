import asyncio
import json

from aiohttp import web

from collector.collector import Collector
from collector.logger import logger
from collector.db import DB

db = DB()


async def handler(request):
    collector = Collector()
    city = request.rel_url.query['city']
    weather_data = await collector.get_weather(city)
    result = {'city': city, 'weather': weather_data}
    logger.info(f'Got data for {city}')

    await db.save_to_db(city=city, weather_data=json.dumps(weather_data))
    logger.info(f'Data for {city} has been saved into database')

    return web.Response(text=json.dumps(result, ensure_ascii=False))


async def main():
    await db.create_table()
    app = web.Application()
    app.add_routes([web.get('/weather', handler=handler)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    while True:
        await asyncio.sleep(7200)

if __name__ == "__main__":
    logger.info('Application is running ...')
    asyncio.run(main())