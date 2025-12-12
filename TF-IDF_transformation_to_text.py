<<<<<<< HEAD
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
df=pd.DataFrame({
    "Text":[
        'Cats are renning quickly',

        "Dogs are barking loudly"
    ]
})
print("Original")
print(df)
tf=TfidfVectorizer()
x=tf.fit_transform(df["Text"])
tf_df=pd.DataFrame(x.toarray(),columns=tf.get_feature_names_out())
print("_"*20)
print("TF-IDF representation ")
print(tf_df )
=======
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
df=pd.DataFrame({
    "Text":[
        'Cats are renning quickly',

        "Dogs are barking loudly"
    ]
})
print("Original")
print(df)
tf=TfidfVectorizer()
x=tf.fit_transform(df["Text"])
tf_df=pd.DataFrame(x.toarray(),columns=tf.get_feature_names_out())
print("_"*20)
print("TF-IDF representation ")
print(tf_df )
>>>>>>> 421369c (Add various data processing and transformation scripts including TF-IDF, bag of words, equal frequency and width binning, image manipulation, and lemmatization)
# tf*idf