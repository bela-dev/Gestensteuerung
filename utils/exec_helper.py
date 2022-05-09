import math
import time
import pyautogui
import threading

from pynput.keyboard import Key, Controller


keyboard = Controller()

def decreaseVolumeBy2():
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)

def increaseVolumeBy2():
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)

def increaseVolume(val):
    for i in range(math.ceil(val / 2.0)):
        increaseVolumeBy2()


def decreaseVolume(val):
    for i in range(math.ceil(val / 2.0)):
        decreaseVolumeBy2()

def changeVolume(val):
    if val > 0:
        increaseVolume(val)
    else:
        decreaseVolume(-val)

def openAltTab():
    thread = OpenAltTabThread()
    thread.start()

def closeAltTab():
    thread = CloseAltTabThread()
    thread.start()

def rightAltTab():
    thread = RightAltTabThread()
    thread.start()

def leftAltTab():
    thread = LeftAltTabThread()
    thread.start()

class RightAltTabThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        pyautogui.press('tab')

class LeftAltTabThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        pyautogui.keyDown('shift')
        time.sleep(.01)
        pyautogui.press('tab')
        time.sleep(.01)
        pyautogui.keyUp('shift')

class CloseAltTabThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        pyautogui.keyUp('alt')

class OpenAltTabThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        pyautogui.keyDown('alt')
        time.sleep(.01)
        pyautogui.press('tab')