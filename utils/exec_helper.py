import math

from pynput.keyboard import Key, Controller

keyboard = Controller()

def decreaseVolumeBy2():
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)

def increaseVolumeBy2():
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)

def increaseVolume(val):
    for i in range(math.ceil(val/2.0)):
        increaseVolumeBy2()


def decreaseVolume(val):
    for i in range(math.ceil(val / 2.0)):
        decreaseVolumeBy2()

def changeVolume(val):
    if val > 0:
        increaseVolume(val)
    else:
        decreaseVolume(-val)
