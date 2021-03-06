'''
 Gestensteuerung für QAware 8Gate
'''

import loading_frame as LoadingFrame
print("start")
LoadingFrame.start()

import cv2
import pyvirtualcam
from pyvirtualcam import PixelFormat
import mediapipe as mp

import utils.screen_helper as ScreenHelper

from gestures.hand_value import HandValue

import utils.zoom_helper as ZoomHelper

from gestures.impl.raise_hand import RaiseHandGesture
from gestures.impl.mute import MuteGesture
from gestures.impl.thumb_up import ThumbUpGesture
from gestures.impl.heart import HeartGesture
from gestures.impl.ok_hand import OkHandGesture
from gestures.impl.alt_tab import AltTabGesture
from gestures.impl.volume_change import VolumeChangeGesture

'''
 Virtuelle Kamera einrichten
'''

# Virtuelle Kamera initialisieren
print("main")
vc = cv2.VideoCapture(0)

if not vc.isOpened():
    raise RuntimeError('Could not open video source')

# Einstellungen der Virtuellen Kamera setzen
pref_width = 1280
pref_height = 720
pref_fps = 25
vc.set(cv2.CAP_PROP_FRAME_WIDTH, pref_width)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, pref_height)
vc.set(cv2.CAP_PROP_FPS, pref_fps)

# Video Qualität der Virtuellen Kamera herausfinden
width = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = vc.get(cv2.CAP_PROP_FPS)

print(fps)

'''
Google Media Pipe einrichten
'''
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

LoadingFrame.end()

'''
Gestenliste erstellen
'''
gestures = [MuteGesture(), RaiseHandGesture(), AltTabGesture(), ThumbUpGesture(), HeartGesture(), OkHandGesture(), VolumeChangeGesture()]

activeGesture = None

ScreenHelper.refresh()


'''
 Anwenden von Google Media Pipe zum erkennen von Gesten
'''
with pyvirtualcam.Camera(width, height, fps, fmt=PixelFormat.BGR) as cam:
    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:

        print("Successfully created virtual camera source(" + cam.device + ") with: " + str(width) + ":" + str(height) + " and " + str(fps) + "fps")

        while True:

            ScreenHelper.refresh()

            # Momentanes Bild empfangen
            ret, frame = vc.read()

            cam.send(frame)
            cam.sleep_until_next_frame()

            # Bild Optionen setzen
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.flip(image, 1)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            #print(results.multi_hand_landmarks)
            if results.multi_hand_landmarks:

                # Convert hand info
                left = None
                right = None
                for num, hand in enumerate(results.multi_hand_landmarks):
                    if num == 0:
                        right = HandValue(False, hand)
                    else:
                        left = HandValue(True, hand)

                # Check hands
                allFalse = True
                if activeGesture is None:
                    for g in gestures:
                        if g.check(left, right, True):
                            allFalse = False
                            lastTime = True
                            activeGesture = g
                else:
                    if not activeGesture.check(left, right, False):
                        if lastTime:
                            lastTime = False
                        else:
                            activeGesture = None
                            lastTime = True
                    else:
                        allFalse = False
                        lastTime = True
                if allFalse:
                    activeGesture = None



            # Bild ausgeben
            if results.multi_hand_landmarks:
                for num, hand in enumerate(results.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                              mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                              mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                              )

            cv2.imshow('Gestenerkennung', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

