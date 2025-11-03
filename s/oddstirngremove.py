s = input("Enter a string: ")
n = int(input("Enter a number: "))
sl = list(s)
del sl[n]
sl = "".join(sl)
print(sl)
# r=s[:n]+s[n+1:]
# print(r)

r=s[::2]
print(r)