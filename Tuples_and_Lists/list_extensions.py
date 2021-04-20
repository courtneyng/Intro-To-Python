# Program ID: lists_extensions
# Author: Courtney Ng
# Period: 7
# Program Description: List extensions in Python

# Given list
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# The new list extensions test

fruits.count('apple')
print(fruits.count('apple')) # Added a print statement to show output

fruits.count('tangerine')
print(fruits.count('tangerine'))

fruits.index('banana')
print(fruits.index('banana'))

fruits.index('banana', 4) # Find the next banana starting at pos 4
print(fruits.index('banana', 4))

fruits.reverse()
print(fruits)

fruits.append('grape') # Adds grape to the list
print(fruits)

fruits.sort() # Alphabetically sorts
print(fruits)

fruits.pop() # Takes a variable out and puts it back in
print(fruits.pop(3))

