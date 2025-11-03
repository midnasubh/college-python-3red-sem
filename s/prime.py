import math
num=int(input("Enter a number :"))

c=0

# for i in range(2,num):
#     if num%i==0:
#         c+=1
# if c==0:
#     print(f"your number is prime {num}")
# else:
#     print(f"your number is not prime {num}")



# for i in range(2,num//2):
#     if num%i==0:
#         c+=1
# if c==0:
#     print(f"your number is prime {num}")
# else:
#     print(f"your number is not prime {num}")


for i in range(2,int(math.sqrt(num)+1)):
    if num%i==0:
        c+=1
if c==0:
    print(f"your number is prime {num}")
else:
    print(f"your number is not prime {num}")

