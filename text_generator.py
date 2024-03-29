import stdio
import sys
from markov_model import MarkovModel

"""
Builds a Markov model of order k from the input text; then, starting
with the k-gram consisting of the first k characters of the input
text, prints out T characters generated by simulating a trajectory
through the corresponding Markov chain, followed by a new line.
"""

# Read command-line arguments k and T.
k = int(sys.argv[1])
T = int(sys.argv[2])

# Initialize text to text read from standard input using
# sys.stdin.read().


text = sys.stdin.read()


def main():

    # Create a Markov model named model using text and k.
    model = MarkovModel(text, k)

    # Use model.gen() to generate a random text of length T and
    # starting with the first k characters of text.
    rand = model.gen(text[:k], T)

    # Write the random text to standard output.
    stdio.writeln(rand)


if __name__ == '__main__':
    main()
