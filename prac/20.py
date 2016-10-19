#function with optional parameters
def circlearea(r, pi=3.14):
    return pi*r**2

print(circlearea(5))
print(circlearea(5, 22/7))


def wish(name, age):
      print(" hello {}, you are {} years old".format(name, age))

wish("India", 12)
wish(67, "India")

wish(age=23, name="India") #keyword argument style
      
