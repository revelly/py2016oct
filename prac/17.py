#write a funtion that takes an integer and returns its factorial


def fact2(x):
    res=1
    for y in range(1,x):
        res*=y
    print("Factorial of {} is {}".format(x, res))

fact2(10)
