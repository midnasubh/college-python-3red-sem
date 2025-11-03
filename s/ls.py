n=int(input("Enter a number : "))
l=[]
c=0
for i in range(n):
    r=int(input(f"Enter {i+1} element : "))
    l.append(r)
key=int(input("what number you want to search : "))

for i in range(n):
    if l[i]==key:
        c+=1
        break
if c!=0:
    print(f"{key} this number is present in {l}")
else:
    print(f"{key} this number is not present in {l}")