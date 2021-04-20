# Program ID: LogicalOperators
# Author: Courtney Ng
# Period 7
# Program Description: Learning about logical operations

# ---------------------------------------------------------------------------------------------------------------------

# while True:
#     for x in range(0,4):
#         print(x)

# ---------------------------------------------------------------------------------------------------------------------

# flag = "y"

# while flag == "y":
#     for x in range(0,4):
#         print(x)
#     flag = input("Do it again? (y or n):")

# ---------------------------------------------------------------------------------------------------------------------

# flag = "y"
# y = 0

# while flag == "y" and y < 4:
#     for x in range(0,4):
#         print(x)
#     flag = input("Do it again? (y or n):")
#     y = int(input("Enter a y value: "))

# ---------------------------------------------------------------------------------------------------------------------

# flag = "y"
# y = 0

# while flag == "y" or y > 4:
#     for x in range(0,4):
#         print(x)
#     flag = input("Do it again? (y or n):")
#     y = int(input("Enter a y value: "))

# ---------------------------------------------------------------------------------------------------------------------

# flag = "y"
# y = 0

# while flag != "y" or y <= 4:
#     for x in range(0,4):
#         print(x)
#     flag = input("Do it again? (y or n):")
#     y = int(input("Enter a y value: "))

# ---------------------------------------------------------------------------------------------------------------------

flag = "y"
y = 0

while flag != "y" and y >= 4:
    for x in range(0,4):
        print(x)
    flag = input("Do it again? (y or n):")
    y = int(input("Enter a y value: "))

# ---------------------------------------------------------------------------------------------------------------------
