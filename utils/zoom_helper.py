import keyboard
import pyautogui
import utils.screen_helper as ScreenHelper

# Pyautogui konfigurieren
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

autoClickRunning = False

def click(x, y):
    if ScreenHelper.containsEntryByTitleContains("Zoom Meeting"):
        print("Zoom isn't open!")
    else:
        ScreenHelper.relClick(x, y, ScreenHelper.getEntryByTitleContains("Zoom Meeting"))

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
        click(950/1450, 915/950)
        #click(1210, 960)
        heart = not heart
        autoClickRunning = False