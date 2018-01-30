# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:43:14 2018

@author: Chris Dryden
"""
import re


f = open('words.txt', 'r')
longest = 0
longestword = ' '
for word in f:
    if re.match("^[ABCDEF]*$", word):
        length = len(word)
        if length > longest:
            longest = length
            longestword = word
print("longest word is " + longestword)