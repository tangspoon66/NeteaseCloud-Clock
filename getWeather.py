# -*- coding: utf-8 -*
import requests
params = {
    # 城市id
    'location': '101280101',
    # 和风天气key
    'key': 'xxxxxxxxx',
    'gzip': 'y'
}


def getNowWeather():
    # 开发版接口地址
    url = 'https://devapi.qweather.com/v7/weather/now?'
    # 接口参数
    html = requests.get(url, params)
    content = html.json()
    now_temp = content['now']['temp']
    now_text = content['now']['text']
    return now_temp, now_text



def get3d():
    url = 'https://devapi.qweather.com/v7/weather/3d?'
    html = requests.get(url, params)
    html_content = html.json()
    tempMax = html_content['daily'][0]['tempMax']
    tempMin = html_content['daily'][0]['tempMin']
    sunsetTime = html_content['daily'][0]['sunset']
    return tempMax, tempMin, sunsetTime
