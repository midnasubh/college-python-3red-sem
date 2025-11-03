import math
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
c=int(input("Enter a number :"))
s=(a+b+c)/2
area=math.sqrt((s*(s-a)*(s-b)*(s-c)))
print("Area of a triangle is :",round(area,2))
