import pyautogui

from gestures.gesture import Gesture
import utils.zoom_helper as ShortkeyHelper
from gestures.hand_value import HandPoint, getHandPointByIndex


class HeartGesture(Gesture):

    def __init__(self):
        self.initLastPositions(20)

    def check(self, left, right, doValid):
        self.addLastPosition(left, right)
        return self.checkBothHands(self.lastLeftHandPositions,self.lastRightHandPositions, doValid)

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

        comparisonDistance = lef.getComparisonDistance()*5

        min_diff = 0.05*comparisonDistance
        min_range = 0.1*comparisonDistance

        cnt = 0

        for i in [8, 12, 16, 20]:
            #print(abs(lef.getPosition(getHandPointByIndex(i)).x-avg_x), ' ', abs(rig.getPosition(getHandPointByIndex(i)).x-avg_x), ' ', abs(lef.getPosition(getHandPointByIndex(i)).y-avg_y), ' ', abs(rig.getPosition(getHandPointByIndex(i)).y-avg_y))
            if abs(lef.getPosition(getHandPointByIndex(i)).x-avg_x) > min_diff:
                cnt += 1
            if abs(rig.getPosition(getHandPointByIndex(i)).x-avg_x) > min_diff:
                cnt += 1
            if abs(lef.getPosition(getHandPointByIndex(i)).y-avg_y) > min_diff:
                cnt += 1
            if abs(rig.getPosition(getHandPointByIndex(i)).y-avg_y) > min_diff:
                cnt += 1

        thumb_xl = lef.getPosition(HandPoint.THUMB_TIP).x
        thumb_xr = rig.getPosition(HandPoint.THUMB_TIP).x
        thumb_yl = lef.getPosition(HandPoint.THUMB_TIP).y
        thumb_yr = rig.getPosition(HandPoint.THUMB_TIP).y

        if cnt > 2:
            return False

        #print(abs(thumb_xl-thumb_xr), ' ', abs(thumb_yl-thumb_yr))
        if abs(thumb_xl-thumb_xr) > min_diff:
            return False
        if abs(thumb_yl-thumb_yr) > min_diff:
            return False

        #print((thumb_yl+thumb_yr)/2-avg_y)
        if (thumb_yl+thumb_yr)/2-avg_y < min_range:
            return False

        return True

    def checkBothHands(self, positions_left, positions_right, doValid):
        for i in range(min(len(positions_left),len(positions_right))):
            if not positions_left[i] or not positions_right[i]:
                return False
            if not self.isHeart(positions_left[i], positions_right[i]):
                self.onInvalid()
                return False
        if doValid:
            self.onValid()
        return True

    def onValid(self):
        self.initLastPositions(self.maxLastPositions)
        ShortkeyHelper.toggleClickAction("heart")
        print("heart")

    def onInvalid(self):
        pass
