import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
# Download required resources
nltk.download('punkit_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
# sample dataset
df=pd.DataFrame({
    'Text':[
        'Cates are moving quickly.',
        'dogs we bucking loudly!',
        'he studies in university.',
        'they are enjoyning the holidays.' 
    ]
})
print("Original DataFrame:")
print(df)
# initialize lemmatizer
lemmatizer=WordNetLemmatizer()
#function to lemmatize text
def lemmatize_text(text):
    tokens=word_tokenize(text.lower())
    lemmas=[lemmatizer.lemmatize(word) for word in tokens if word.isalpha()]
    return" ".join(lemmas)
df['Lemmatized_Text']=df['Text'].apply(lemmatize_text)
print("\nAfter Lemmatization:")
print(df[['Text','Lemmatized_Text']])