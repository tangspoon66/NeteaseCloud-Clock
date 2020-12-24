# NeteaseCloud-Clock
这是一个可以播放「网易云每日推荐歌曲」的闹钟，还可以给女朋友播报天气🌞☁️☔️

----

Linux部署项目肯定会有大大小小的问题出现，不会与我下面提供的步骤完全一致。遇到问题多网络搜索，大部分问题都会有解决方案。搜索结果没有的，就耐下心来多看原始文档，多尝试，多尝试，多尝试！

## 目录结构
.
├── Netease.py<br/>
├── README.md<br/>
├── TextToVoice.py<br/>
├── VolControl.py<br/>
├── getWeather.py<br/>
└── shutdown.py

## 材料准备

1. 树莓派 / 其他可以运行python脚本的开发板
2. 音响：pdd 8.8包邮

## 环境准备

### 系统版本

树莓派我用的是Linux raspberrypi 5.4.79-v7+ ，其他版本大同小异。

### mplayer

```
apt-get install mplayer
```

### baidu-api

```
pip install baidu-aip
```

## 账号准备

1. [百度TTS](https://ai.baidu.com/tech/speech/tts)：获取`APP_ID`， `API_KEY`， `SECRET_KEY`
2. [和风天气](https://www.qweather.com/)：获取城市`id`，`key`

## 开始搭建

### 下载脚本

```
sudo -i
mkdir /home/clock && cd /home/clock
git clone https://github.com/tangspoon66/NeteaseCloud-Clock.git
```

### 修改参数

脚本内有详细的参数说明，下面只列出需要需要修改的参数，如何修改请参考注释。

#### Netease.py

- url
- phone
- pwd

#### getWeather.py

- location
- key

#### TextToVoice.py

- APP_ID
- APP_KEY
- SECRET_KEY
- text_normal、text_lowtemp、text_rain

### 定时执行

```
crontab -e
```

定时每天`7:00`的闹钟：

```
# 一定要填写绝对路径！
00 7 * * * python /home/clock/Netease.py &>> /home/clock/log.log
00 7 * * * python /home/clock/VolControl.py
```

