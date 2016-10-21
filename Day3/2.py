import os
from datetime import datetime


d=datetime.now()
print(d)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)

indian_date=str(d.day)+'/'+str(d.month)+'/'+str(d.year)
print (indian_date)
