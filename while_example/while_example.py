# Program ID: while_example
# Author: Courtney Ng
# Period: 7
# Program Description: Creating and experimenting with a while loop

# This section sets up two variables
people = 0
dogs = 40

while people < dogs:
    print ("There are not enough people")
    people = int(input("Enter a number of people"))

print ("There are too many people - end loop")
