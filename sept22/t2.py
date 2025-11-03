t=[(100,200,300),(400,500,600),(700,800,900)]
for i,j in enumerate(t):
    # print(i,j)
    t2=list(j)
    t2[-1]=1000
    t[i]=tuple(t2)
print(t)
