import os


def mute():
    os.system("nircmd.exe mutesysvolume 1")


def unmute():
    os.system("nircmd.exe mutesysvolume 0")


def play_music():
    