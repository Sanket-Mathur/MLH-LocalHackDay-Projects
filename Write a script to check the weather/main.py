import python_weather
import asyncio

async def fetch_weather():
    client = python_weather.Client(format=python_weather.METRIC)
    weather = await client.find("New Delhi")
    
    # extracting and printing the weather report
    report = weather.current

    print('Weather Report of {}'.format(report.observation_point))
    print('{}, {}'.format(report.day, report.date.date()))
    print('The current temperature is {}°C with {}% humidity'.format(report.temperature, report.humidity))
    print('The sky is {} with a wind speed of {}'.format(report.sky_text, report.wind_display))

    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_weather())

