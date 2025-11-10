import numpy as np
l=[[1,2,3],[4,5,6],[7,8,9]]
l23=[i for l2 in l for i in l2]
print(l23)

flat_list = sum(l,list())
print(flat_list)

fl=np.array(l).flatten()
print(fl)