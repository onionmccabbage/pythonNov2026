from weatherService import WeatherGetter

def main():
    cityList = ['Dover', 'London', 'Salford']
    reportList = []
    weatherGetterInstance = WeatherGetter()
    for city in cityList:
        report = weatherGetterInstance.findWeather(city)
        reportList.append(report)
    return reportList


if __name__ == '__main__':
    r = main()
    for _ in r:
        print(_)