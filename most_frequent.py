# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 01:35:47 2021

@author: Sharayu
"""

w=input("Please enter a string :")
def most_frequent(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d

print(most_frequent(w))
