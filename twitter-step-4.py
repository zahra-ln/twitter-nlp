# -*- coding: utf-8 -*-import twitter_config
import os,fnmatch,codecs
import re
import pathlib
counter = 0



Tweet_Step3 = 'nlp/step3/'
f = codecs.open(os.path.join(Tweet_Step3, "word-frequency.txt"), 'r', encoding="utf-8")


Tweet_Step4 = 'nlp/step4/'
pathlib.Path(Tweet_Step4).mkdir(parents=True, exist_ok=True)

stopWords = {}

for x in range(0 , 19) :
    line = f.readline();
    str = line.replace(" ", "")
    stopWords[str.split(":")[0]] = str.split(":")[1];

for dirpath, dirs, files in os.walk('nlp/step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename), 'r', encoding="utf-8")as f:
            pretext = f.read();
            text = pretext;
            for word in pretext.split():
                if word in stopWords:
                    text = text.replace(" " + word + " " , " ");

            ff = codecs.open(os.path.join(Tweet_Step4, filename), 'w', encoding="utf-8")
            ff.write(text)

f.close();