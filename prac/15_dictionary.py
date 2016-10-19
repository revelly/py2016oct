#dictionaty

d={"one":1, "two":"one", "three":[3,4,5]}
print(type(d))
print(len(d))


print(d["one"]) # access value
d["four"]=4 # add value
d["two"]=5 #modify value

#print keys
for x in d.keys():
    print(x)

for x in d.values():
    print(x)

for x in d.keys():
    print(d[x])
