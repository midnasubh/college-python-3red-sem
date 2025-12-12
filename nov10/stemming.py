import pandas as pd
from nltk.stem import porterstemmer
from nltk.tokenize import word_tokenize 

nltk.download("punkit_tab")
df=pdDataFrame({
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

stemmer=porterstemmer()

def stem_text(text):
    tokens=word_tokenize(text.lower())
    stems=[stemmer.stem(word) for word in tokens if word.isalpha()]
    returns "".join(stems)
df['stemmed_text']=df['text'].apply(stem_text)
print("\n after stemming:")
print(df[["Text",'Stemmed_text']])