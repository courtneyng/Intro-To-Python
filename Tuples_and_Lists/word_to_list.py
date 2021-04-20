# Program ID: word_to_list
# Author: Courtney Ng
# Period: 7
# Program Description: Splits Characters and sets it as own element
word = input("Insert a word that has at least 7 characters")

# Will separate each character and set it as its own element
charList = list(word)

print(charList)
print(len(charList))

for x in range(0,len(charList)):
    print(charList[x])