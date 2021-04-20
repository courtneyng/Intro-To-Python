# Program ID: string_handling
# Author: Courtney Ng
# Period: 7
# Program description: Basic practice with strings


print("This is a string")

string1 = "This is a string !!"
print(string1)

string2 = """\
    First line.
    Second line.
    Third line."""

string3 = """
    Who's on first.
    What's on second.
    I don't know is on third."""

print(string2)
print(string3)

string4 = "String a is this."
print(string4[16])

string5 = "How many licks does it take to get to the center of a tootsie pop?"
print(string5)
print(string5[-1])

string6 = "The world may never know"
print(string6)
print(string6[14:19])

string7 = "My birthday is on Spring Break !!"
print(string7)
print(string7[-9:-3]) # Doing it [-4:-9] did not work, switched it [-9:-4] and it put Brea.
# Tried [-9:-5] chose less letters, "Bre" then did [-9:-3] solved
# slicing only goes left to right!


