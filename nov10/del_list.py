# list comparizion, rempve,del statment,filter()
n=int(input())
list1=[]
for i in range(n):
    x=input()
    list1.append(x)
print(list1)
# # # using remove
a=int(input(":"))
list.remove(list[a])
print(list)
# using del
del(list[a])
print(list)
# using filter


list2=list(filter(lambda J: J  != a,lis t1))
print(list2)