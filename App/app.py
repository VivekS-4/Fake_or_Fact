#!/usr/bin/env python3
from flask import Flask, request, render_template
import joblib
from feature import *
pipeline = joblib.load('pipeline.sav')
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/api',methods=['POST'])
def get_delay():
    result=request.form
    query_title = result['title']
    query_author = result['author']
    query_text = result['maintext']
    print(query_text)
    query = get_all_query(query_title, query_author, query_text)
    query1 = remove_punctuation_stopwords_lemma(query)
    query1 = [query1]
    pred = pipeline.predict(query1)
    print(pred)
    dic = {1:'real',0:'fake'}
    return f'<html><body><h1>This news is {dic[pred[0]]}</h1> <form action="/"> <button type="submit">back </button> </form></body></html>'
if __name__ == '__main__':
    app.run(port=8080, debug=True)
