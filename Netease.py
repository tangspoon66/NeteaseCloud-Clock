# -*- coding: utf-8 -*
import requests
import os

# NeteaseCloudMusicApi地址。如果是vps，把localhost换成vps的ip
url = 'http://localhost:3000'
phone = 'xxxxxx'
pwd = 'xxxxxxx'
song_id = []
songs_url = []

s = requests.session()


# 登陆
def login():
    login_url = url + '/login/cellphone'
    login = s.get(login_url, data={'phone': phone, 'password': pwd})
    try:
        if login.status_code is 200:
            print('恭喜！登陆成功！')
    except Exception as e:
        print('Exception', e)


# 获取每日推荐歌曲id，每日推荐32首
def getSongs_id():
    # 获取每日推荐歌曲字典
    dailySongs_url = url + '/recommend/songs'
    dailySongs_object = s.get(dailySongs_url)
    songs_dict = dailySongs_object.json()  # 获取node.js返回值
    # 获取所有id
    for list_index in range(0, 32):
        song_id.append(songs_dict['data']['dailySongs'][list_index]['id'])

    return song_id


# 获取播放url
def getSongs_url():
    getSongs_url = url + '/song/url'
    song_id = getSongs_id()
    data = {
        'id': song_id
    }
    song_url_object = s.post(getSongs_url, data=data)
    song_url_dict = song_url_object.json()

    # 根据song_id重新对song_url排序
    # 修复乱序播放的bug
    for i in range(0, 32):
        for j in range(0, 32):
            if song_id[i] == song_url_dict['data'][j]['id']:
                songs_url.append(song_url_dict['data'][j]['url'])
    # print('新的songs_url是：', new_songs_url)

    return songs_url


# mplayer
def playmusic():
    songs_url = getSongs_url()
    print('开始渐入')
    # 日后改善为多线程
    try:
        # 先播放第一首
        print('第一首歌')
        os.system('mpg123 "%s" > /dev/null 2>&1' % songs_url[0])
        # 播放天气
        for i in range(0, 2):
            print('播放天气')
            os.system('python /home/clock/TextToVoice.py')
        # 开始随机播放2～32首
        for i in range(1, 32):
            print('播放第' + str(i) + '首')
            os.system('mpg123 "%s" > /dev/null 2>&1' % songs_url[i])
    except Exception as e:
        print('Exception', e)


if __name__ == '__main__':
    login()
    getSongs_id()
    getSongs_url()
    playmusic()
