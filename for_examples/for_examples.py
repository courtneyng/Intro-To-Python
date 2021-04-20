# Project ID: for_examples
# Author: Courtney Ng
# Period 7
# Program Description: Different examples of for loops

# First Set Up
pairs = []
# ---------------------------------------------------------------------------------------------------------------------
for x in range(0,5):
    y = (2 * x) + 4
    pairs.append((x,y))

# print(pairs)
# print(pairs[2])  # x,y
# print((pairs[2])[1])  # just y coordinate
# ---------------------------------------------------------------------------------------------------------------------
for x in range(5,10):
    y = (2 * x) + 4
    pairs.append((x,y))

# print(pairs)

# For a "For" loop it stops at 10 so you if you want 10/11 you add one more 11/12
# ---------------------------------------------------------------------------------------------------------------------

# Second Set Up
# ---------------------------------------------------------------------------------------------------------------------
for x in range(5):  # if its one index number it assumes you start at 0 and the index is last number
    y = (2 * x) + 4
    pairs.append((x,y))

print(pairs)
print(pairs[2])
print((pairs[2])[1])
# ---------------------------------------------------------------------------------------------------------------------


# Third Set Up
words = ["Ed", "Edd", "Eddy"]
for w in words:  # don't need parenthesis but you could "(words)"
    print(w)

# Fourth Set Up
print("length: ", len(words))
for w in range(len(words)):
    print(w, words[w])
