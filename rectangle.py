import stdio
import sys
from interval import Interval


class Rectangle:
    """
    Represents a rectangle as two (x and y) intervals.
    """

    def __init__(self, xint, yint):
        """
        Construct a new rectangle given the x and y intervals.
        """

        self._xint = xint
        self._yint = yint

    def area(self):
        """
        Return the area of self.
        """

        width = self._xint.rbound() - self._xint.lbound()
        height = self._yint.rbound() - self._yint.lbound()
        return width * height

    def perimeter(self):
        """
        Return the perimeter of self.
        """

        width = self._xint.rbound() - self._xint.lbound()
        height = self._yint.rbound() - self._yint.lbound()
        return 2 * (width + height)

    def contains(self, x, y):
        """
        Return True if self contains the point (x, y) and
        False otherwise.
        """

        return self._xint.contains(x) and self._yint.contains(y)

    def intersects(self, other):
        """
        Return True if self intersects other and
        False othewise.
        """

        return self._xint.intersects(other._xint) and \
            self._yint.intersects(other._yint)

    def __str__(self):
        """
        Return a string representation of self.
        """

        return str(self._xint) + ' x ' + str(self._yint)


# Test client [DO NOT EDIT].
def _main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    rectangles = []
    while not stdio.isEmpty():
        lbound1 = stdio.readFloat()
        rbound1 = stdio.readFloat()
        lbound2 = stdio.readFloat()
        rbound2 = stdio.readFloat()
        rectangles += [Rectangle(Interval(lbound1, rbound1),
                                 Interval(lbound2, rbound2))]
    for i in range(len(rectangles)):
        stdio.writef('Area(%s) = %f\n', rectangles[i],
                     rectangles[i].area())
        stdio.writef('Perimeter(%s) = %f\n', rectangles[i],
                     rectangles[i].perimeter())
        if rectangles[i].contains(x, y):
            stdio.writef('%s contains (%f, %f)\n',
                         rectangles[i], x, y)
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if rectangles[i].intersects(rectangles[j]):
                stdio.writef('%s intersects %s\n',
                             rectangles[i], rectangles[j])


if __name__ == '__main__':
    _main()
