num=int(input("Enter a number : "))
s=0
t=num
while num!=0:
    r=num%10
    s=s+r
    num=num//10
if t%s==0:
    print("Hash number ")
else:    
    print("Not Hash number ")


# 21
# 2+1=3
# 21%3==0