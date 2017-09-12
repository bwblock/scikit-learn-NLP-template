#! /usr/bin/env python


import sklearn
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
string0 = "hi Katie the self driving car will be late"
string1 = "Hi Sebastian the machine learning class will be great great great"
string2 = "Hi Katie the machine learning class will be most excellent"
email_list = [string0,string1,string2]

#  assign list indices to all words in corpus
bag_of_words = vectorizer.fit(email_list)

# count words in corpus

# format (x,y)  z
#  in document number x, word number y appears z times

bag_of_words = vectorizer.transform(email_list)

print bag_of_words

print vectorizer.vocabulary_.get("great")

