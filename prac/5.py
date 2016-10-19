city="hyderabad"
marks=[56,34,56,67,87] # this is list in python
for x in city:
    print(x)
for x in marks:
    print(x)
for index,mark in enumerate(marks):
    print("index: {}, marks: {}".format(index, mark))
for x in range(5, 56, 5): # max number should be exactly like in slicing
    #it wont consider the max (56) number
    print(x)

#count down
for x in range(10, 0, -2):
    print(x)

#decreasing the number
for x in range(10, 9, -2):
    print(x)

    
