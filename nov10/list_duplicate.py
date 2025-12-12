# rempve duplicate list_i) set(),ii) for loop, iii) fromkeys()
n=int(input(": "))
list=[]
for i in range(n):
    a=(input(" :"))
    list.append(a)
print(set(list))
a=0
def dubfor(list):
    list2=[]
    for i in list:
        if list2.count(i)==0:
            list2.append(i)
    return list2
print(dubfor(list))