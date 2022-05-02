import win32gui
import pyautogui

screenEntries = []

def refresh():
    screenEntries = []
    win32gui.EnumWindows(insertEntry, None)
    for item in screenEntries:
        print(item.getTitle())


def insertEntry(hwnd, extra):
    # get window title
    txt = win32gui.GetWindowText(hwnd)
    # only insert not empty and not double values
    if len(txt) != 0 and not containsEntry(txt):
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        screenEntries.append(ScreenEntry(txt, x, y, w, h))


def containsEntry(title):
    for item in screenEntries:
        if item.getTitle() == title:
            return True
    return False


def getEntry(title):
    for item in screenEntries:
        if item.getTitle() == title:
            return item
    return None


def getEntryByTitleContains(title):
    for item in screenEntries:
        if title in item.getTitle():
            return item
    return None


def relClickFullHD(x, y, screenEntry):
    print(x / 1920)
    print(y / 1080)
    print(screenEntry.getWidth())
    print(screenEntry.getHeight())
    print(screenEntry.getX())
    print(screenEntry.getY())
    relClick(x / 1920, y / 1080, screenEntry)


def relClick(relX, relY, screenEntry):
    x = screenEntry.getX() + screenEntry.getWidth() * relX
    y = screenEntry.getY() + screenEntry.getHeight() * relY
    print(x)
    print(y)
    pyautogui.click(x, y)


class ScreenEntry:

    def __init__(self, txt, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.title = txt

    def getX(self):
        return self.x + 8

    def getY(self):
        return self.y + 8

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h

    def getTitle(self):
        return self.title