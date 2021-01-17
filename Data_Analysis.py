from Get_Rezension import df_google
from datetime import date, timedelta

df_google=df_google.replace({"Bewertung: 5,0 von 5,": 5, "Bewertung: 4,0 von 5,": 4, "Bewertung: 3,0 von 5,": 3,
                   "Bewertung: 2,0 von 5,": 2, "Bewertung: 1,0 von 5,": 1})

# how to deal with the date?
df_google.date.unique()

df_google= df_google.replace({"vor einem Monat": date.today() - timedelta(30), "vor 2 Monaten":date.today() - timedelta(60),
                              "vor 3 Monaten":date.today() - timedelta(90), "vor 4 Monaten": date.today() - timedelta(120),
                              "vor 5 Monaten": date.today() - timedelta(150), "vor 6 Monaten":date.today() - timedelta(180),
                              "vor 7 Monaten": date.today() - timedelta(210), "vor 8 Monaten": date.today() - timedelta(240),
                              "vor 9 Monaten": date.today() - timedelta(270), "vor 10 Monaten":date.today() - timedelta(300),
                              "vor 11 Monaten": date.today() - timedelta(330), "vor einem Jahr": date.today() - timedelta(365),
                              "vor 2 Jahren":date.today() - timedelta(730), "vor 3 Jahren":date.today() - timedelta(1065),
                              "vor 4 Jahren": date.today() - timedelta(1430)})

# create wordcloud:

from wordcloud import WordCloud
from nltk.corpus import stopwords
import re
import nltk
nltk.download("stopwords")

sentences = df_google["text"].tolist()
words_clean=[]
german_stop_words = stopwords.words('german') # stop word list

for sentence in sentences:
    sentence_low = sentence.lower() # lower case
    sentences_without_punctuation = re.sub(r"[-?!:;.,()0-9\n\r|]","",sentence_low) # remove punctuation
    words_clean.extend(sentences_without_punctuation.split()) # get list with all words

wordcloud = WordCloud(width = 800, height = 800,
            background_color ='white',
            stopwords = german_stop_words, # remove stopwords
            min_font_size = 10).generate(" ".join(words_clean))

# to make it better: spelling check and remove stopwords
# second approach only adjectives?
# or check for a word net






