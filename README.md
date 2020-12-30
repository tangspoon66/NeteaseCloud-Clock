# NeteaseCloud-Clock
这是一个可以播放「网易云每日推荐歌曲」的闹钟，还可以给女朋友播报天气🌞☁️☔️

<img src="https://picbed.tangspoon.cn/uPic/WechatIMG1204.jpeg" alt="WechatIMG1204" style="zoom:50%;" />

----

Linux部署项目肯定会有大大小小的问题出现，不会与我下面提供的步骤完全一致。遇到问题多网络搜索，大部分问题都会有解决方案。搜索结果没有的，就耐下心来多看原始文档，多尝试，多尝试，多尝试！

## 一、目录结构

.
|_ tree.py<br/>
|_ getWeather.py<br/>
|_ shutdown.py<br/>
|_ README.md<br/>
|_ Netease.py<br/>
|_ VolControl.py

## 二、材料准备

1. 树莓派 / 其他可以运行python脚本的开发板
2. 音响：pdd 8.8包邮

## 三、环境准备

### 1. 系统版本

树莓派我用的是Linux raspberrypi 5.4.79-v7+ ，其他版本大同小异。

### 2. NeteaseCloudMusicApi搭建

可以选择直接搭建在树莓派、VPS上，确保可以稳定长时间运行。搭建方法请看[官方文档](https://binaryify.github.io/NeteaseCloudMusicApi/#/?id=%e5%ae%89%e8%a3%85)。

### 3. mplayer

```
apt-get install mplayer
```

### 4. baidu-api

```
pip install baidu-aip
```

## 四、账号准备

1. [百度TTS](https://ai.baidu.com/tech/speech/tts)：获取`APP_ID`， `API_KEY`， `SECRET_KEY`
2. [和风天气](https://www.qweather.com/)：获取城市`id`，`key`

## 五、开始搭建

### 1. 下载脚本

```
sudo -i
mkdir /home/clock && cd /home/clock
git clone https://github.com/tangspoon66/NeteaseCloud-Clock.git
```

### 2. 修改参数

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

### 3. 定时执行

```
crontab -e
```

定时每天`7:00`的闹钟：

```
# 一定要填写绝对路径！
00 7 * * * python /home/clock/Netease.py &>> /home/clock/log.log
00 7 * * * python /home/clock/VolControl.py
```

## 六、过程记录

1. [智能闹钟（一）｜macOS 入门使用树莓派 3B+](https://blog.tangspoon.cn/2020/12/19/%E6%99%BA%E8%83%BD%E9%97%B9%E9%92%9F%EF%BC%88%E4%B8%80%EF%BC%89%EF%BD%9CmacOS%E5%85%A5%E9%97%A8%E4%BD%BF%E7%94%A8%E6%A0%91%E8%8E%93%E6%B4%BE3B/#more)
2. [智能闹钟（二）｜使用「和风天气、百度语音合成」API进行天气的播报](http://localhost:4000/2020/12/21/%E6%99%BA%E8%83%BD%E9%97%B9%E9%92%9F%EF%BC%88%E4%BA%8C%EF%BC%89%EF%BD%9C%E4%BD%BF%E7%94%A8%E3%80%8C%E5%92%8C%E9%A3%8E%E5%A4%A9%E6%B0%94%E3%80%81%E7%99%BE%E5%BA%A6%E8%AF%AD%E9%9F%B3%E5%90%88%E6%88%90%E3%80%8DAPI%E8%BF%9B%E8%A1%8C%E5%A4%A9%E6%B0%94%E7%9A%84%E6%92%AD%E6%8A%A5/#more)
3. [智能闹钟（三）| 使用「网易云音乐 NodeJS 版 API 接口」播放每日推荐歌曲](https://blog.tangspoon.cn/2020/12/22/%E6%99%BA%E8%83%BD%E9%97%B9%E9%92%9F%EF%BC%88%E4%B8%89%EF%BC%89%7C%20%E4%BD%BF%E7%94%A8%E3%80%8C%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90NodeJS%E7%89%88API%E6%8E%A5%E5%8F%A3%E3%80%8D%E8%8E%B7%E5%8F%96%E6%AF%8F%E6%97%A5%E6%8E%A8%E8%8D%90%E6%AD%8C%E6%9B%B2/#more)

## 七、TODO

- [x] ~~修改乱序播放的bug~~
- [ ] 优雅地「关闭」闹钟
- [ ] 优雅地「设置」闹钟

## 八、感谢

网易云音乐 NodeJS 版 API：https://binaryify.github.io/NeteaseCloudMusicApi/#/

