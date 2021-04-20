# Program ID: A_List_Of_Numbers
# Author: Courtney Ng
# Period: 7
# Program Description: List extensions in Python

# numList = [1, 1, 2, 3, 5, 8, 11, 19, 30, 49]
# product = 30*8*11*19*30*49
num1 = int(input("Enter the first number."))
numList = [100, 101, 102]
numList.append(num1)
numList.remove(100)
numList.remove(101)
numList.remove(102)
print(numList)
print("The amount of numbers is: 1")
# gathering variables
num2 = int(input("Add another number to the list"))
numList.append(num2)

num3 = int(input("Add another number to the list"))
numList.append(num3)

num4 = int(input("Add another number to the list"))
numList.append(num4)

num5 = int(input("Add another number to the list"))
numList.append(num5)

num6 = int(input("Add another number to the list"))
numList.append(num6)

num7 = int(input("Add another number to the list"))
numList.append(num7)

num8 = int(input("Add another number to the list"))
numList.append(num8)

num9 = int(input("Add another number to the list"))
numList.append(num9)

num10 = int(input("Add another number to the list"))
numList.append(num10)

print("This is the list of numbers:", numList)
print("The amount of numbers is: 10")

print("If you add all the numbers together the sum is:", sum(numList))
# sum = 0
# for x in range(0,9):
    # sum = sum + list[x]
product = 1
for x in range(0, 9):
    product = product * numList[x]
print("If you multiply all the numbers in the list the product is:", product)

# this will sort the numbers in order from least to highest
numList.sort()
print("The smallest number is:", numList.pop(0))
print("The largest number is:", numList.pop(8))
print("The new amount is: 8")
print(numList)


