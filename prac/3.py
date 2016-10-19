char='c'
word="hyderabad"
para="""
India is my country
All indians are my brothers and sisters
except my wife"""
print(type(char))
print(type(str))
print(type(para))




print(char+word)
print(word*10) # repeasts the same word 10 times
# if you want to add specific word to join, here the workaround
print((word+' ')*10)

#string slicing
print(word[0:3]) #print hyd
print(word[-3:]) #print bad
print(word[0:6])

#info: count of the slice is upperIndex-LowerIndex = 6-0 == 6
