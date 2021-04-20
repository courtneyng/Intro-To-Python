# Program ID: Mad-Libs
# Author: Courtney Ng
# Period 7
# Program Description: Making a mad lib based on the string functions

adj = input("Please input an adjective. ")
noun = input("Please input a noun. ")
verb = input("Please input a verb. ")
place = input("Please input a place. ")

line1 = "After the uprising, the world became a(n) adj cyberpunk society where technology is almost everything."
line2 = "While everyone sleeps, one adj person named Temperance Rebekah Wickham patrols the night to hack the system."
line3 = "Temperance uses a noun to hack into the system by distorting files and corrupting them so they rip."
line4 = "Her base is located in place." 
line4a = "Her work space is very adj and shes proud of that."
line5 = "To get from place to place in this new blocked society, she also uses her noun."
line6 = "Her noun"
line7 = "Her noun can decode messages like this"
line8 = "Ixwixllxbxexatxtxhexschxooxlxtoxmorxrow."
line8a = "I will be at the school tomorrow"
line9 = "She goes to help out at the school after seeing this. "
line9a = "She works to liberate the adj humans of her time"
print(line1.replace("adj", adj))
print(line2.replace("adj", adj))
print(line3.replace("noun", noun))
print(line4.replace("place", place))
print(line4a.replace("adj", adj))
print(line5.replace("noun", noun))
print(line6.replace("noun", noun), "can do all sorts of amazing things")
print(line7.replace("noun", noun))
print(line8)
print(line8.split("x"))
print("She decodes it to see the message.", " ".join(line8a))
print(line9 + line9a.replace("adj", adj))

