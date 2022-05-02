import math

from gestures.gesture import Gesture
from gestures.hand_value import Hand, HandPoint
import utils.exec_helper as ExecHelper


class AltTabGesture(Gesture):

    def __init__(self):
        self.initLastPositions(20)
        self.activeHand = None
        self.lastMidActiveHand = None

    def check(self, left, right, doValid):
        self.addLastPosition(left, right)
        if self.lenLeftPosition() >= self.maxLastPositions and self.lenRightPosition() >= self.maxLastPositions:
            return self.checkOneHand(self.lastRightHandPositions, Hand.RIGHT, doValid) or self.checkOneHand(
                self.lastLeftHandPositions,
                Hand.LEFT,
                doValid)
        return False

    def checkOneHand(self, positions, hand, doValid):
        if not self.activeHand:
            i = 0
            valid = True
            for v in positions:
                if v:
                    # Distanz zwischen WRIST und INDEX_FINGER_MC bekommen als anhalts Punkt für die Größe
                    comparisonDistance = v.get2DDistance(HandPoint.WRIST, HandPoint.INDEX_FINGER_MCP)
                    if i < 13:
                        if not v.getAVGDistance() < 0.07*comparisonDistance*10:
                            valid = False
                    else:
                        if not v.getAVGDistance() > 0.08*comparisonDistance*10:
                            valid = False
                    i += 1
                else:
                    valid = False
            if valid and doValid:
                self.activeHand = hand
                self.lastMidActiveHand = positions[-1].getMidOfHand()
                self.onValid()
                return True
            return False
        else:
            if hand == self.activeHand:
                currentHand = positions[-1]
                comparisonDistance = currentHand.get2DDistance(HandPoint.WRIST, HandPoint.INDEX_FINGER_MCP)
                if not currentHand.getAVGDistance() > 0.08*comparisonDistance*10:
                    self.activeHand = None
                    self.onInvalid()
                    return False
                else:
                    if currentHand.getMidOfHand().x > self.lastMidActiveHand.x + 0.02:
                        self.lastMidActiveHand = currentHand.getMidOfHand()
                        ExecHelper.rightAltTab()
                    elif currentHand.getMidOfHand().x < self.lastMidActiveHand.x - 0.02:
                        self.lastMidActiveHand = currentHand.getMidOfHand()
                        ExecHelper.leftAltTab()

        return True


    def onValid(self):
        ExecHelper.openAltTab()
        print("alt tab")

    def onInvalid(self):
        ExecHelper.closeAltTab()
