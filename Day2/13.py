import sys, math

if len(sys.argv) == 2:
    arg=int(sys.argv[1])
elif len(sys.argv) > 2:
    print("Dnt know what to do with additional number")
    sys.exit()
else:
    arg=int(input("Enter a number "))

print(math.factorial(arg))
