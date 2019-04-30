# Pseudocode: in argv[1] is list of banned words, load it into list - use set()
# get prompt from a user, separate each word prompted - use split()
# check if word is in list: if no - print word, if yes - print ****

from cs50 import get_string
from sys import argv

# check if there are two arguments (strings)
if len(argv) != 2:
    print("Usage: python bleep.py dictionary")
    exit([1])


def main():

    # load argv[1] and add banned words to new list(set)
    bannedwords = set()
    file = open(argv[1], "r")
    for line in file:
        bannedwords.add(line.rstrip("\n"))
    file.close()

    # get message from user
    p = get_string("What line would you like to censor?\n")

    # iterate over each word in messsage
    for word in p.split():

        # check word if it's banned list and print
        if word.lower() in bannedwords:
            print("*" * len(word), end=" ")
        else:
            print(word, end=" ")
    print()


if __name__ == "__main__":
    main()
