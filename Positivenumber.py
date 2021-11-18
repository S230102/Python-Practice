# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 01:04:16 2021

@author: Sharayu
"""

NumList=[]

Number = int(input("Please enter the total number of list element: "))
for i in range(1,Number+1):
    value=int(input("Please enter the value of %d element "%i))
    NumList.append(value)
print("\nInput Numbers in th list are:")
for k in range(Number):
    print(NumList[k],end=" ")
print("\nPositive Numbers in this List are: ")
for j in range(Number):
    if(NumList[j]>=0):
        print(NumList[j],end=" ")
