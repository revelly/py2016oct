#working with lists
marks =[45,78,67,90,89,67,56,78]
print("Sum: ",sum(marks))
print("Number of elements: ",len(marks))
print("Min: ",min(marks))
print("Max: ", max(marks))
print("Avg: ",sum(marks)/len(marks))


print(marks[0])
print(marks[-2])
print(sum(marks[4:8]))
print(marks[0:3])

marks[0]=55 #modify element at 0
print(marks)

marks.append(99)
print(marks)
marks.insert(2, 100)
print(marks)
marks.pop()
print(marks)
marks.remove(89)
print(marks)
marks.append(99)
marks.append(99)
print(marks.count(99)) #just query, doesnt modifies list
print(marks.index(99)) #just query, doesnt modifies list
marks.reverse()
print(marks)
marks.sort()
print(marks)
