#write a python program that reads settings.txt and loads the setting and value in a dictionary as key value

f, d=open("settings.txt","r"),{}
for line in f:
    #keyValue=line.split("=")
    #print(line.index("="))
    if '=' in line: d[line[0:line.index("=")]]=line[line.index("=")+1:len(line)]
    #d[line]= keyValue[1]
f.close()
print(d)
