import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
df=pd.DataFrame({
    "Text":[
        'Cats are renning quickly',
        "The sun is shining bright",
        "Dogs are barking loudly"
    ]
})
print("Original")
print(df)
vect=CountVectorizer()
x=vect.fit_transform(df["Text"])
bow_df=pd.DataFrame(x.toarray(),columns=vect.get_feature_names_out())
print("-"*20)
print("bag of words")
print(bow_df)