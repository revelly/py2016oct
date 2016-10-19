a=10 #global variable
def abc():
    a=20 #local variable
    print(a)

print(a)
abc()


#docstring
def add(x, y):
    """
This funtion takes two integers and return their sum
usage: add(3,4) returns 7
""" #Doc string: Documentation string
    return x+y

print(add(4,5))

help(add)
