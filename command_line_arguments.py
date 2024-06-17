import sys

# [cmd_args.py, --help]
arg1 = sys.argv[1]

if len(sys.argv) == 4:
    arg2 = int(sys.argv[2])
    arg3 = int(sys.argv[3])

if arg1 == "sum":
    print("Sum of numbers: ",arg2+arg3)

elif arg1 == "mul":
    print("Multiplication of numbers: ",arg2*arg3)    

elif arg1 == "--help":
    print('=> Currently you can perfrom only sum and multiplication')    