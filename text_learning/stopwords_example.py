#! /usr/bin/env python

from nltk.corpus import stopwords

sw = stopwords.words("english")

#number of stopwords in list

print "number of stopwords:", len(sw)

for word in sw[0:10]:
    print word
