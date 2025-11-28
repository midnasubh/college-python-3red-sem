import pandas as pd 
import numpy as np 
from sklearn.impute import SimpleImputer
data={
    'Name':['Ram','sham',np.nan,'ankit','rita','golam',np.nan,'rita'],
    'age':[64,26,35,np.nan,38,42,np.nan,42],
    'Height':[152,np.nan,135,142,np.nan,157,161,146],
    'weight':[68,np.nan,75,70,80,57,43,np.nan],
    'grade':[np.nan,'B',np.nan,'D','C','A',np.nan,'B']

}
df=pd.DataFrame(data)
print("original data:")
print(df)

# imputer=SimpleImputer(strategy='most_frequent')
# df_imp=pd.DataFrame(imputer.fit_transform(df[['Name','age','Height','weight','grade']]),columns=[['Name','age','Height','weight','grade']])
# df['Name']=df_imp['Name']
# df['age']=df_imp['age']
# df['Height']=df_imp['Height']
# df['weight']=df_imp['weight']
# df['grade']=df_imp['grade']
print("\nAfter mean Imputation")
df_f=df.ffill()
df_b=df.bfill()

print(df_b)
print(df_f)
'''26,35,38,42,42,64'''