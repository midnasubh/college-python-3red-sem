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
>>>>>>> 59fb9afcc8fee418f11b8b598fab4bd42320a753
# tf*idf