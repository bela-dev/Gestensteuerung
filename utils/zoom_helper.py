import keyboard
import pyautogui

muted = False
handRaised = False
thumbUp = False
heart = False
okHand = False
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False

autoClickRunning = False

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
    global thumbUp
    global autoClickRunning
    if not autoClickRunning:
        autoClickRunning = True
        pyautogui.click(x=1280, y=1000)
        pyautogui.click(x=1175, y=890)
        thumbUp = not thumbUp
        autoClickRunning = False

def setHeartState(value: bool):
    global heart
    if heart != value:
        toggleHeart()

def toggleHeart():
    global heart
    global autoClickRunning
    if not autoClickRunning:
        autoClickRunning = True
        pyautogui.click(x=1280, y=1000)
        pyautogui.click(x=1330, y=880)
        heart = not heart
        autoClickRunning = False

def setOkHandState(value: bool):
    global okHand
    if okHand != value:
        toggleOkHand()

def toggleOkHand():
    global okHand
    global autoClickRunning
    if not autoClickRunning:
        autoClickRunning = True
        pyautogui.click(x=1280, y=1000)
        pyautogui.click(x=1425, y=880)
        pyautogui.press("o")
        pyautogui.press("k")
        pyautogui.click(x=1140,y=671)
        okHand = not okHand
        autoClickRunning = False
