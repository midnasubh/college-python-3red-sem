import numpy as np
data=np.array([200,300,400,600,1000])
minval=np.min(data)
maxval=np.max(data)
scale=(data -minval)/(maxval-minval)
print(data)
print(scale)