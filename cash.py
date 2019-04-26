# import cs50 get float and math to round down
from cs50 import get_float
import math

# dodgy loop to get non-negative values only
while True:
    x = get_float("Change owed: ")
    if x >= 0:
        break

# convert dollars to cents, set coins to 0
c = x * 100
coins = 0

# count quarters
if c / 25 >= 1:
    coins += math.floor(c / 25)
    c %= 25

# count dimes
if c / 10 >= 1:
    coins += math.floor(c / 10)
    c %= 10

# count nickles
if c / 5 >= 1:
    coins += math.floor(c / 5)
    c %= 5

# add pennies
coins += c

print(f"coins: {coins:0.0f}")
