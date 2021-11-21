# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 01:06:13 2021

@author: Sharayu
"""

mylist = ["game","fruits","food","juice","dress","choclates","bike"]

print(mylist)

print(len(mylist))

print(mylist[1])

print(mylist[-1])

print(mylist[2:5])

print(mylist[:4])

print(mylist[2:])

print(mylist[-4:-1])

if "food"  in mylist:
    print("Food is in mylist")

mylist[6]="place"
print(mylist)


mylist[1:3]=["animal","flower"]
print(mylist)

mylist[1:3]=["insects"]
print(mylist)

mylist.insert(2, "flower")
print(mylist)

mylist.append("plants")
print(mylist)

car=["Ford"]
mylist.extend(car)
print(mylist)

mylist.remove("insects")
print(mylist)

mylist.pop(3)
print(mylist)

del mylist[4]
print(mylist)

for x in mylist:
    print(x)
   
print("---------")
for i in range(len(mylist)):
    print(mylist[i])
   
print("---------")
i=0
while i<len(mylist):
    print(mylist[i])
    i=i+1
    
print("----------")
[print (x) for x in mylist]

print("--------")
newlist=[x for x in mylist if "a" in x]
print(newlist)

newlist=[x for x in mylist if x!="juice"]
print(newlist)

newlist=[a.upper() for a in mylist]
print(newlist)

newlist=['hello' for x in mylist]
print(newlist)

newlist=[x if x!="juice" else "shake" for x in mylist]
print(newlist)

mylist.sort()
print(mylist)

mylist.sort(reverse=True)
print(mylist)

def myfunc(n):
    return abs(n-50)
thislist=[100,50,65,82,23]
thislist.sort(key=myfunc)
print(thislist)

mylist.sort(key=str.lower)
print(mylist)

thislist=mylist.copy()
print(thislist)

list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)

list1.extend(list2)
print(list1)