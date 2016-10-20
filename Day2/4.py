#print options end chararter
"""fin=open("sample.txt","r")
for line in fin:
    print(line.rstrip())
"""

# this option works only in 3 version
fin=open("sample.txt","r")
for line in fin:
    print(line.rstrip(), end="")
