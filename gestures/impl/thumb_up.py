import math

from gestures.gesture import Gesture
import utils.zoom_helper as ShortkeyHelper
from gestures.hand_value import HandPoint, getHandPointByIndex


class ThumbUpGesture(Gesture):

    def __init__(self):
        self.initLastPositions(20)

    def check(self, left, right, doValid):
        self.addLastPosition(left, right)
        return self.checkOneHand(self.lastRightHandPositions, doValid) or self.checkOneHand(self.lastLeftHandPositions, doValid)

    def isThumbUp(self, v):
        thumb_y = v.getPosition(HandPoint.THUMB_TIP).y
        mn_x = 10000000
        mx_x = -10000000
        avg_y = 0
        for i in range(21):
            cur_x = v.getPosition(getHandPointByIndex(i)).x
            cur_y = v.getPosition(getHandPointByIndex(i)).y
            mn_x = min(mn_x,cur_x)
            mx_x = max(mx_x,cur_x)
            avg_y += cur_y

        avg_y /= 21

        comparisonDistance = v.getComparisonDistance() * 5

        max_range = 0.2 * comparisonDistance
        min_diff = 0.25 * comparisonDistance

        if thumb_y+min_diff > avg_y or mx_x-mn_x > max_range:
            #self.onInvalid()
            return False

        #self.onValid()
        return True

    def checkOneHand(self, positions, doValid):
        for v in positions:
            if not v:
                return False
            if not self.isThumbUp(v):
                self.onInvalid()
                return False
        if doValid:
            self.onValid()
        return True

    def onValid(self):
        self.initLastPositions(self.maxLastPositions)
        ShortkeyHelper.setClickActionState("thumbup", True)
        print("thumb up")

    def onInvalid(self):
        ShortkeyHelper.setClickActionState("thumbup", False)
