import numpy  # linear algebra
import pandas  # data processing
import os
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
def get_all_query(title, author, text):
    total = title + author + text
    total = [total]
    return total
def remove_punctuation_stopwords_lemma(sentence):
    filter_sentence = ''
    lemmatizer = WordNetLemmatizer()
    sentence = re.sub(r'[^\w\s]',
                      '',
                      str(sentence))
    words = nltk.word_tokenize(sentence)  # tokenization
    stop_words = stopwords.words('english')
    words = [w for w in words if not w in stop_words]
    for word in words:
        filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
    return filter_sentence
