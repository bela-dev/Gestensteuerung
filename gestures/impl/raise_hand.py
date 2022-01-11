import math

from gestures.gesture import Gesture
import utils.zoom_helper as ShortkeyHelper

class RaiseHandGesture(Gesture):

    def __init__(self):
        self.initLastPositions(20)

    def check(self, left, right):
        self.addLastPosition(left, right)
        return self.checkOneHand(self.lastRightHandPositions) or self.checkOneHand(self.lastLeftHandPositions)


    def checkOneHand(self, positions):
        for v in positions:
            if not v or not v.isOpen():
                return False

        mueX = 0
        for i in positions:
            mueX += i.getMidOfHand().x
        mueX = mueX / len(positions)

        sumX = 0
        for i in positions:
            sumX += (i.getMidOfHand().x - mueX) ** 2
        sumX = sumX / len(positions)
        sumX = math.sqrt(sumX)

        mueY = 0
        for i in positions:
            mueY += i.getMidOfHand().y
        mueY = mueY / len(positions)

        sumY = 0
        for i in positions:
            sumY += (i.getMidOfHand().y - mueY) ** 2
        sumY = sumY / len(positions)
        sumY = math.sqrt(sumY)

        minSum = 0.01
        minMueY = 0.4

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
        ShortkeyHelper.setHandRaisedState(True)
        print("hand raised")

    def onInvalid(self):
        ShortkeyHelper.setHandRaisedState(False)