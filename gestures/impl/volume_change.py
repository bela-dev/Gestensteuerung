import math

from gestures.position import Position

from gestures.gesture import Gesture
import utils.exec_helper as ExecHelper
from gestures.hand_value import HandPoint, getHandPointByIndex


class VolumeChangeGesture(Gesture):

    def __init__(self):
        self.initLastPositions(20)

    def check(self, left, right, doValid):
        self.addLastPosition(left, right)
        return (self.lenLeftPosition() >= 2 and self.checkOneHand(self.lastLeftHandPositions)) \
               or (self.lenRightPosition() >= 2 and self.checkOneHand(self.lastRightHandPositions))

    def volumeChangeReady(self, v):

        wrist_y = v.getPosition(HandPoint.WRIST).y

        cD = v.getComparisonDistance() * 5.6
        possible_difference = 0.15 * cD

        for i in range(20):
            cur_y = v.getPosition(getHandPointByIndex(i)).y
            if abs(wrist_y-cur_y) > possible_difference:
                return False

        return True

    def checkOneHand(self, positions):
        for v in positions:
            if not v:
                return False
            if not self.volumeChangeReady(v):
                self.onInvalid()
                return False

        cD = positions[0].getComparisonDistance() * 5.6
        ExecHelper.changeVolume((positions[0].getPosition(HandPoint.WRIST).y
                                 - positions[1].getPosition(HandPoint.WRIST).y)*10 / cD)

        self.onValid()
        return True

    def onValid(self):
        print("volume change")

    def onInvalid(self):
        pass
