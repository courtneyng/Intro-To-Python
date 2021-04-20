# Program ID: Variables_and_Names
# Author: Courtney Ng
# Period: 7
# Program Description: This code will be about variables and names for a program

# This part lays out the variable and names for the program to use.
cars = 200
space_in_car = 7
drivers = 25
passengers = 125
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

# This section prints out a code about the cars using the variables.
print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")


# This area is for freelance purposes
# These are new variables for different types of cars
space_in_suv = 8
space_in_van = 10
space_in_honda_civic = 5
amt_of_suv = 10
amt_of_van = 3
amt_of_honda_civic = 20
family1 = 4
family2 = 2
family3 = 5
family4 = 3
drivers2 = 10
ttl_cars = amt_of_honda_civic + amt_of_suv + amt_of_van

# This is testing area
print ("-------------------------------------------------------------")
print ("                     Separate Code                           ")
print ("-------------------------------------------------------------")
print ("We have new services in XXX area currently.")
print ("We have a much smaller amount of cars due to the area not having many people. ")
print ("We have", ttl_cars, "cars ready to go.")
print ("Yes it is a smaller amount but it serves many different sized families who are larger than 4")
print ("We have vans, SUVs and regular cars like the honda civic")
print ("Our vans hold", space_in_van, "people.")
print ("Our SUVs hold", space_in_suv, "people")
print ("Finally, our honda civics hold", space_in_honda_civic, "people")
