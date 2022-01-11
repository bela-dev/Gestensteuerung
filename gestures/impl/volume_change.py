import math

from gestures.position import Position

from gestures.gesture import Gesture
import utils.exec_helper as ExecHelper
from gestures.hand_value import HandPoint, getHandPointByIndex


class VolumeChangeGesture(Gesture):

    def __init__(self):
        self.initLastPositions(20)
        self.ready = False

    def check(self, left, right):
        self.addLastPosition(left, right)
        return self.checkOneHand(self.lastRightHandPositions) or self.checkOneHand(self.lastLeftHandPositions)

    def volumeChangeReady(self, v):

        wrist_y = v.getPosition(HandPoint.WRIST).y
        possible_difference = 0.1

        for i in range(20):
            cur_y = v.getPosition(getHandPointByIndex(i)).y
            if abs(wrist_y-cur_y) > possible_difference:
                return False

        return True

    def inOnePosition(self, positions):

        possible_difference = 0.1
        first_pos = positions[0].getPosition(HandPoint.WRIST)

        for v in positions:
            if not v:
                return False

            cur_x = v.getPosition(HandPoint.WRIST).x
            cur_y = v.getPosition(HandPoint.WRIST).y

            if max(abs(first_pos.x - cur_x), abs(first_pos.y - cur_y)) > possible_difference:
                return False

        return True

    def checkOneHand(self, positions):
        for v in positions:
            if not v:
                return False
            if not self.volumeChangeReady(v):
                self.onInvalid()
                return False

        if not self.ready and self.inOnePosition(positions):
            self.ready = True
            print("ready")

        if self.ready:

            print((positions[0].getPosition(HandPoint.WRIST).y - positions[1].getPosition(HandPoint.WRIST).y)*20)

        self.onValid()
        return True

    def onValid(self):
        self.initLastPositions(self.maxLastPositions)
        print("volume change")

    def onInvalid(self):
        self.ready = False
        pass
