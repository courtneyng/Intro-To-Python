# Program ID: If-exercises
# Author: Courtney Ng, Jasmine Li
# Period 7
# Program Description: Using if statements

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']
# months.append('December')

ans = input("Enter the name of a month: ")

if ans == "January" or "March" or "May" or "July" or "August" or "October" or "December":
    print("No. of days: 31")

elif ans == "February":
    print("No. of days: 28/29")

elif ans == "April" or "June" or "September" or "November":
    print("No. of days: 30")


elif ans in months:
    print ("found it")
    
else:
    print("That is not a month.")
