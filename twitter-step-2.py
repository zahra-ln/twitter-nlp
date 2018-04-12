# -*- coding: utf-8 -*-import twitter_config
import os,fnmatch,codecs
import re
import pathlib
counter = 0
for dirpath, dirs, files in os.walk('tweets'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8")as f:
            counter +=1
            # خواندن فایل
            tweet = f.read()
            # حذف منشن یا ااسمی افراد
            tweet= re.sub(r'@[A-Za-z0-9_]+', '',tweet)
            # حذف یوآرال
            tweet= re.sub(r'https?://[^ ]+', '', tweet)
            # حذف یوآرال
            tweet= re.sub(r'www.[^ ]+', '', tweet)
            # حذف کاراکترهای خاص
            tweet = re.sub(r"[a-zA-Z!#$()&@0-9:\\/|{}<>?؟=.\"\'…»«;,،_-]", " ", tweet)
            # تبدیل متن به یک خط
            tweet = " ".join(tweet.split())

            Tweet_Step2 = 'nlp/step2/'
            pathlib.Path(Tweet_Step2).mkdir(parents=True, exist_ok=True)

            if len(tweet) > 0 :
                with codecs.open(Tweet_Step2 + filename, 'w',encoding="utf-8") as f:
                    f.write(tweet)


print(str(counter))