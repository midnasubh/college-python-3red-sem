
num=[2,5,90,5,4,50]
n=len(num)
high=num[0]
sec_high=num[1]
for i in range(1,n):
    if high<num[i]:
        sec_high=high
        high=num[i]
    elif high>num[i] and sec_high<num[i]:
        sec_high=num[i]
print(f"second highest number is{sec_high}")

