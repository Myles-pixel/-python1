#small anonymous function
#takes any number of arguments,but can only have one expression
x=lambda a:a+10
print(x(5))
#two arguments
y=lambda a,b:a*b
print(y(4,6))
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(4)
print(mydoubler(5))
