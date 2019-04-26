# import get int from cs50 library and get int
from cs50 import get_int

# loop for proper height
while True:
    h = get_int("Height: ")
    if h >= 1 and h <= 8:
        break

# iterate over a height
for i in range(h):
    # print spaces and then hashes
    print(" " * (h - 1 - i), end="")
    print("#" * (i + 1), end="")
    # print additional space and hashes in reverse order
    print(" ", "#" * (i + 1), end="")
    # print new line
    print()
