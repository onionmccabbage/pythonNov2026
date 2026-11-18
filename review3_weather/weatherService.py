import requests
from weather import Weather

class WeatherGetter():
    def __init__(self):
        pass
    def findWeather(self, city):
        url_template = (
            'http://api.openweathermap.org/data/2.5/'
            'weather?q={}&units={}&APPID=48f2d5e18b0d2bc50519b58cce6409f1')
        try:
            uri = url_template.format(city, 'metric')
            # print(uri)
            response = requests.get(uri)
            results = response.json()
            self.temperature = results['main']['temp']
            self.description = results['weather'][0]['description']
            weatherReport = Weather(city=city, temp=self.temperature, desc=self.description)
            return weatherReport
        except Exception as err:
            print(err)
