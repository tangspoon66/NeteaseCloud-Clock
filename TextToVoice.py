from aip import AipSpeech
import os
import sys
from getWeather import *


APP_ID = '23185990'
API_KEY = 'nrKiIERZWl7SfHI1TFK3qWya'
SECRET_KEY = 'D8xvsI9gMEH4wgWGjTiLNg4Y3sa4r3f6'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 获取天气模块的信息
now_temp, now_text = getNowWeather()
tempMax, tempMin, sunsetTime = get3d()

# 正常天气
text_normal = '翠宜宝贝早上好呀！现在外面' + now_temp + '度，' + '今天最低温度为：' + tempMin + '度，' + '最高温度为：' + tempMax + '度，' \
              + '看好温度穿衣哦！' + '再提醒一下，今天的日落时间是，' + sunsetTime + '，祝您傍晚能看到美丽的日落！拜拜～'
# 最高温度小于14度时
text_lowtemp = '翠宜宝贝早上好呀！现在外面' + now_temp + '度，' + '今天最低温度为：' + tempMin + '度！' + '最高温度也才：' + tempMax + '度，' \
               + '，也是好冷的呢！要多穿衣服哦！' + '再提醒一下，今天的日落时间是，' + sunsetTime + '祝翠宜宝贝傍晚能看到美丽的日落！拜拜～'
# 下雨
text_rain = '翠宜宝贝早上好呀！现在外面' + now_temp + '度，' + '外边正在下雨呢，记得带伞～' + '今天最低温度为：' + tempMin + '度，' + '最高温度为：' + tempMax + '度，' \
            + '看好温度穿衣哦！' + '再提醒一下，今天的日落时间是，' + sunsetTime + '祝翠宜宝贝傍晚能看到美丽的日落！拜拜～' + '对了，记得带伞哦！再见'

# per: 3是性感大叔 4是妹妹；spd: 是语速，vol是: 音量
if int(tempMax) < 14:
    result = client.synthesis(text_lowtemp, 'zh', 1, {'vol': 10, 'per': 4, 'spd': 5})
elif now_text is '雨':
    result = client.synthesis(text_rain, 'zh', 1, {'vol': 10, 'per': 4})
else:
    result = client.synthesis(text_normal, 'zh', 1, {'vol': 10, 'per': 4, 'spd': 5})

# 播放模块
if not isinstance(result, dict):
    with open('/home/clock/weather.mp3', 'wb') as f:
        f.write(result)
os.system('mplayer "%s" > /dev/null 2>&1' % '/home/clock/weather.mp3')
