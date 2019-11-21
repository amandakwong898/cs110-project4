import stdio
import sys
from markov_model import MarkovModel

"""
Takes an integer k (model order) and a string s (noisy message) as
command-line arguments, reads the input text from standard input, and
prints out the most likely original string.
"""

# Read command-line arguments k and s.
k = int(sys.argv[1])
s = str(sys.argv[2])

# Initialize text to text read from standard input using
# sys.stdin.read().


text = sys.stdin.read()


def main():
    # Create a Markov model named model using text and k.
    model = MarkovModel(text, k)

    # Use model.replace_unknown() to decode the corrupted text s.
    stdio.writeln(model.replace_unknown(s))


if __name__ == '__main__':
    main()
