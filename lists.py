thislist=["apple","kiwi","cherry"]
print(thislist)
#list length
print(len(thislist))
#list data type(can be different)
print(type(thislist))
#list() constructor
mylist=list(("kiwi","cherry","banana"))
print(mylist)
#lists are ordered,changeable and allows duplicate
print(thislist[2])
print(mylist[-1])
#change list items
thislist[1]="pineapple"
print(thislist)
#change range of values
thislist[1:3]=["apple","banana"]
print(thislist)
mylist.insert(2,"watermelon")
print(mylist)
#add list items
mylist.append("orange")
print(mylist)
#append elements from another list to current list
mylist.extend(thislist)
print(mylist)
#remove list items
thislist.remove("apple")
print(thislist)
mylist.pop(2)
print(mylist)
#delete entire list
#del thislist[2]
mylist.clear()
print(mylist)
#loop lists
ourlist=['kiwi', 'cherry', 'watermelon', 'banana', 'orange', 'apple', 'apple', 'banana']
#for x in ourlist:
# print(x)
#loop through using indexes
#for i in range(len(ourlist)):
 #   print(ourlist[i])
#while loop
i=0
while i<len(ourlist):
    print(ourlist[i])
    i=i+1
#sorting lists
ourlist.sort()
print(ourlist)
#sort in descending order
ourlist.sort(reverse=True)
print(ourlist)
#reverse order
ourlist.reverse()
print(ourlist)
#copying lists
thislist=["peaches","berries","chillies"]
#thislist=list(ourlist)
#print(thislist)
#thislist=ourlist.copy()
print(thislist)
#join lists
allList=ourlist+thislist
print(allList)



