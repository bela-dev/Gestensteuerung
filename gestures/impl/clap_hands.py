import math

from gestures.gesture import Gesture
import utils.zoom_helper_old as ShortkeyHelper
from gestures.hand_value import HandPoint, getHandPointByIndex


class ClapHands(Gesture):

    def __init__(self):
        self.frameState = [None] * 180
        self.initLastPositions(180)

    def check(self, left, right, doValid):
        self.addLastPosition(left, right)
        if left is not None and right is not None:
            dx = abs(left.getPosition(HandPoint.MIDDLE_FINGER_TIP).x - right.getPosition(HandPoint.MIDDLE_FINGER_TIP).x)
            dy = abs(left.getPosition(HandPoint.MIDDLE_FINGER_TIP).y - right.getPosition(HandPoint.MIDDLE_FINGER_TIP).y)
            dist = math.sqrt(dx * dx + dy * dy)
            print(dist)


        # check if clap hands
        return False

    def onValid(self):
        self.initLastPositions(self.maxLastPositions)
        print("clap hands")

    def onInvalid(self):
        ShortkeyHelper.setHeartState(False)
