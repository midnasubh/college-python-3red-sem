a=int(input("Enter a number:"))
sod=0
temp=a
while temp>0:
    sod+=temp%10
    temp//=10
    if a%sod==0:
        print(a,"is a harshad number")
    else:
        print(a,"is not a harshad number")

