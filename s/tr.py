a=10
b=15
print("a:",a,"b:",b)
print("Without using 3rd variable\n")
# a,b=b,a
a=a+b
b=a-b
a=a-b
print("a:",a,"b:",b)


print("Using 3rd variable :\n")
c=a
a=b
b=c
print("a:",a,"b:",b)
