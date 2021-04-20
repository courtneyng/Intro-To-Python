# Project ID: forLoop_exercises
# Author: Courtney Ng
# Period 7
# Program Description: Different examples of for loops

# The Fibonacci Sequence


def fibonacci(k):
    n = 0
    y = 1
    for x in range(0, k):
        hold = n
        n = y
        y = hold + y
    return n
for r in range(0, 51):
    print(fibonacci(r))

