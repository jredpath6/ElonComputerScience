#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:50:01 2018

@author: Jack Redpath
@homework Lab 1: Krypton excersses
"""

from string import ascii_uppercase as alphabet

def lvl1():
    
    code = "YRIRY GJB CNFFJBEQ EBGGRA" 
    for i in range(len(alphabet)):
        adjustment = alphabet[i:] + alphabet[:i]
        translate = alphabet.maketrans(alphabet, adjustment)
        print(code.translate(translate))

lvl1()
        
def lvl2():
    cipher = "OMQEMDUEQMEK"
    for i in range(len(alphabet)):
        adjustment = alphabet[i:] + alphabet[:i]
        translate = alphabet.maketrans(alphabet, adjustment)
        print(cipher.translate(translate))
lvl2()

def lvl3():
    cipher = "KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS"
    adjustment = "BOIHGKNQVTWYURXZAJEMSLDFPC"

    translate = alphabet.maketrans(alphabet, adjustment)
    print(cipher.translate(translate))
lvl3()
