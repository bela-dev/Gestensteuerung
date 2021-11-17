import math

from gestures.gesture import Gesture
import utils.shortkey_helper as ShortkeyHelper

class ThumbUpGesture(Gesture):

    def __init__(self):
        self.initLastPositions(20)

    def check(self, left, right):
        self.addLastPosition(left, right)
        return self.checkOneHand(self.lastRightHandPositions) or self.checkOneHand(self.lastLeftHandPositions)


    def checkOneHand(self, positions):
        for v in positions:
            if not v or not v.isOpen():
                self.onInvalid()
                return False



        if sumX > minSum or sumY > minSum:
            self.onInvalid()
            return False
        if mueY > minMueY:
            self.onInvalid()
            return False
        self.onValid()
        return True



    def onValid(self):
        self.initLastPositions(self.maxLastPositions)
        ShortkeyHelper.setMuteState(True)
        print("hand raised")

    def onInvalid(self):
        ShortkeyHelper.setMuteState(False)
        print("hand unraised")