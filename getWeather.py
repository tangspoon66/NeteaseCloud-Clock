# -*- coding: utf-8 -*
import requests
params = {
    'location': '101280101',
    'key': '6dee7771746148fbbee9cedeb9c1ffc4',
    'gzip': 'y'
}
umbrella = 0
moreClothes = 0

def getNowWeather():
    # 开发版接口地址
    url = 'https://devapi.qweather.com/v7/weather/now?'
    # 接口参数
    html = requests.get(url, params)
    content = html.json()
    now_temp = content['now']['temp']
    now_text = content['now']['text']
    return now_temp, now_text
    # 加入判断：如果下雨，提醒带好雨伞
    # if now_text is '雨':
    #     bringA
    # if now_temp < 14:
    # 最高温度为14度时，提醒穿衣


def get3d():
    url = 'https://devapi.qweather.com/v7/weather/3d?'
    html = requests.get(url, params)
    html_content = html.json()
    tempMax = html_content['daily'][0]['tempMax']
    tempMin = html_content['daily'][0]['tempMin']
    sunsetTime = html_content['daily'][0]['sunset']
    return tempMax, tempMin, sunsetTime

#
# if __name__ == '__main__':
#     now_temp, now_text = getNowWeather()
#     tempMax, tempMin, sunsetTime = get3d()
#     if tempMax < 14:
#         moreClothes = 1
#     if now_text is '雨':
#         umbrella = 1
