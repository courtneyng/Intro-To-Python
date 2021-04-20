# Program ID: stringhandlingDemo
# Author: Courtney Ng
# Period 7
# Program Description:Going more in depth with string handling

# string_input = ("This is a string")
# part1 = (string_input [0,5])
# part2 = (string_input [5,9])
yes= "yes"
no = "no"
printString = "print a string"
sliceString = "slice a string"
negativeIndices = "negative indices"
exit_menu = "exit"


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
    answer = input("What would you like to do?")
    if ans == exit_menu:
        print("Goodbye")
    else:
        if answer == printString:
            string1 = input("Enter a line")
            print(string1)
        else:
            if answer == sliceString:
                string2 = input("Enter a line.")
                print(string2)
                print(string2[0:11])
            else:
                answer == negativeIndices
                string3 = "winnie the pooh"
                print(string3)
                print(string3[-9:-1])
    ans = input("Do you want to see the menu?")
