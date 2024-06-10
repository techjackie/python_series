# wc => white chocolate, dc => dark chocolate
chocolate_box = ['wc','dc', 'wc', 'wc', 'dc']

# For Loop
"""
    for ele in iteratable_objects:
        logic
"""
for chocolate in chocolate_box:
    if chocolate == "dc":
        break

    print(chocolate)


for number in range(1, 10, 2): #[1,3,5, 7].. 1, 3,5 
    print(number)


# While Loop
steps = 0

"""
while condition:
   logic

"""

while steps <= 10:
    print("step ",steps)
    break
    steps += 1

else:
    print("Steps has been finished.")    
