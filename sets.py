#used to store multiple items in a single variable
#unordered,unchangeable and indexed,not duplicated
#unchangeable, but you can remove items and add new items
#set() constructor
thisset=set(("corn","carrot","chives","garlic","kale","chickpeas"))
print(thisset)
#to access the set componets
#loop through
for x in thisset:
    print(x)
#check for element
print("chives" in thisset)
#adding values to set
thisset.add("kiwi")
print(thisset)
#update(), add items from another set into current set
tropical=set(("onion","chillies","broccoli","okra"))
tropical.update(thisset)
print(tropical)
#removing elements from the set
tropical.remove("chillies")
tropical.discard("chickpeas")
print(tropical)
#pop(): removes last item in the set
tropical.pop()
print(tropical)
#clear(): empties the set
tropical.clear()
print(tropical)
#join sets
ourset=set(("peaches","berries","chillies"))
myset=set(("apple","kiwi","cherry"))
print(ourset)
print(myset)
friuts=ourset.union(myset)
print(friuts)
