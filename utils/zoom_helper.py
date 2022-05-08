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
    "heart": [Position2D(1230, 1000), Position2D(1120, 830)]
}

states = {
    "heart": False
}

def setClickActionState(key, value: bool):
    if not states.get(key) == value:
        toggleClickAction(key)

def toggleClickAction(key):
    states[key] = not states[key]
    for v in actions.get(key):
        thread = ClickActionThread(v)
        thread.start()


class ClickActionThread(threading.Thread):
    def __init__(self, pos):
        threading.Thread.__init__(self)
        self.pos = pos

    def run(self):
        click(self.pos.getX(), self.pos.getY())

'''
 Thumb Up
'''
thumbUp = False
def setThumbUpState(value: bool):
    global thumbUp
    if thumbUp != value:
        toggleThumbUp()

def toggleThumbUp():
    global time
    global thumbUp
    global autoClickRunning
    if not autoClickRunning:
        time = 0
        autoClickRunning = True
        click(1230, 1000)
        click(1120, 830)
        thumbUp = not thumbUp
        autoClickRunning = False


'''
Heart
'''
heart = False
def setHeartState(value: bool):
    global heart
    if heart != value:
        toggleHeart()

def toggleHeart():
    global time, heart, autoClickRunning
    if not autoClickRunning:
        time = 0
        autoClickRunning = True
        click(1170, 1050)
        click(1210, 960)
        heart = not heart
        autoClickRunning = False