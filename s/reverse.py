n=int(input("Enter a number :"))
t=n
n=str(n)
n=int(n[::-1])
print(n)

if t==n:
    print("your number is palindrome")
else:
    print("your number is not palindrome")
# t=n
# s=0
# while t!=0:
#     r=t%10
#     s=(s*10)+r
#     t=t//10
# print(s)