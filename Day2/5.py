f=open("sample.txt","r")
print(f.tell())
print(f.readline())
print(f.tell())

f.seek(5,0)
print(f.readline())

f.close()


"""
f.seek(n,m)
n=integer
m=integer but limited to 0, 1, 2
    0 - begining of file
    1 - current location
    2 - end of file

"""
