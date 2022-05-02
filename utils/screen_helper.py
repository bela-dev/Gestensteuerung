import win32gui
import pyautogui

screenEntries = []

'''
 Die Informationen über alle geöffneten Fenster werden neu geladen
 und in dem Feld screenEntries gespeichert
'''
def refresh():
    screenEntries.clear()
    win32gui.EnumWindows(insertEntry, None)

'''
 Die nötigen Informationen aus einer Fenster instance werden gefiltert
 und als Objekt der Klasse ScreenEntry in dem Feld screenEntries gespeichert
'''
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


'''
 Gibt einen Wahrheitswert zurück, je nachdem, ob ein Eintrag
 mit dem als Parameter übergebenen Titel existiert
'''
def containsEntry(title):
    for item in screenEntries:
        if item.getTitle() == title:
            return True
    return False


'''
 Gibt das gespeicherte Objekt der Klasse ScreenEntry, falls vorhanden,
 identifiziert über den Titel zurück
'''
def getEntry(title):
    for item in screenEntries:
        if item.getTitle() == title:
            return item
    return None


'''
 Ähnlich wie getEntry(): Gibt einen Wahrheitswert zurück,
 jetzt mit der Bedingung, dass Parameter nur im Fenster Titel
 enthalten sein soll
'''
def getEntryByTitleContains(title):
    for item in screenEntries:
        if title in item.getTitle():
            return item
    return None

'''
 Führt mit pyautogui einen Klick an den übergebenen Koordinaten aus
'''
def click(x, y):
    pyautogui.click(x, y)

'''
 Führt einen Klick an dem Produkt aus dem übergebenem X/Y und
 der Breite/Höhe des übergebenen Referenz Fensters aus
'''
def relClick(relX, relY, screenEntry):
    x = screenEntry.getX() + screenEntry.getWidth() * relX
    y = screenEntry.getY() + screenEntry.getHeight() * relY
    pyautogui.click(x, y)


'''
 Führt relClick() aus, nur dass ganze Zahlen als x und y
 übergeben werden und die relativen Koordinaten erst noch
 mit FullHD berechnet werden
'''
def relClickFullHD(x, y, screenEntry):
    relClick(x / 1920, y / 1080, screenEntry)


'''
 Klasse zum Speichern aller wichtigen Attribute
 für ein Fenster
'''
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