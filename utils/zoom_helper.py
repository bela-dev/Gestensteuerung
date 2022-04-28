import keyboard
import pyautogui

QAware = False
Vollbild = True
time = 0

muted = False
handRaised = False
thumbUp = False
heart = False
okHand = False
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

autoClickRunning = False

def click(x, y):
    global time
    ny = y
    nx = x
    if Vollbild:
        ny += 50
    if time == 1 and not QAware:
        ny += 50
    pyautogui.click(nx, ny)
    time += 1

def openDesktop():
    keyboard.send("windows+d")

def setMuteState(value: bool):
    global muted
    if muted != value:
        toggleMute()

def toggleMute():
    global muted
    keyboard.send("alt+a")
    muted = not muted

def setHandRaisedState(value: bool):
    global handRaised
    if handRaised != value:
        toggleHandRaised()

def toggleHandRaised():
    global handRaised
    keyboard.send("alt+y")
    handRaised = not handRaised

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
        click(1230, 1000)
        click(1275, 830)
        heart = not heart
        autoClickRunning = False

def setOkHandState(value: bool):
    global okHand
    if okHand != value:
        toggleOkHand()

def toggleOkHand():
    global time
    global okHand
    global autoClickRunning
    if not autoClickRunning:
        time = 0
        autoClickRunning = True
        click(1230, 1000)
        click(1375, 830)
        pyautogui.press("o")
        pyautogui.press("k")
        click(1075, 670)
        okHand = not okHand
        autoClickRunning = False
