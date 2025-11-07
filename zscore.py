import numpy as np
data=np.array([200,300,400,600,1000])
mean=np.mean(data)
std=np.std(data)
scaled_data=(data-mean)/std
print("Original Data:",data)
print("Mean:",mean)
print("Standard Deviation:",std)
print("Z-score Scaled Data:\n",scaled_data)
