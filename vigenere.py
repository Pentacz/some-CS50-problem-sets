# import get string and sys
from cs50 import get_string
import sys

# check if there are two arguments (strings) and argv[1] is alphabetical
if len(sys.argv) != 2:
    print("Usage: 'python vigenere.py key', where the key is a word")
    sys.exit([1])
key = sys.argv[1]
for k in key:
    if k.isalpha() == False:
        print("only alphabetical characters")
        sys.exit([2])

# get plaintext to cipher
p = get_string("plaintext: ")
print("ciphertext: ", end="")

length = len(key)
count = 0

# iterate each character in plaintext
for c in p:

    # cipher only for alphabetic characters
    if c.isalpha() == True:

        # get back to beginning of the key word if already ended
        while count >= length:
            count = count - length

        # create integer to shift by position of character in alphabet
        if key[count].isupper() == True:
            shift = ord(sys.argv[1][count]) - 65
        else:
            shift = ord(sys.argv[1][count]) - 97

        # shift c by key, substracting difference between ascii value and position in alphabet
        if c.isupper() == True:
            c = ((ord(c) - 65 + shift) % 26) + 65
        else:
            c = ((ord(c) - 97 + shift) % 26) + 97

        # change back c to char, print it and count+1
        c = chr(c)
        print(c, end="")
        count += 1
    else:
        print(c, end="")
print()

