from abc import abstractmethod

class Gesture:

    @abstractmethod
    def check(self, left, right):
        pass

    @abstractmethod
    def onValid(self):
        pass

    @abstractmethod
    def onInvalid(self):
        pass

    def addLastPosition(self, left, right):
        if len(self.lastLeftHandPositions) >= self.maxLastPositions:
            self.lastLeftHandPositions.pop(0)
        if len(self.lastRightHandPositions) >= self.maxLastPositions:
            self.lastRightHandPositions.pop(0)
        self.lastLeftHandPositions.append(left)
        self.lastRightHandPositions.append(right)

    def getLeftPosition(self, i):
        return self.lastLeftHandPositions[i]
    def getRightPosition(self, i):
        return self.lastRightHandPositions[i]
    def lenLeftPosition(self):
        return len(self.lastLeftHandPositions)
    def lenRightPosition(self):
        return len(self.lastRightHandPositions)

    def initLastPositions(self, max):
        self.maxLastPositions = max
        self.lastLeftHandPositions = []
        self.lastRightHandPositions = []