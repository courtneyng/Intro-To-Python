# Program ID: calculate_body_mass_index
# Author: Courtney Ng
# Period: 7
# Program Description: Create a program to calculate BMI through math functions.

yes = "yes"
no = "no"
exit = "Exit"
calc_bmi = "Calculate BMI"
find_abs = "Find Absolute Value"
time_conversion = "Time Conversion"

# Setting up a menu
answer_a = input("Do you want to see the task options?")
while answer_a == yes:
    
    print("------------------------------ MENU ------------------------------")
    print("                          [Calculate BMI]                         ")
    print("                       [Find Absolute Value]                      ")
    print("                         [Time Conversion]                        ")
    print("                              [Exit]                              ")
    print("------------------------------------------------------------------")
    answer = input("What would you like to do?")

    if answer == exit:
        print("Okay.")
    else:
        if answer == calc_bmi:
            ans = input("Do you want to calculate your bmi?")
            # Assignment A, Calculate BMI
            while ans == yes:
                height_in = int(input("What is your height in inches?"))
                weight_lb = float(input("What is your weight in pounds?"))
                height_m = round((height_in / 39), 2)
                weight_kg = round((weight_lb / 2.2),2)
                bmi = round(((weight_kg / height_m) / height_m),2)

                print("Your height in inches is:", height_in)
                print("Your weight in pounds is:", weight_lb)
                print("Your height in meters is:", height_m)
                print("Your weight in kilograms is:", weight_kg)
                print("Your BMI is:", bmi)
            answer_b = input("Go back to menu?")
            if answer_b == yes:
                print("Okay")


    # Assignment B, Absolute Value
        else:
            if answer == find_abs:
                answer_c = input("Do you want to find absolute value?")
                while
                    print("We will calculate the absolute value after multiplying and then subtracting the values.")
                    value_a = int(input("What would you like the first value to be?"))
                    value_b = int(input("The second value?"))
                    value_c = int(input("The third?"))
                    value_d = (value_a * value_b) + value_c
                    finalValue = abs(value_d)
                    print(finalValue)
                input("Go back to menu?")

    # Assignment C, Time Conversion
    print("We will convert military time (24 hour clock) into 12 hour clock values.")
    militaryTime = int(input("Insert a military time."))
    analogTime = militaryTime % 12
    input("Go back to menu?")
