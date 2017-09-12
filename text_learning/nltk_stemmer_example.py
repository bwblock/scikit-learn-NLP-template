#! /usr/bin/env python


from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

print stemmer.stem("responsiveness")

print stemmer.stem("responsivity")

print stemmer.stem("unresponsive")



