# Program ID: stringhandlingDemo
# Author: Courtney Ng
# Period 7
# Program Description:Going more in depth with string handling

# string_input = ("This is a string")
# part1 = (string_input [0,5])
# part2 = (string_input [5,9])
yes= "yes"
no = "no"
# printString = "How many licks does it take to get to the center of a tootsie pop?"
# sliceString = "Slice a ; The world may never know ; pizza"
# negativeIndices = "The spider climbed up the water spout"
# exit_menu = "exit"
printString = 1
sliceString = 2
negativeIndices = 3
exit_menu = 4


def first_string():
    string1 = input("Enter a string")
    print(string1)


def second_string():
    string2 = input("Enter a string")
    print(string2)
    print(string2[0:5])


def third_string():
    string3 = "Winnie the Pooh"
    print(string3)
    print(string3[-4:-1])

ans = input("Do you want to see the menu?")
while ans == yes:
    menu = """\
    -------------------------Menu-------------------------
    Print a string.      [1]
    Slice a string.      [2]
    Negative indices.    [3]
    Exit                 [4]
    ------------------------------------------------------"""
    print(menu)
    answer = int(input("What would you like to do?"))
    if ans == 4:
        print("Goodbye")
    else:
        if answer == 1:
            first_string()

        else:
            if answer == 2:
                second_string()

            else:
                answer == 3
                third_string()
    ans = input("Do you want to see the menu?")

