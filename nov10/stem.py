import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 
import nltk

nltk.download("punkt")
df=pd.DataFrame({
    "text":[
        'Cates are moving quickly.',
        'dogs we bucking loudly.',
        'he studies in university.',
        'they are enjoyning the holidays.',
        'run fast'
    ]
})
print("Original DataFrame:")
print(df)
stemmer=PorterStemmer()
def stem_text(text):
    tokens=word_tokenizeimport(text.lower())
    stems=[stemmer.stem(word) for word in token if word is alpha()]
    return " ".join(stem)
df['stemmed_Text']=df['Text'].apply(stem_text)
print("\nAfter stemming:")
print(df[["Text",'Stemmed_Text']])