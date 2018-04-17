# -*- coding: utf-8 -*-import twitter_config
import operator
import os, fnmatch, codecs
import re
import pathlib

counter = 0
wordcount = {}
for dirpath, dirs, files in os.walk('nlp/step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename), 'r', encoding="utf-8")as f:

            for word in f.read().split():
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1

            f.close();

sortedKeys = []

for k,v in sorted(wordcount.items() , key=operator.itemgetter(1)):
    sortedKeys.append(k);

Tweet_Step3 = 'nlp/step3/'
pathlib.Path(Tweet_Step3).mkdir(parents=True, exist_ok=True)
f = codecs.open(os.path.join(Tweet_Step3, "word-frequency.txt"), 'w', encoding="utf-8")

sortedKeys.reverse()
for k in sortedKeys:
   f.write(str(k) + " : " + str(wordcount[k]) + "\n")