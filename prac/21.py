#passing a dict by value
def pop(x):
    x.pop()


a=[1,2,3,4,5]
pop(a)
print(a)

#to avoid pass by ref issue

pop(a[:])
print(a)
