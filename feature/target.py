import pandas as pd 
import numpy as np 
from category_encoders import TargetEncoder
from sklearn.preprocessing import LabelEncoder
data={
    'Fruit':['apple', 'banana','orange','apple','banana'],
    'color' : ['red','yellow','orange','green','yellow']
}
df=pd.DataFrame(data)
print("Original Dataset\n\n",df)
labelEn=LabelEncoder()
df['fruit']=labelEn.fit_transform(df["Fruit"])

targen=TargetEncoder()
dftargen=df.copy()
dftargen[['Fruit','color']]=targen.fit_transform(df[['Fruit','color']],df['Fruit'])

print('\n After Target Encoding\n')
print(dftargen)