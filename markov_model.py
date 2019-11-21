import stdio
import stdrandom
import sys


class MarkovModel(object):
    """
    Represents a Markov model of order k from a given text string.
    """

    def __init__(self, text, k):
        """
        Create a Markov model of order k from given text (assumed
        to have length at least k).
        """

        # order of the Markov model, _k (int)
        self._k = k
        # a dictionary to keep track of character frequencies, _st (dict)
        self._st = dict()
        text += text[:k]
        for i in range(len(text) - k):
            tk = text[i:i + k]
            if tk not in self._st:
                self._st[tk] = dict()
            c = text[i + k]
            if c not in self._st[tk]:
                self._st[tk][c] = 0
            self._st[tk][c] += 1

    def order(self):
        """
        Return order of Markov model.
        """

        return self._k

    def kgram_freq(self, kgram):
        """
        Return number of occurrences of kgram in text (sum of values of
        _st[kgram]).
        """

        return sum(self._st[kgram].values())

    def char_freq(self, kgram, c):
        """
        Return number of times character c follows kgram (value of c in
        _st[kgram]).
        """
        if c not in self._st[kgram]:
            return 0
        return self._st[kgram][c]

    def rand(self, kgram):
        """
        Use stdrandom.discrete() to randomly select and return a
        random character following kgram.
        """
        if kgram not in self._st:
            raise ValueError()
        t = self._st[kgram]
        s = sum(list(t.values()))
        a = list(self._st[kgram].values())
        # a = stdarray.create1D(len(t.values(), 0))
        for i in range(len(a)):
            a[i] = (list(t.values()))[i] / s
        r = stdrandom.discrete(a)
        return list(t.keys())[r]

    def gen(self, kgram, T):
        """
        Generate and return a string of length T by simulating a trajectory
        through the correspondng Markov chain. The first k (<= T) characters
        of the generated string is the argument kgram.
        Initialize a variable text to kgram. Perform T - _k iterations,
        where each iteration involves appending to text a random character
        obtained using a call to self.rand() and updating kgram to the last
        _k character of sum. Return text.
        """

        text = kgram
        for i in range(T - self._k, 0, -1):
            text += self.rand(kgram)
            kgram = text[len(text) - self._k:]
        return text

    def replace_unknown(self, corrupted):
        """
        Replace unknown characters (~) in corrupted with most probablenb
        characters, and return that string.
        """

        # Return the index of the maximum element in the given list a.
        def argmax(a):
            return a.index(max(a))

        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                kgram_before = corrupted[i - self._k: i]
                kgram_after = corrupted[i + 1: self._k + i + 1]
                probs = []
                hypothesis = list(self._st[kgram_before].keys())
                for m in hypothesis:
                    context = kgram_before + m + kgram_after
                    p = 1.0
                    for k in range(0, self._k + 1):
                        kgram = context[k: k + self._k]
                        char = context[k + self._k]
                        if (kgram not in self._st or char not in
                                self._st[kgram]):
                            p = 0.0
                        else:
                            p *= (self.char_freq(kgram, char) /
                                  self.kgram_freq(kgram))
                    probs.append(p)
                original += hypothesis[argmax(probs)]
            else:
                original += corrupted[i]
        return original


def _main():
    """
    Test client [DO NOT EDIT].
    """

    text, k = sys.argv[1], int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        kgram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace("-", " "), char.replace("-", " ")))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char,
                         model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()
