# file readings
words=["India","is","my", "country"]
f=open("sample.txt","a")
f.write("This is my first line"+"\n")
for word in words:
    f.write(word+"\n\t")
f.close()

print("Print using f.read()")
f=open("sample.txt","r")
print(f.read())


print("Read char by char")
f=open("sample.txt","r")
print(f.read(1))
print(f.read(1))


print("Read line one at a time")
f=open("sample.txt","r")
print(f.readline())

print("Read all lines")
lines = f.readlines()
for line in lines:
    print(line)
