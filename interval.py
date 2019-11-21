import stdio
import sys


class Interval:
    """
    Represents a 1-dimensional interval [lbound, rbound].
    """

    def __init__(self, lbound, rbound):
        """
        Construct a new interval given its lower and
        upper bounds.
        """

        self._lbound = lbound
        self._rbound = rbound

    def lbound(self):
        """
        Return the lower bound of the interval.
        """

        return self._lbound

    def rbound(self):
        """
        Return the upper bound of the interval.
        """

        return self._rbound

    def contains(self, x):
        """
        Return True if self contains the point x and False otherwise.
        """

        return self._lbound <= x <= self._rbound

    def intersects(self, other):
        """
        Return True if self intersects other and
        False othewise.
        """

        return max(self._lbound, other._lbound) <= \
            min(self._rbound, other._rbound)

    def __str__(self):
        """
        Returns a string representation of self.
        """

        return '[' + str(self._lbound) + ", " + \
            str(self._rbound) + ']'

# Test client [DO NOT EDIT].


def _main():
    x = float(sys.argv[1])
    intervals = []
    while not stdio.isEmpty():
        lbound = stdio.readFloat()
        rbound = stdio.readFloat()
        intervals += [Interval(lbound, rbound)]
    for i in range(len(intervals)):
        if intervals[i].contains(x):
            stdio.writef('%s contains %f\n', intervals[i], x)
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i].intersects(intervals[j]):
                stdio.writef('%s intersects %s\n',
                             intervals[i], intervals[j])


if __name__ == '__main__':
    _main()
