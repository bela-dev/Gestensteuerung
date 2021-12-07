'''
 Gestensteuerung für QAware 8Gate
'''
import cv2
import pyvirtualcam
from pyvirtualcam import PixelFormat
import mediapipe as mp
import numpy as np
import uuid
import os

'''
 Virtuelle Kamera einrichten
'''

# Virtuelle Kamera initialisieren
vc = cv2.VideoCapture(0)

if not vc.isOpened():
    raise RuntimeError('Could not open video source')

# Einstellungen der Virtuellen Kamera setzen
pref_width = 1920
pref_height = 1080
pref_fps = 25
vc.set(cv2.CAP_PROP_FRAME_WIDTH, pref_width)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, pref_height)
vc.set(cv2.CAP_PROP_FPS, pref_fps)

# Video Qualität der Virtuellen Kamera herausfinden
width = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = vc.get(cv2.CAP_PROP_FPS)

'''
Google Media Pipe einrichten
'''
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

'''
 Anwenden von Google Media Pipe zum erkennen von Gesten
'''

with pyvirtualcam.Camera(width, height, fps, fmt=PixelFormat.BGR) as cam:
    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:

        print("Successfully created virtual camera source(" + cam.device + ") with: " + str(width) + ":" + str(height) + " and " + str(fps) + "fps")

        while True:
            ret, frame = vc.read()

            # .. apply your filter ..

            cam.send(frame)
            cam.sleep_until_next_frame()

            # BGR 2 RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Flip on horizontal
            image = cv2.flip(image, 1)

            # Set flag
            image.flags.writeable = False

            # Detections
            results = hands.process(image)

            # Set flag to true
            image.flags.writeable = True

            # RGB 2 BGR
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Detections
            print(results)

            # Rendering results
            if results.multi_hand_landmarks:
                for num, hand in enumerate(results.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                              mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                              mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                              )

            cv2.imshow('Hand Tracking', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

