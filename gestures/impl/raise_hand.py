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
            if not v:
                return False
            cD = v.getComparisonDistance() * 5.6
            if not v.isOpen(cD):
                return False

        mueX = 0
        for i in positions:
            mueX += i.getMidOfHand().x
        mueX = mueX / len(positions)

        sigma_X = 0
        for i in positions:
            sigma_X += (i.getMidOfHand().x - mueX) ** 2
        sigma_X = sigma_X / len(positions)
        sigma_X = math.sqrt(sigma_X)

        mueY = 0
        for i in positions:
            mueY += i.getMidOfHand().y
        mueY = mueY / len(positions)

        sigma_Y = 0
        for i in positions:
            sigma_Y += (i.getMidOfHand().y - mueY) ** 2
        sigma_Y = sigma_Y / len(positions)
        sigma_Y = math.sqrt(sigma_Y)

        comparisonDistance = positions[0].getComparisonDistance() * 5.6
        #print(sigma_X, ' ', sigma_Y)

        minSum = 0.01
        minMueY = 0.4

        if sigma_X > minSum or sigma_Y > minSum or mueY > minMueY or positions[0].getPosition(getHandPointByIndex(12)).y+(0.1 * comparisonDistance) > positions[0].getPosition(getHandPointByIndex(0)).y:
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