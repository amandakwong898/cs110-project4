import stdio
import sys


class Point:
    """
    Represents a point in 2-dimensional space.
    """

    def __init__(self, x, y):
        """
        Construct a new point given its x and y coordinates.
        """

        self._x = x
        self._y = y

    def distanceTo(self, other):
        """
        Return the Euclidean distance between self and other.
        """

        p = ((self._x - other._x) ** 2 + (self._y - other._y) ** 2)
        q = p ** (1/2)
        return q

    def __str__(self):
        """
        Return a string representation of self.
        """

        return "(%.1f, %.1f)" % (self._x, self._y)


# Test client [DO NOT EDIT].
def _main():
    x1, y1, x2, y2 = map(float, sys.argv[1:])
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    stdio.writeln('p1 = ' + str(p1))
    stdio.writeln('p2 = ' + str(p2))
    stdio.writeln('d(p1, p2) = ' + str(p1.distanceTo(p2)))


if __name__ == '__main__':
    _main()
