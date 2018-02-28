from urllib import request
import json

TOKEN = ""


def getweather(city):
    try:
        weather = json.loads(request.urlopen(
            f'http://api.worldweatheronline.com/premium/v1/weather.ashx?key='
            f'{TOKEN}&q={request.quote(city)}&num_of_days=1&format=json').read())
        return weather['data']['request'][0]['query'] + \
               ' ' + weather['data']['current_condition'][0]['temp_C'] + '\u2103'
    except KeyError:
        return 'Что то пошло не так, возможно, у вас ошибка, а возможно и у меня.'
