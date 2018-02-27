#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:17:19 2018

@author: jredpath

Cheating Hangman
"""
import time

def generateWordList():
    acceptedWords = []
    with open('dictionary.txt') as file:
        for line in file:
            acceptedWords.append(line.strip())
    return acceptedWords

def getMaxWordLength():
    maxWord = 0
    for word in generateWordList():
        if len(word) > maxWord:
            maxWord = len(word)
    return int(maxWord)
    
def gameSetup():
    wordMatches = []
    gameDict = {}
    dashString = ""
    userLength = input('Provide a length for the word: ')
    while userLength.isdigit() is False:
        userLength = input('Try again. Provide a vaild integer for word length: ')
    chooseLength = int(userLength)
    while chooseLength < 0 or chooseLength > getMaxWordLength():
        chooseLength = int(input('Try again. Provide a vaild word length: '))
    numGuesses = int(input('How many guesses would you like? '))
    while numGuesses < 0:
        numGuesses = int(input('Try again. Number must be bigger than 0. '))
    showUsed = input('Do you want a running list of used letters to be displayed? (Y/N): ')
    while showUsed.upper() != 'Y' and showUsed.upper() != 'N':
        showUsed = input('Try again. Please answer Y/N: ')
    for word in generateWordList():
        if len(word) == chooseLength:
            wordMatches.append(word)
    for i in range(chooseLength):
        dashString = '-' + dashString
    for word in wordMatches:
        gameDict[word] = dashString
    return wordMatches, chooseLength, numGuesses, showUsed, gameDict

def play():
    info = gameSetup()
    wordLengthMatches = info[0] 
    wordLength = int(info[1])
    numGuesses = int(info[2])
    showUsed = info[3]
    gameDict = info[4]
    lettersUsed = []
    
    blankDict = {}
    aWord = str(wordLengthMatches[0])
    secretWord = aWord
    for letter in aWord:
        secretWord = secretWord.replace(letter,'-')
    while(numGuesses != 0):
        print('You have', numGuesses, 'guesses remaining.')
        if showUsed.upper() == 'Y':
            print('Letters previously used:', lettersUsed[0:])            
        print(secretWord)
        letterGuessed = input('What letter do you guess? ')
        if letterGuessed in lettersUsed:
            print('ERROR: You already guessed that letter!')
            time.sleep(2)
        if letterGuessed.isalpha() is False:
            print('ERROR: Try again. Not a valid letter.')
            time.sleep(2)
        if letterGuessed not in lettersUsed and letterGuessed.isalpha() is True:
            lettersUsed.append(letterGuessed)
            lettersUsed.sort()
#            for pair in gameDict:
            for word in gameDict:
                if letterGuessed in word:
                    dash = gameDict.get(word)
                if letterGuessed not in word:
                    blankDict[word] = gameDict.get(word)
            #assuming blanDict is the biggest dictionary
            gameDict.clear()
            gameDict.update(blankDict)
            blankDict.clear()
#            print(gameDict)
            numGuesses -= 1
        
    if(numGuesses == 0):
        print('GAME OVER!')
        print('The secret word was', aWord)
        playAgain = input('Would you like to play again? (Y/N) ')
        while playAgain.upper() != 'Y' and playAgain.upper() != 'N':
            playAgain = input('Try again. Please answer Y/N: ')
        if playAgain.upper() == 'Y':
            print('***NEW GAME***')
            play()
        if playAgain.upper() == 'N':
            print('Bye!')
    
    
    
play()
    
            
