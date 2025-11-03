n=int(input("Enter a number :"))
a,b,c=0,1,0

for i in range(n):
    c=a+b
    print(a)
    a=b
    b=c
