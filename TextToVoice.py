from aip import AipSpeech
import os
import sys
from getWeather import *

# 百度TTS信息
APP_ID = 'xxxx'
API_KEY = 'xxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxxxxx'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 获取天气模块的信息
now_temp, now_text = getNowWeather()
tempMax, tempMin, sunsetTime = get3d()

# 正常天气
text_normal = 'xxx早上好呀！现在外面' + now_temp + '度，' + '今天最低温度是：' + tempMin + '度，' + '最高温度是：' + tempMax + '度，' \
              + '看好温度穿衣哦！' + '再提醒一下，今天的日落时间是，' + sunsetTime + '，祝宝贝傍晚能看到美丽的日落！拜拜～'
# 最高温度小于14度时
text_cold = 'xxx早上好呀！现在外面' + now_temp + '度，' + '今天最低温度是：' + tempMin + '度！' + '但是注意哦，最高温度也才：' + tempMax + '度，' \
            + '，也是好冷的呢！要多穿衣服哦！' + '再提醒一下，今天的日落时间是，' + sunsetTime + '，祝宝贝傍晚能看到美丽的日落！拜拜～'
# 下雨
text_rain = 'xxx早上好呀！现在外面' + now_temp + '度，' + '外边正在下雨呢，记得带伞～' + '今天最低温度是：' + tempMin + '度，' + '最高温度是：' + tempMax + '度，' \
            + '看好温度穿衣哦！' + '再提醒一下，今天的日落时间是，' + sunsetTime + '，祝宝贝傍晚能看到美丽的日落！拜拜～' + '对了，记得带伞哦！再见'
# 下雨又冷
text_cold_rain = 'xxx早上好呀！现在外面' + now_temp + '度，' + '外边正在下雨呢，记得带伞～记得带伞～记得带伞～' + '今天最低温度是：' + tempMin + '度，' + '另外还要注意，今天最高温度也才：' + tempMax + '度，' \
                 + '，也是好冷的呢！要多穿衣服哦！' + '再提醒一下，今天的日落时间是，' + sunsetTime + '，祝宝贝傍晚能看到美丽的日落！拜拜～' + '对了，记得带伞哦！再见'

# per: 3是性感大叔 4是妹妹；spd: 是语速，vol是: 音量
if int(tempMax) <= 14:
    result = client.synthesis(text_cold, 'zh', 1, {'vol': 10, 'per': 4, 'spd': 5})
elif now_text == '雨':
    result = client.synthesis(text_rain, 'zh', 1, {'vol': 10, 'per': 4})
elif int(tempMax) <= 14 & now_text == '雨':
    result = client.synthesis(text_cold_rain, 'zh', 1, {'vol': 10, 'per': 4})
else:
    result = client.synthesis(text_normal, 'zh', 1, {'vol': 10, 'per': 4, 'spd': 5})

# 播放模块
if not isinstance(result, dict):
    with open('/home/clock/weather.mp3', 'wb') as f:
        f.write(result)
os.system('mpg123 "%s" > /dev/null 2>&1' % '/home/clock/weather.mp3')
