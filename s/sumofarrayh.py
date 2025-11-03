import random
n=int(input("Enter a number :"))
l=[random.randint(1,100) for i in range(n)]
print(l)
print(sum(l))
