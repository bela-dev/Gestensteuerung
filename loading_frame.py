from tkinter import *
from PIL import ImageTk, Image
from screeninfo import get_monitors
import threading
from threading import Thread
from multiprocessing import Pool

class LoadingThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        self.root = Tk()

        x, y = (get_monitors()[0].width / 2.0) - 100.0, (get_monitors()[0].height / 2.0) - 100.0

        print(x)
        print(y)

        self.root.geometry("200x200+" + str(int(x)) + "+" + str(int(y)))

        img = Image.open("logo.jpg")
        img = img.resize((200, 200), Image.ANTIALIAS);

        img = ImageTk.PhotoImage(img)
        panel = Label(self.root, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")

        self.root.overrideredirect(1)
        self.root.mainloop()

    def end(self):
        try:
            self.root.quit()
            self.root.destroy()
        except:
            print("loading frame closed")

def initLoadingFrame():
    root = Tk()

    x, y = (get_monitors()[0].width / 2.0) - 100.0, (get_monitors()[0].height / 2.0) - 100.0

    print(x)
    print(y)

    root.geometry("200x200+" + str(int(x)) + "+" + str(int(y)))

    img = Image.open("logo.jpg")
    img = img.resize((200, 200), Image.ANTIALIAS);

    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")

    root.overrideredirect(1)
    root.mainloop()

thread = LoadingThread()
f = initLoadingFrame

def start():
    thread.setDaemon(True)
    thread.start()

def end():
    print("end")
    thread.end()
