# Program ID: string_variables
# Author: Courtney Ng
# Period: 7
# Program Description: Creating the quadratic solver

a = int (input ("What is a?"))
b = int (input ("What is b?"))
c = int (input ("What is c?"))

# print ((-1 * b) + (((b ** 2) - (4 * a * c)) / (2 * a)) ** (1 / 2)) % (b, b, a, c, a)
# print ("If I combine %d and %d I get %d") % (b, b, b + b)
# print ("If I add %d, %d and %d, I get %d." % (b, b, b, b + b))
# print ()
# print ((-1 * b) + (((b ** 2) - (4 * a * c)) / (2 * a)) ** (1 / 2)) % (b, b, a, c, a))

d = (b ** 2) - (4 * a * c)
e = d ** .5
x1 = (-b + e) / (2*a)
x2 = (-b - e) / (2*a)
print (x1, x2)

q1 = ((-b + (((b ** 2) - (4 * a * c)) ** .5)) / (2 * a))
q2 = ((-b - (((b ** 2) - (4 * a * c)) ** .5)) / (2 * a))

print (q1, q2)
