#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:48:43 2018

@author: jredpath
"""

def createDictionary():
    pirateDictionary = {}
    with open('Translation.txt') as file:
        for line in file:
            english, pirate = line.strip().split(':')
            pirateDictionary[english] = pirate
        return pirateDictionary

def main(pirateDict):
    userPhrase = input('Enter a sentance or q to quit: ')
    while userPhrase != 'Q' and userPhrase != 'q':
        for english in pirateDict:
            userPhrase = userPhrase.replace(english, pirateDict[english])
            print(userPhrase)
            userPhrase = input('Enter a sentance or q to quit: ')
#            else:
#                print('Word not recognized. Try again')
#                userPhrase = input('Enter a sentance or q to quit: ')
            
pirateDict = createDictionary()
main(pirateDict)
            