# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 22:02:34 2021

@author: Hugo
"""

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2


count = 0
for i in range(len(s)):
    if (s[i:i+3]) == "bob":
        count += 1    
print(count)