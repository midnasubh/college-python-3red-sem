n=int(input("upper bound :"))
a=int(input("lower bound :"))
t=0
c=0
s=0
for i in range(a,n+1):
    t=i
    c=len(str(i))
    s=0
    while t!=0:
        r=t%10
        s=s+(r**c)
        t=t//10
        
    if i==s:
        print(i)



# i=n
# t=n
# c=len(str(n))
# while t!=0:
#     r=t%10
#     s=s+(r**c)
#     t=t//10
        
# if i==s:
#     print(i)