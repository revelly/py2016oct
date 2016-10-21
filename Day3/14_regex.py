#regex examples
import re
#finding
r=re.findall('\d+', '13 blues pens, 9 balls, 6 books, 20 rupess, 34reds')
print (r)


#splitting
r=re.split('[,:-]',"Ramesh,223-rsannareddy@yahoo.com:Trainer")
print(r)

#matching
r=re.match('ba','fdsaf ds f sfsdaf asbar bar blacksheer ba ')
print(r)

#searching
r=re.search('\w{10}', 'ba ba blacksheep ba ba blacksheep')
print(r.group())
print(r.span())
