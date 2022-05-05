from gestures.gesture import Gesture
import utils.zoom_helper as ShortkeyHelper

class MuteGesture(Gesture):

    def __init__(self):
        self.initLastPositions(15)

    def check(self, left, right, doValid):
        # Add new position to recent position list
        self.addLastPosition(left, right)

        # check if recent positions contains enough values
        if not self.lenLeftPosition() >= 7:
            return False
        if not self.lenRightPosition() >= 7:
            return False

        if sum([1 for i in range(7) if self.getRightPosition(i) is None]) == 0:
            # check if movement goes from left to right
            comparisonDistance = self.getRightPosition(0).getComparisonDistance()*100/15
            # check movement to right
            valid = True
            for i in range(1, 7):
                if not self.getRightPosition(i).getMidOfHand().x >= self.getRightPosition(i-1).getMidOfHand().x+0.01*comparisonDistance:
                    valid = False
            if valid and doValid:
                self.onValid(True)
                return True

            # check movement to left
            valid = True
            for i in range(1, 7):
                if not self.getRightPosition(i).getMidOfHand().x <= self.getRightPosition(
                        i - 1).getMidOfHand().x - 0.01 * comparisonDistance:
                    valid = False
            if valid and doValid:
                self.onValid(False)
                return True

        if sum([1 for i in range(7) if self.getLeftPosition(i) is None]) == 0:
            comparisonDistance = self.getLeftPosition(0).getComparisonDistance()*100/15
            valid = True
            for i in range(1, 7):
                if not self.getLeftPosition(i).getMidOfHand().x >= self.getLeftPosition(i-1).getMidOfHand().x+0.01*comparisonDistance:
                    valid = False
            if valid and doValid:
                self.onValid(True)
                return True
            valid = True
            for i in range(1, 7):
                if not self.getLeftPosition(i).getMidOfHand().x <= self.getLeftPosition(
                        i - 1).getMidOfHand().x - 0.01 * comparisonDistance:
                    valid = False
            if valid and doValid:
                self.onValid(False)
                return True

        return False

    def onInvalid(self):
        return

    def onValid(self, muteState: bool):
        ShortkeyHelper.setMuteState(muteState)
        self.initLastPositions(self.maxLastPositions)
        print("mute")
