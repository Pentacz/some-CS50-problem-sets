# import cs50 get string
from cs50 import get_string
import sys

# check if there are two arguments (strings)
if len(sys.argv) != 2:
    print("Usage: 'python caesar.py key', where the key is a number")
    sys.exit([1])

# assign int for key and get plaintext
k = int(sys.argv[1])
p = get_string("plaintext: ")
print("ciphertext: ", end="")

# iterate (and print) each character in plaintext
for c in p:
    # only for alphabetic characters
    if c.isalpha():
        # shift c by key, substracting difference between ascii value and position in alphabet
        if c.isupper() == True:
            c = ((ord(c) - 65 + k) % 26) + 65
        else:
            c = ((ord(c) - 97 + k) % 26) + 97
        c = chr(c)
    print(c, end="")
print()
