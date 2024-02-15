import asyncio
import aiohttp

async def get_weather(session, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=5dd4a8b96c4a88cffbc4d0514293f207&units=metric'
    async with session.get(url) as response:
        data = await response.json()
        print(data)

async def main():
    cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", 
    "Dallas", "San Jose", "Austin", "Jacksonville", "San Francisco", "Indianapolis", "Columbus", "Fort Worth", 
    "Charlotte", "Seattle", "Denver", "El Paso", "Detroit", "Washington", "Boston", "Memphis", "Nashville", 
    "Portland", "Oklahoma City", "Las Vegas", "Baltimore", "Louisville", "Milwaukee", "Albuquerque", 
    "Tucson", "Fresno", "Sacramento", "Kansas City", "Long Beach", "Mesa", "Atlanta", "Colorado Springs", 
    "Virginia Beach", "Raleigh", "Omaha", "Miami", "Oakland", "Minneapolis", "Tulsa", "Wichita", 
    "New Orleans", "Arlington", "Cleveland", "Bakersfield", "Tampa", "Aurora", "Honolulu", "Anaheim", 
    "Santa Ana", "Corpus Christi", "Riverside", "Lexington", "Stockton", "Pittsburgh", "Anchorage", 
    "Cincinnati", "Saint Paul", "Greensboro", "Toledo", "Newark", "Plano", "Henderson", "Lincoln", 
    "Orlando", "Jersey City", "Chula Vista", "Buffalo", "Fort Wayne", "Chandler", "St. Petersburg", 
    "Laredo", "Durham", "Irvine", "Madison", "Norfolk", "Lubbock", "Gilbert", "Winston-Salem", 
    "Glendale", "Reno", "Hialeah", "Garland", "Chesapeake", "Irving", "North Las Vegas", 
    "Scottsdale", "Baton Rouge", "Fremont", "Richmond", "Boise"
]
    async with aiohttp.ClientSession() as session:
        tasks = []
        for city in cities:
            tasks.append(asyncio.create_task(get_weather(session, city)))
        await asyncio.gather(*tasks)

asyncio.run(main())

