import keyboard

muted = False

def openDesktop():
    keyboard.send("windows+d")

def toggleMute():
    keyboard.send("alt+a")

def setHandState(value: bool):
    global muted
    if muted != value:
        toggleHand()

def toggleHand():
    global muted
    keyboard.send("alt+y")
    muted = not muted
