import random

def generateNumber(Min, Max):
    return random.choice(range(Min,Max))

lstRandom = []
for x in range(100):
    lstRandom.append(generateNumber(10, 500))

print(lstRandom)
print("Items count: {}".format(len(lstRandom)))
print("No of time 99 found ",lstRandom.count(99))
            
