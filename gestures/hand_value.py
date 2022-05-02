from enum import Enum
import math

class HandValue:

    def __init__(self, left, wrist, thumbCMC, thumbMCP, thumbDIP, thumbTIP, indexFingerMCP, indexFingerPIP, indexFingerDIP, indexFingerTIP, ringFingerMCP, ringFingerPIP, ringFingerDIP, ringFingerTIP, pinkyMCP, pinkyPIP, pinkyDIP, pinkyTIP):
        self.content = {
            HandPoint.WRIST: wrist,
            HandPoint.THUMB_CMC: thumbCMC,
            HandPoint.THUMB_MCP: thumbMCP,
            HandPoint.THUMB_DIP: thumbDIP,
            HandPoint.THUMB_TIP: thumbTIP,
            HandPoint.INDEX_FINGER_MCP: indexFingerMCP,
            HandPoint.INDEX_FINGER_PIP: indexFingerPIP,
            HandPoint.INDEX_FINGER_DIP: indexFingerDIP,
            HandPoint.INDEX_FINGER_TIP: indexFingerTIP,
            HandPoint.RING_FINGER_MCP: ringFingerMCP,
            HandPoint.RING_FINGER_PIP: ringFingerPIP,
            HandPoint.RING_FINGER_DIP: ringFingerDIP,
            HandPoint.RING_FINGER_TIP: ringFingerTIP,
            HandPoint.PINKY_MCP: pinkyMCP,
            HandPoint.PINKY_PIP: pinkyPIP,
            HandPoint.PINKY_DIP: pinkyDIP,
            HandPoint.PINKY_TIP: pinkyTIP
        }
        self.left = left

    def __init__(self, left, data):
        if data:
            self.content = {}
            i = 0
            for v in data.landmark:
                self.content[getHandPointByIndex(i)] = Position(v.x, v.y, v.z);
                i += 1

    def isOpen(self):
        maxDist = 0.15
        finger_tips = [HandPoint.THUMB_TIP, HandPoint.INDEX_FINGER_TIP, HandPoint.MIDDLE_FINGER_TIP, HandPoint.RING_FINGER_TIP, HandPoint.PINKY_TIP]
        for currentFinger in finger_tips:
            dx = abs(self.getPosition(currentFinger).x - self.getPosition(HandPoint.WRIST).x)
            dy = abs(self.getPosition(currentFinger).y - self.getPosition(HandPoint.WRIST).y)
            dist = math.sqrt(dx*dx+dy*dy)
            if dist < maxDist:
                return False
        return True

    def get2DDistance(self, point1, point2):
        dx = abs(self.getPosition(point1).x - self.getPosition(point2).x)
        dy = abs(self.getPosition(point1).y - self.getPosition(point2).y)
        return math.sqrt(dx*dx+dy*dy)

    def getMidOfHand(self):
        return Position((self.getPosition(HandPoint.WRIST).x + self.getPosition(HandPoint.INDEX_FINGER_MCP).x)/2, (self.getPosition(HandPoint.WRIST).y + self.getPosition(HandPoint.INDEX_FINGER_MCP).y)/2, (self.getPosition(HandPoint.WRIST).z + self.getPosition(HandPoint.INDEX_FINGER_MCP).z)/2)

    def getPosition(self, handPoint):
        return self.content.get(handPoint)

    def getAVGDistance(self):
        sum = 0
        for v1 in HandPoint:
            for v2 in HandPoint:
                sum += abs(self.getPosition(v1).x - self.getPosition(v2).x)
                sum += abs(self.getPosition(v1).y - self.getPosition(v2).y)
        return sum / (21*21)

class Hand(Enum):
    LEFT = 0
    RIGHT = 1

class HandPoint(Enum):
    WRIST = 0
    THUMB_CMC = 1
    THUMB_MCP = 2
    THUMB_DIP = 3
    THUMB_TIP = 4
    INDEX_FINGER_MCP = 5
    INDEX_FINGER_PIP = 6
    INDEX_FINGER_DIP = 7
    INDEX_FINGER_TIP = 8
    MIDDLE_FINGER_MCP = 9
    MIDDLE_FINGER_PIP = 10
    MIDDLE_FINGER_DIP = 11
    MIDDLE_FINGER_TIP = 12
    RING_FINGER_MCP = 13
    RING_FINGER_PIP = 14
    RING_FINGER_DIP = 15
    RING_FINGER_TIP = 16
    PINKY_MCP = 17
    PINKY_PIP = 18
    PINKY_DIP = 19
    PINKY_TIP = 20

class Position:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def getHandPointByIndex(i):
    for e in HandPoint:
        if e.value == int(i):
            return e