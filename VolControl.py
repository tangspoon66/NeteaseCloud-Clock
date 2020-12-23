import subprocess, os
import time


# a value between %0 and %100
def slowUp():
    volume = 70
    # 写一个range,0.3秒递增1个音量
    for volume in range(70, 100, 1):
        print(volume)
        time.sleep(0.3)
        command = ["amixer", "sset", "Headphone", "{}%".format(volume)]
        subprocess.Popen(command)


def slowDown():
    volume = 90
    for volume in range(90, 75, -1):
        print(volume)
        time.sleep(0.3)
        command = ["amixer", "sset", "Headphone", "{}%".format(volume)]
        subprocess.Popen(command)


if __name__ == '__main__':
    slowUp()
    # slowDown()
