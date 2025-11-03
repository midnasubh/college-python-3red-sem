n=input("Enter a string :")
# 65-90
# 97-122
l = list(n)
filtered = []
for char in l:
    s = ord(char)
    if not (65 <= s <= 90 or 97 <= s <= 122):
        filtered.append(char)

if filtered == l:
    print("pangram")
