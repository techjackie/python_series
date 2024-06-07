# Arithmetic Operations

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))


print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("My remainder is: ",a%b)
print("My Quotient is: ",a//b)
print("Power of 3: ",a**3)

# Assignment Operators
a = 5

a += 5
print(a)

# Logical Operators

# AND operator
age = 14

check = age > 13 and age < 18
print(check)

# OR Operator
age = 20
check = (age == 18) or (age == 20)
print(check)

# NOT Operator
allowed = False
check = not allowed
print(check)

# Identity Operator
a = []
b = []

c = a

print(id(a))
print(id(c))
print(a is c)