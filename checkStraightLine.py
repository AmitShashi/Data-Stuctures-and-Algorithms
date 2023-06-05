class Solution(object):
    def checkStraightLine(self, coordinates):
        (x0, y0), (x1, y1) = coordinates[:2]
        for x, y in coordinates[2:]:
            if (y1 - y0) * (x1 - x) != (y1 - y) * (x1 - x0):
                return False
        return True
