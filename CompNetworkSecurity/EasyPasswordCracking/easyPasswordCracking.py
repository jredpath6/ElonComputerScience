#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:43:16 2018

@author: jredpath
"""

import os
import time

tm = time.time()

matches = ["d54ce9de9df77c579775a7b6b1a4bdc0",
           "0d98b597aa732aea606bde680c3b57d8",
           "afdc9c071bdfa235c1fa041758a7dffe",
           "ae0e08163d22befd4635f47bef1b6e3f",
           "d16a974d4d6d0d71b29bfbfe045f1da7",
           "28b60a16b55fd531047c0c958ce14b95",
           "7cd86ecb09aa48c6e620b340f6a74592"]

def superFastLookup():
    f = open("pinTable.txt","r")
    for line in f:
        if line[15:].strip() in matches:
            timeStamp = str(round(time.time()-tm, 2))
            print(line.strip())
    print("That took " + timeStamp + " seconds. I ain't even sweating.")
    
#superFastLookup()

def bruteForce():
    for i in range(0, 10000):
        x = '{:d}'.format(i).zfill(4)
        examine = os.popen("md5 -s " + x).read()
        compare = examine[examine.find('=')+2:].strip()
        if(compare in matches):
            timeStamp = str(round(time.time()-tm, 2))
            print ("Password for " + compare + " is: " + x + " and took " + 
                   timeStamp + " seconds to find.")
            matches.remove(compare)
            
bruteForce()
            
def generateLookupTable():
    for i in range(0, 10000):
        x = '{:d}'.format(i).zfill(4)
        print(os.popen("md5 -s " + x).read().strip())
        
#generateLookupTable()