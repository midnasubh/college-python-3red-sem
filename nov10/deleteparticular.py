l=[1,2,1,3,1,2,10,8]
print(l)
l2=[i for i in l if i !=1]
print(l2)
l.remove(1)
print(l)
del l[-1]
print(l)
l3=list(filter(lambda x:x!=2,l))
print(l3)