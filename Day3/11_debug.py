#sample program for debugger
a=1
b=2
c=3
def abc():
    a=30
    b=40
    c=50
    a=a+1
    b=b+2
    c=c+3
for z in range(2):
    a+=10
    b+=20
    c+=30
abc()
print()
