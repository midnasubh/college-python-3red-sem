import pandas as pd
df=pd.DataFrame({
        'Value':[5,12,17,24,35,46,59,63,72]
}) 
print(df)
bins=[0,12,18,60,100]
labels=['Child','Teen','Adult','Senior']
df['Custom_Bin']=pd.cut(df['Value'],bins=bins,labels=labels,right=False)
print(df)