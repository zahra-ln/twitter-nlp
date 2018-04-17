import operator
import os, fnmatch, codecs
import re
import pathlib

counter = 0
inverted_indext = {}
for dirpath, dirs, files in os.walk('nlp/step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename), 'r', encoding="utf-8")as f:

            for word in f.read().split():
                if word not in inverted_indext:
                    list = []
                    list.append(str(filename).replace(".txt", ""))
                    data = {"c": 1, "l": list}
                    inverted_indext[word] = data

                else:
                    list = []
                    inverted_indext[word]["c"] += 1
                    for a in inverted_indext[word]["l"]:
                        list.append(a)

                    list.append(str(filename).replace(".txt", ""))
                    inverted_indext[word]["l"] = list;

            f.close();

s = input("Enter Key : ")
finalList = []
commonList = []

for v in s.split():
    if (v in inverted_indext) :
        if (len(finalList) > 0):
            finalList = set(finalList) & set(inverted_indext[v]["l"])
        else:
            finalList = inverted_indext[v]["l"]

        commonList = set(commonList) | set(inverted_indext[v]["l"])

Tweet_Step2 = 'nlp/step2/'

if (len(finalList) > 0) :
    for a in finalList:
        f = codecs.open(os.path.join(Tweet_Step2, a + ".txt"), 'r', encoding="utf-8")
        print(f.read() + "\n" + "*" * 20)


commonList = set(commonList) - set(finalList)

if (len(commonList) > 0):
    for a in commonList:
        f = codecs.open(os.path.join(Tweet_Step2, a + ".txt"), 'r', encoding="utf-8")
        print(f.read() + "\n" + "*" * 20)
