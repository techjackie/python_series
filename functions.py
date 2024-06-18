def sum():
    num1 = int(input("Enter a number1: "))
    num2 = int(input("Enter a number2: "))

    print(num1+num2)

# Function Definition
"""
def function_name(parameters):
    logic
"""

# function_name(arguments)
sum()

def mul(num1, num2):
    print(num1*num2)

mul(1,2)

# Keyword Arguments
def fruit_display(f_name, f_color):
    print("Fruit name: ",f_name)
    print("Color: ",f_color)

fruit_display(f_color="Yellow",f_name="Mango")    


# Arbitrary Positional Arguments
def trolly(*items):
    for item in items:
        print(item)

trolly('biscut','cake')
trolly('vegetables','fruits','glass','sugar')

# Arbitrary Keyword Arguments
def trolly(**items):
    for k,v in items.items():
        print(f"{k}: {v}")

trolly(item1="biscut",item2="cake")

# Format function in print
item = "biscut"
print(f"My item is {item}")        