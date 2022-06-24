#store multiple items in a single variable
#ordered,unchangeable and allow duplicates
#tuple creation
thistuple=("onion","chillies","broccoli","okra")
print(thistuple)
#tuple length
print(len(thistuple))
#tuple with one item
minituple=("cauliflower",)
print(minituple)
#check tuple data type
print(type(thistuple))
#tuple consructor
mytuple=tuple(("corn","carrot","chives","garlic","kale","chickpeas"))
print(mytuple)
#access tuple
print(mytuple[1])
print(mytuple[2:5])
#check if item exists
if "garlic" in mytuple:
    print("True")
#update tuples
#convert to list,update then convert back to tuple
y=list(mytuple)
y[1]="kiwi"
mytuple=tuple(y)
print(mytuple)
#add items
y=list(mytuple)
y.append("celery")
mytuple=tuple(y)
print(mytuple)
#remove items
y=list(mytuple)
y.remove("kale")
mytuple=tuple(y)
print(mytuple)
#unpacking tuples
fruits=("apple","kiwi","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)
(green,*yellow,red)=fruits
print(green)
print(yellow)
print(red)
#loop through tuples
for x in thistuple:
    print(x)
#looping using while loop
i=0
while i<len(thistuple):
    print(mytuple[i])
    i=i+1
#join tuples
ourTuple=thistuple+fruits
mainTuple=fruits*2
print(mainTuple)
print(mainTuple)
