import os
import platform
import keyboard
from playsound import playsound
from random import choice
import schedule
import time


def mute():
    if platform.system() == 'Darwin':
        os.system("osascript -e 'set volume with output muted'")
    if platform.system() == 'Windows':
        os.system("nircmd.exe mutesysvolume 1")


def unmute():
    if platform.system() == 'Darwin':
        os.system("osascript -e 'set volume without output muted'")
    if platform.system() == 'Windows':
        os.system("nircmd.exe mutesysvolume 0")
        os.system("nircmd.exe setsysvolume 50000")


def play_music():
    def try_play():
        music = choice(music_list)
        print("play {}".format(music))
        try:
            playsound("D:\Music" + "\\" + music)
        except BaseException as e:
            print("error" + str(e))
            try_play()


    unmute()
    dir = "D:\Music"
    music_list = []
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in files:
            music_list.append(name)
            print(name)
    try_play()
    mute()


schedule.every().day.at("7:50").do(play_music)

schedule.every().day.at("09:00").do(play_music)
schedule.every().day.at("09:10").do(play_music)
schedule.every().day.at("09:20").do(play_music)

keyboard.add_hotkey('k', mute)
while True:
    schedule.run_pending()
    time.sleep(10)
