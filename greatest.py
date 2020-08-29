# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:02:54 2020

@author: Acer
"""

a=float(input("enter the first number: "))
b=float(input("enter the second number: "))
c=float(input("enter the third number: "))
if(a>b and a>c):
    print("first number is greater :",a)
elif(b>c and b>a):
    print("second number is greater :",b)
else:
    print("thirh number is greater:",c)   