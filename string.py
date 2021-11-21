# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 23:28:35 2021

@author: Sharayu
"""

a="Hello"
print(a)

a="Hello,World!"
print(a[1])

for x in "banana":
    print(x)

a="Hello,World!"
print(len(a))

txt="The best things in life are free!"
print("free"in txt)

txt="The best things in life are free!"
print("expensive" not in txt)

b="Hello,World!"
print(b[2:5])

b="Hello,World!"
print(b[:5])

b="Hello,World!"
print(b[2:])

b="Hello, World!"
print(b[-5:-2])

a="Hello,World!"
print(a.upper())

print(a.lower())

print(a.strip())

print(a.replace("H","J"))

print(a.split(","))

a="Hello"
b="World"
c=a+b
print(c)

c=a+" "+b
print(c)

age=19
txt="My name is Sharayu, I am "+str(age)
print(txt)

txt="My name is Sharayu, and I am {}"
print(txt.format(age))

quantity=3
itemno=567
price=49.95
myorder="I want {} pieces of items {} for {} dollars."
print(myorder.format(quantity,itemno,price))

quantity=3
itemno=567
price=49.95
myorder="I want {2} pieces of items {0} for {1} dollars."
print(myorder.format(quantity,itemno,price))

print("We are the so-called \"Vikings\" from the north.")
