#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:01:06 2018

@author: jredpath
"""

import os
import time

tm = time.time()

passwordHashes = ["31ba00b8e52d322fcdde1640b7634aaf",
                  "43a2599f56d77d379de1a344ba402f6d",
                  "6a54b9a7decc730b187633d6f82ee4db",
                  "7fa23d8a7a6f09ccf3d266ddceb45c05",
                  "c490c792560b0449d24d20555fe0a9fd",
                  "cbe54e698b1169cb94a03b1de95afa40",
                  "fee7d7c096ad91bb6baf65ee6ce9b836",
                  "ffc92c458b8c2fae185c283126663580"]

def makeLookupTable():
    md5hash = open('hashLookup.txt', 'w')
    with open('google-10000-english.txt') as file:
        for word in file:
            md5hash.write((os.popen("md5 -s " + word).readlines[0]))
#makeLookupTable()
            
def numbersAfterWords():
    numberHash = open('numberHash.txt', 'w')
    with open('google-10000-english.txt') as file:
        for word in file:
            for i in range(1000):
                numberHash.write(os.popen("md5 -s " + word.strip('\n') + str(i)).read())
#                examine = os.popen("md5 -s " + word.strip() + str(i)).read()
#                print(examine)
#                compare = examine[examine.find('=')+2:].strip()
#                if compare in passwordHashes:
#                    print(examine)
            for i in range(1000):
                x = '{:d}'.format(i).zfill(2)
                numberHash.write(os.popen("md5 -s " + word.strip('\n') + str(x)).read())
            for i in range(1000):
                x = '{:d}'.format(i).zfill(3)
                numberHash.write(os.popen("md5 -s " + word.strip('\n') + str(x)).read())

            
numbersAfterWords()

def asciiLettersOnly():
    with open('hashLookup.txt','r') as file:
        for word in file:
            compare = word[word.find('=')+2:].strip()
            if compare in passwordHashes:
                timeStamp = str(round(time.time()-tm, 2))
                print(word.strip(), "\n", timeStamp)
#asciiLettersOnly()