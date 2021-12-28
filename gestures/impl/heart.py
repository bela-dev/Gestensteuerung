import math

from gestures.gesture import Gesture
import utils.shortkey_helper as ShortkeyHelper
from gestures.hand_value import HandPoint, getHandPointByIndex


class HeartGesture(Gesture):

    def __init__(self):
        self.initLastPositions(20)

    def check(self, left, right):
        self.addLastPosition(left, right)
        return self.checkBothHands(self.lastLeftHandPositions,self.lastRightHandPositions)

    def isHeart(self, lef, rig):
        # Daumen gleiche Position

        # 8, 12, 16, 20
        avg_x = 0
        avg_y = 0
        for i in [8, 12, 16, 20]:
            avg_x += lef.getPosition(getHandPointByIndex(i)).x+rig.getPosition(getHandPointByIndex(i)).x
            avg_y += lef.getPosition(getHandPointByIndex(i)).y+rig.getPosition(getHandPointByIndex(i)).y
        avg_x /= 8
        avg_y /= 8

        min_diff = 0.05
        min_range = 0.1

        for i in [8, 12, 16, 20]:
            if abs(lef.getPosition(getHandPointByIndex(i)).x-avg_x) > min_diff:
                return False
            if abs(rig.getPosition(getHandPointByIndex(i)).x-avg_x) > min_diff:
                return False
            if abs(lef.getPosition(getHandPointByIndex(i)).y-avg_y) > min_diff:
                return False
            if abs(rig.getPosition(getHandPointByIndex(i)).y-avg_y) > min_diff:
                return False

        thumb_xl = lef.getPosition(HandPoint.THUMB_TIP).x
        thumb_xr = rig.getPosition(HandPoint.THUMB_TIP).x
        thumb_yl = lef.getPosition(HandPoint.THUMB_TIP).y
        thumb_yr = rig.getPosition(HandPoint.THUMB_TIP).y

        if abs(thumb_xl-thumb_xr) > min_diff:
            return False
        if abs(thumb_yl-thumb_yr) > min_diff:
            return False

        if (thumb_yl+thumb_yr)/2-avg_y < min_range:
            return False

        return True

    def checkBothHands(self, positions_left, positions_right):
        for i in range(min(len(positions_left),len(positions_right))):
            if not positions_left[i] or not positions_right[i]:
                return False
            if not self.isHeart(positions_left[i], positions_right[i]):
                self.onInvalid()
                return False

        self.onValid()
        return True

    def onValid(self):
        self.initLastPositions(self.maxLastPositions)
        ShortkeyHelper.setHeartState(True)
        print("heart")

    def onInvalid(self):
        ShortkeyHelper.setHeartState(False)