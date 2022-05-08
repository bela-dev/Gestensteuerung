import math

from gestures.gesture import Gesture
import utils.zoom_helper as ShortkeyHelper
from gestures.hand_value import getHandPointByIndex


class RaiseHandGesture(Gesture):

    def __init__(self):
        self.initLastPositions(15)

    def check(self, left, right, doValid):
        self.addLastPosition(left, right)
        return self.checkOneHand(self.lastRightHandPositions, doValid) or self.checkOneHand(self.lastLeftHandPositions, doValid)


    def checkOneHand(self, positions, doValid):
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

        comparisonDistance = positions[0].getComparisonDistance() * 5.6

        minSum = 0.01 * comparisonDistance
        minMueY = 0.4 * comparisonDistance

        if sumX > minSum or sumY > minSum or mueY > minMueY or positions[0].getPosition(getHandPointByIndex(12)).y+(0.1 * comparisonDistance) > positions[0].getPosition(getHandPointByIndex(0)).y:
            self.onInvalid()
            return False
        if doValid:
            self.onValid()
        return True



    def onValid(self):
        self.initLastPositions(self.maxLastPositions)
        ShortkeyHelper.setHandRaisedState(True)
        print("hand raised")

    def onInvalid(self):
        ShortkeyHelper.setHandRaisedState(False)