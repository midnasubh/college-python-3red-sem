n=int(input("Enter a number :"))
s=0
t=n
l=len(str(n))
while t!=0:
    r=t%10
    s=s+r**l
    t=t//10
if s==n:
    print("your number is armstrong")
else:
    print("your number is armstrong")