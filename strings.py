course = "Coding for Python"
#print(course.find("t"))
print(course.replace('Coding' ,'Code'))
print("tho" in course)
#strings are arrays
a= "Hello World!"
print(a[2])
#looping through a string
b="Banana"
for x in "Banana":
    print(x)
#string length
print(len(a))
#check string
txt="school is free!"
print("free" in txt)
print("free" not in txt)
if "free" in txt:
    print("Yes,'free' is present.")
#slicing
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
#String modification
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("Hello","Hey"))
print(a.split(","))
#concatenation
c=a+b
#c=a +" "+b
print(c)
#string format(combine numbers and strings)
age=36
txt="I am {}"
print(txt.format(age))
quantity=3
itemNo=567
price=49
myOrder="I want {} pieces of item {} for {} dollars."
print(myOrder.format(quantity,itemNo,price))
#using indexes to place correctly
myOrder="I want {2} pieces of item {0} for {1} dollars."
print(myOrder.format(quantity,itemNo,price))