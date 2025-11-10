l=[1,2,1,3,1,2,10,8]
print("original list:",l)
print(set(l))

def dubfor(l):
    l2=[]
    for i in l:
        if l2.count(i)==0:
            l2.append(i)
    return l2
print(dubfor(l))
print(dict.fromkeys(l))