# Program ID: If-exercises
# Author: Courtney Ng, Jasmine Li
# Period 7
# Program Description: Using if statements

# list for months
longMonths = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
shortMonths = ["April", "June", "September", "November"]
oDD = ["February"]

ans = input("Enter the name of a month: ")

# check list
if ans in longMonths:
    print ("No. of days: 31")
elif ans in shortMonths:
    print("No. of days: 30")
elif ans in oDD:
    print("No. of days: 28/29")
else:
    print("That is not a month.")
