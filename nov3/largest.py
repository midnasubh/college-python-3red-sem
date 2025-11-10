num=list(map(int,input("Enter a value:").split()))
n=int(input("Enter a value of n:"))
number=list(set(num))
number.sort(reverse=True)
largest=number[:n]
print(largest)