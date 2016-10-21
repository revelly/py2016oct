#simple performance measurement

import time

starttime = time.time()

for x in range(1000):
    x**x
endtime = time.time()
print(endtime-starttime)
print(starttime)
