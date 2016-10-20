# open csv
# print lines which has data greater than 1MB
f,d,lst=open("HourlyHits.csv","r"),{},[]
for line in f:
    if ',' in line:
        index1=line.index(",")
        #print(type(index1))
        index2=line.index(",",index1+1)
        #print (index1," ",index2)
        d["time"]=line[0:index1]
        d["page"]=line[index1+1:index2]
        d["pagesize"]=line[index2+1:len(line)]
        #if int(size) > 1024*1024
print (d)
