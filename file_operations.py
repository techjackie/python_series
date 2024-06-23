# open(filename, mode) [r, w, x, a]

# write mode
file = open('sample.txt','w')
file.write('Welcome to Techjackie Series!')
file.close()

# x mode
file = open('sample.txt','x')
file.close()

# read mode 
file = open('sample.txt','r')
content = file.read()
file.close()

print(content)

# using with statement for above read mode
with open('sample.txt','r') as file:
    buff = file.read()

print(buff)    





