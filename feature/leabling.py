import pandas as pd 
from sklearn.preprocessing import LabelEncoder
data={
    'Fruit':['apple', 'banana','orange','apple','banana'],
    'color' : ['red','yellow','orange','green','yellow']
}
df=pd.DataFrame(data)
print("Original Dataset\n\n",df)
labelEn=LabelEncoder()
dflabelen=df.copy()
dflabelen['Fruit']=labelEn.fit_transform(df["Fruit"])
dflabelen['color']=labelEn.fit_transform(df["color"])
print("---"*10)
print("After Label Encoding \n\n",dflabelen)