a=[123,(12123,"swd"),564,23,45,78]
x=(123,12123,564,23,45,78)
b=[]
b=a[:]#1
print(b)
print(list(x))#2
c=[i for i in a]#3
print(c)