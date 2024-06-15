"""
name, age, gender
"""

student_1 = ["raju",18, "male"]

# {"key":"value"}
student_1 = {"name":"raju",'age':18, "gender":"male"}

# dict[key]
print(student_1['age'])

# printing keys
print(student_1.values())

# dict()
students = dict()

# set
fruits = {"mango","apple",10}
fruits.add('orange')
fruits.remove('mango')
print(fruits)

# set()
names = ['raju','ramu','raju']
names = set(names)
names = list(names)

print(names)
