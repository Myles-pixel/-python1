#use to store data values in key
#key and value pairs,
#ordered,changeable and no duplicates
mydict={
    "brand":"Ford",
    "model":"Mustang"
    #"year":1972
}
#access dictionaries
x=mydict["model"]
print(x)
y=mydict("brand")
print(y)
#returns a list of all keys
z=mydict.keys()
print(z)
#get values of the keys
m=mydict.values()
print(m)
k=mydict.items()
print(k)
#check if keys exists
if "model" in mydict:
    print("model present")
#change items
mydict["year"]=2017
print(mydict)
#add items
mydict["color"]="red"
print(mydict)