import os
import platform
import requests
import pynput
from playsound import playsound


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


def play_music():
    #  requests.get('https://api.vvhan.com/api/rand.music?sort=热歌榜')
    r = requests.get('https://api.uomg.com/api/rand.music?sort=热歌榜&format=music')
    with open("music.mp3", "wb") as code:
        code.write(r.content)
    playsound("music.mp3")


play_music()