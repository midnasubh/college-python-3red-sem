n=int(input("Enter a number :"))
s=0
for i in range(1,n+1):
    s=s+(i**3)
print(f"cube sum of first {n} natural number is {s}")