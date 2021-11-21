# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 00:50:25 2021

@author: Sharayu
"""

print("Which calculation do you want to do: ")
print("1.Add\n2.Subtract")
choice = int(input("Enter choice: "))
print("Enter two numbers: ")
a = int (input("Enter a: "))
b = int (input("Enter b: "))
if(choice==1):
    print("Your addition is: "+str(a+b))
elif(choice==2):
    print("Your subtraction is: "+str(a-b))
else:
    print("Invalid Choice")