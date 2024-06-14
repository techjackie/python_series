# packing
fruits = ('apple','orange',1)

print(fruits)
# fruits[0] = "grapes"

# unpacking
(f1, *f2 )= fruits

print(f2)


fruits = list(fruits)
print(type(fruits))