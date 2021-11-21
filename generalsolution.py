# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:04:10 2021

@author: Sharayu
"""


s=2
i=1



list={10,1,8,3,6,5,4,7,"x","y"}


while i<10:
    if(i%2==1):
        list[i]=list[1]
        list[1]+=2
    else:
        list[i]=list[0]-s
        s+=2
    i+=1

print("X="+str(list[x]))
print("Y="+str(list[y]))


#I am unable to find out errors in this program please help me cap