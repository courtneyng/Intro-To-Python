# Program ID: If-exercises
# Author: Courtney Ng, Jasmine Li
# Period 7
# Program Description: Using if statements

# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']
# months.append('December')

ans = input("Enter the name of a month: ")

if ans == "January":
    print("No. of days: 31")
elif ans == "March":
    print("No. of days: 31")
elif ans == "May":
    print("No. of days: 31")
elif ans == "July":
    print("No. of days: 31")
elif ans == "August":
    print("No. of days: 31")
elif ans == "October":
    print("No. of days: 31")
elif ans == "December":
    print("No. of days: 31")

elif ans == "February":
    print("No. of days: 28/29")

elif ans == "April":
    print("No. of days: 30")
elif ans == "June":
    print("No. of days: 30")
elif ans == "September":
    print("No. of days: 30")
elif ans == "November":
    print("No. of days: 30")

else:
    print("That is not a month.")
