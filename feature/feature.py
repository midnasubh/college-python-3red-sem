import pandas as pd 
import numpy as np 
from sklearn.impute import SimpleImputer
data={
    'age':[35,np.nan,31,67,59],
    'Testscore':[85,90,np.nan,78,92],
    'grade':['A','B',np.nan,'C','A']

}
df=pd.DataFrame(data)
print("original data:")
print(df)

imputer=SimpleImputer(strategy='mean')
df_imp=pd.DataFrame(imputer.fit_transform(df[['age','Testscore']]),columns=[['age','Testscore']])
df['age']=df_imp['age']
df['Testscore']=df_imp['Testscore']
print("\nAfter mean Imputation")
print(df)