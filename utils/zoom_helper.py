import keyboard
import pyautogui
import utils.screen_helper as ScreenHelper
from gestures.position import Position2D
import threading

# Pyautogui konfigurieren
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

autoClickRunning = False

def click(x, y):
    if ScreenHelper.containsEntryByTitleContains("Zoom Meeting"):
        ScreenHelper.relClickFullHD(x, y, ScreenHelper.getEntryByTitleContains("Zoom Meeting"))
    else:
        print("Zoom isn't open!")

'''
 Mute ausführen
'''
muted = False
def setMuteState(value: bool):
    global muted
    if muted != value:
        toggleMute()

def toggleMute():
    global muted
    keyboard.send("alt+a")
    muted = not muted

'''
 Hand Raise
'''
handRaised = False
def setHandRaisedState(value: bool):
    global handRaised
    if handRaised != value:
        toggleHandRaised()

def toggleHandRaised():
    global handRaised
    keyboard.send("alt+y")
    handRaised = not handRaised


'''
 Click Actions

'''

actions = {
    "heart": [Position2D(1230, 1000), Position2D(1120, 830)],
    "thumbup": [Position2D(1230, 1000), Position2D(1120, 830)]
}

states = {}

for v in actions.keys():
    states[v] = False


def setClickActionState(key, value: bool):
    if not states.get(key) == value:
        toggleClickAction(key)


def toggleClickAction(key):
    states[key] = not states[key]
    for v in actions.get(key):
        click(v.getX(), v.getY())