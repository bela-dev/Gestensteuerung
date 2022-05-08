import math

from gestures.gesture import Gesture
import utils.zoom_helper_old as ShortkeyHelper
from gestures.hand_value import HandPoint, getHandPointByIndex


class OkHandGesture(Gesture):

    def __init__(self):
        self.initLastPositions(20)
        #self.alreadyExec = False

    def check(self, left, right, doValid):
        self.addLastPosition(left, right)
        return self.checkOneHand(self.lastRightHandPositions, doValid) or self.checkOneHand(self.lastLeftHandPositions, doValid)

    def is_equal(self, x1, y1, x2, y2, cD):
        TRESHOLD = 0.05 * cD
        dx = x1-x2
        dy = y1-y2
        dist = math.sqrt(dx*dx+dy*dy)

        if dist > TRESHOLD:
            return False
        else:
            return True

    def isOkHand(self, v):

        comparisonDistance = v.getComparisonDistance() * 5.3

        a = v.getPosition(HandPoint.THUMB_TIP)
        b = v.getPosition(HandPoint.INDEX_FINGER_TIP)

        if not self.is_equal(a.x, a.y, b.x, b.y, comparisonDistance):
            return False

        # 6 unter 12, 16, 20

        ysix = v.getPosition(getHandPointByIndex(6)).y
        other = [v.getPosition(getHandPointByIndex(i)).y for i in [12, 16, 20]]

        for yfinger in other:
            if yfinger > ysix:
                return False

        if v.getPosition(getHandPointByIndex(2)).y - (0.165 * comparisonDistance) < v.getPosition(getHandPointByIndex(6)).y:
            return False

        return True

    def checkOneHand(self, positions, doValid):
        for v in positions:
            if not v:
                return False
            if not self.isOkHand(v):
                self.onInvalid()
                return False
        if doValid:
            self.onValid()
        return True

    def onValid(self):
        self.initLastPositions(self.maxLastPositions)
        ShortkeyHelper.setOkHandState(True)
        print("ok hand")

    def onInvalid(self):
        ShortkeyHelper.setOkHandState(False)
