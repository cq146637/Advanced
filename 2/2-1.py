"""
    实现可迭代对象和迭代器对象,达到使用时加载，实现资源的节约和高效利用
"""
from collections import Iterable, Iterator
import requests


class WeatherItertor(Iterator):
    """ 
        城市气温迭代器类
    """
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s , %s' % (city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherItertor(self.cities)


def main():
    wi = WeatherIterable(['上海', '北京', '广州', '天津', '深圳'])
    for i in wi:
        print(i)


if __name__ == '__main__':
    main()