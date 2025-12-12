a=[('a',1),('b',2),('c',3),('d',4),('a',5)]
d={}
for i in a:
    d[i[0]]=i[1]

print(d)