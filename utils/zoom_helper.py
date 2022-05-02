import keyboard
import pyautogui
import utils.screen_helper as ScreenHelper

time = 0

muted = False
handRaised = False

thumbUp = False
heart = False

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

autoClickRunning = False

def click(x, y):
    if ScreenHelper.getEntryByTitleContains("Zoom Meeting") == None:
        print("Zoom isn't open!")
    else:
        global time
        ScreenHelper.relClick(x, y, ScreenHelper.getEntryByTitleContains("Zoom Meeting"))
        time += 1

'''
 Mute
'''
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
def setHeartState(value: bool):
    global heart
    if heart != value:
        toggleHeart()

def toggleHeart():
    global time
    global heart
    global autoClickRunning
    if not autoClickRunning:
        time = 0
        autoClickRunning = True
        click(950/1450, 915/950)
        #click(1210, 960)
        heart = not heart
        autoClickRunning = False