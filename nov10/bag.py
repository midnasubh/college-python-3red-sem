import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
# Sample dataset
df=pd.DataFrame({
        'Text':[
        'Cates are moving quickly',
        'dogs we bucking loudly',
        'he studies in university',
        'they are running to reach the target' 
    ]
})
print("Original dataFrame:")
print(df)
#Initize Count vectorizer
vectorizer=CountVectorizer()
#fill and transform text data
X=vectorizer.fit_transform(df['Text'])
#Convert to dataFrame
bow_df=pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names_out())
print("\nBag-of-words representation:")
print(bow_df)