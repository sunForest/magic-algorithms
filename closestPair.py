def findClosestPair(X, Y):
    """
        Find the closest pair among the given 2-dementional points
        with O (nlogn) running time

        X: points sorted by x coordinate
        Y: points sorted by y coordinate

        return (point1, point2)
    """

    numPoints = len(X)

    if numPoints < 2:
        return

    # Base Case with only two points
    if numPoints < 3:
        return tuple(X)

    # Split the points into left part and right part
    splitIdx = numPoints/2
    leftX = X[:splitIdx]
    rightX = X[splitIdx:]

    # Sort the points in left and right part according to y coordinate
    # with the help of hashing
    xSetLeft = set(leftX)
    xSetRight = set(rightX)
    leftY = []
    rightY = []
    for p in Y:
        if p in xSetLeft:
            leftY.append(p)
        else:
            rightY.append(p)

    pair1 = findClosestPair(leftX, leftY)
    pair2 = findClosestPair(rightX, rightY)

    if pair1 and pair2:
        dist1 = d(*pair1[:])
        dist2 = d(*pair2[:])
        delta = min(dist1, dist2)
        closestPair = pair1 if dist1 == delta else pair2
    elif pair1:
        delta = d(*pair1[:])
        closestPair = pair1
    else:
        delta = d(*pair2[:])
        closestPair = pair2

    midX = rightX[0][0]
    leftBound, rightBound = midX - delta, midX + delta
    pointsInStrip = [ p for p in Y if (leftBound <= p[0] <= rightBound) ]

    if len(pointsInStrip):
        pair3 = findCloserSplitPair(delta, pointsInStrip)

    if pair3:
        return pair3

    return closestPair

def findCloserSplitPair(delta, pointsInStrip):
    pnts = pointsInStrip
    numPoints = len(pointsInStrip)
    closerPair = None
    minDist = delta

    if numPoints < 8:
        for i in range(numPoints):
            for j in range(i+1, numPoints):
                distance = d(pnts[i], pnts[j])
                if distance < minDist:
                    minDist = distance
                    closerPair = (pnts[i], pnts[j])

    else:
        # Check the book <Introduction to Algorithms> for the reason why
        # we could consider only the 7 nearest neighbours
        # There could be at most 8 points in the rectangle with the size
        # of delta * 2delta
        for i in range(numPoints - 7):
            for j in range(1, 8):
                distance = d(pnts[i], pnts[i+j])
                if distance < minDist:
                    minDist = distance
                    closerPair = (pnts[i], pnts[j])

    return closerPair

# ----- util functions -----


def d (p1, p2):
    """
        Returns the Euclidean distance of the two points

        p1: (x1, y1)
        p2: (x2, y2)
    """

    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def minDistance (pnts):
    """
        Return the minimum distance between pairs of given points
        -Brute Force approach for testing 
    """
    numPnts = len(pnts)
    if numPnts < 2:
        return 
    minDist = d(pnts[0], pnts[1])

    for i in range(numPnts):
        for j in range(i+1, numPnts):
            dist = d(pnts[i], pnts[j])
            if dist < minDist:
                minDist = dist

    return minDist

# ----- test -----
if __name__ == "__main__":
    import random
    randomPnts = []
    for i in range(100):
        x = random.randint(-100000, 100000)
        y = random.randint(-100000, 100000)
        randomPnts.append((x , y))

    X = sorted(randomPnts, key = lambda x: x[0])
    Y = sorted(randomPnts, key = lambda x: x[1])

    closestPair = findClosestPair(X, Y)
    minDist = minDistance(randomPnts)
    print d(*closestPair[:]), minDist
