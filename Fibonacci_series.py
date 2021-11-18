# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 00:54:58 2021

@author: Sharayu
"""

n=int(input("Enter the number of terms: "))
a=0
b=1

sum=0
count=1

print("Fibonacci Series: ",end = " ")
while(count<=n):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b
