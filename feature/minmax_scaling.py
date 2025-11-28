import numpy as np
from sklearn.preprocessing import MinMaxScaler
data1=[[3,2],[15,6],[0,10],[1,18]]
scaler=MinMaxScaler()

data=np.array([200,300,400,600,1000])
minval=np.min(data)
maxval=np.max(data)
scale=(data -minval)/(maxval-minval)
print(data)
print(scale)


print(scaler.fit(data1))
print(scaler.data_min_)
print(scaler.data_max_)
print(scaler.transform(data1))
