#file options
fin=open("sample.txt","r")
print(fin.name)
print(fin.fileno())
print(fin.mode)
print(fin.closed)
fin.close()
print(fin.closed)
      
print(dir(fin))
