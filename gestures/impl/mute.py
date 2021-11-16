from gestures.gesture import Gesture


class MuteGesture(Gesture):

    def __init__(self):
        self.initLastPositions(15)

    def check(self, left, right):
        # Add new position to recent position list
        self.addLastPosition(left, right)

        # check if recent positions contains enough values
        if not self.lenLeftPosition() >= 10:
            return False

        # check if movement goes from left to right
        for i in range(1, 7):
            if not self.getRightPosition(i).getMidOfHand().x >= self.getRightPosition(i-1).getMidOfHand().x:
                return False

        # check if movement goes wide enough
        if not self.getRightPosition(1).getMidOfHand().x < self.getRightPosition(7).getMidOfHand().x - 0.4:
            return False

        # execute valid script
        self.onValid()
        return True

    def onInvalid(self):
        self.initLastPositions(15)

    def onValid(self):
        self.initLastPositions(15)
        print("mute")
