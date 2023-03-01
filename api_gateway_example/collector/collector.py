from aiohttp import ClientSession


KEY = '2a4ff86f9aaa70041ec8e82db64abf56'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


class Collector:

    @staticmethod
    async def get_weather(city: str):
        async with ClientSession() as session:
            params = {'q': city, 'APPID': KEY}

            async with session.get(BASE_URL, params=params) as response:
                res_data = await response.json()
                temp = res_data['main'].get('temp')
                hum = res_data['main'].get('humidity')
                weather = {"temp": temp, "humidity": hum}

                return weather