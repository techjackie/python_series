fruits = ["mango","orange",1]

# adding elements
fruits.append("apple")
fruits.insert(1, "banana")


# updating the elements list_name[pos] = value
fruits[1] = "water melon"

# removing the elements by value
fruits.remove("orange")

# removing the elements based on index
fruits.pop(0)

print(len(fruits))
