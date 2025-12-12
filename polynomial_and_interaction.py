
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
df=pd.DataFrame({
    "x1":[2,4,6,3,5],
    "x2":[3,5,7,8,10]
})
print("Oirginal ")
print(df)
poly=PolynomialFeatures(degree=3,include_bias=False)
poly_featues=poly.fit_transform(df)
feature_name=poly.get_feature_names_out(['x1','x2'])
poly_df=pd.DataFrame(poly_featues,columns=feature_name)
print("Polynomial and Interaction Features")
print(poly_df)