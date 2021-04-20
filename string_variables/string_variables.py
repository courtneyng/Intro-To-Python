# Program ID: string_variables
# Author: Courtney Ng
# Period: 7
# Program Description: Using variables, names, numbers and letters to make strings

# These are the variables about me for the following print.
# my_name = 'Courtney Ng'
# my_age = 15
# my_height = 62
# my_weight = 105
# my_eyes = 'Dark Brown'
# my_teeth = 'white'
# my_hair = 'Brown, Red'

# These print out the information about me.
# print ("Let's talk about %s." % my_name)
# print ("She's %d inches tall." % my_height)
# print ("She's %d pounds heavy." % my_weight)
# print ("Actually, that's not too heavy")
# print ("She's got %s eyes and %s hair" % (my_eyes, my_hair))
# print ("Her teeth are usually %s depending on the coffee." % my_teeth)

# This adds up some of the variables about myself.
# print ("If I add %d, %d and %d, I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

# Another way to prompt.
# print ("How old are you")
# age = input ()
# put "int" in front of input if you want to use a numeric value
# could also use "float" which is numbers with decimals

my_name = input ("What is your name?")
my_age = int (input ("How old are you?"))
my_height = int (input ("How tall are you?"))
my_weight = int (input ("How many pounds do you weigh?"))
my_eyes = input ("What colors are your eyes?")
my_teeth = input ("What color are you teeth?")
my_hair = input ("What color is your hair?")

print ("Let's talk about %s." % my_name)
print ("She's %d inches tall." % my_height)
print ("She's %d pounds heavy." % my_weight)
print ("Actually, that's not too heavy")
print ("She's got %s eyes and %s hair" % (my_eyes, my_hair))
print ("Her teeth are usually %s depending on the coffee." % my_teeth)
print ("If I add %d, %d and %d, I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))